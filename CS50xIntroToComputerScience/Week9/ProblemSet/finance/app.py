import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0",
        session["user_id"],
    )

    holdings = []
    grand_total = 0

    for stock in stocks:
        quote = lookup(stock["symbol"])
        total = quote["price"] * stock["total_shares"]
        grand_total += total
        holdings.append(
            {
                "symbol": stock["symbol"],
                "name": quote["name"],
                "shares": stock["total_shares"],
                "price": usd(quote["price"]),
                "total": usd(total),
            }
        )

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
        "cash"
    ]
    grand_total += cash

    return render_template(
        "homepage.html", holdings=holdings, cash=usd(cash), grand_total=usd(grand_total)
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        if not symbol:
            return apology("Must provide stock symbol", 400)

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Must provide valid number of shares", 400)

        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid stock symbol", 400)

        shares = int(shares)
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ]
        cost = shares * stock["price"]

        if cash < cost:
            return apology("Not enough cash", 400)

        db.execute(
            "UPDATE users SET cash = cash - ? WHERE id = ?", cost, session["user_id"]
        )
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
            session["user_id"],
            symbol,
            shares,
            stock["price"],
        )

        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    transactions = db.execute(
        "SELECT symbol, shares, price, transacted FROM transactions WHERE user_id = ? ORDER BY transacted DESC",
        session["user_id"],
    )

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            flash("Must provide username", "warning")
            return render_template("login.html")

        elif not request.form.get("password"):
            flash("Must provide password", "warning")
            return render_template("login.html")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Invalid username and/or password", "warning")
            return render_template("login.html")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares", 0))

        if not symbol:
            return apology("Must provide a stock symbol", 400)

        if shares <= 0:
            return apology("Must provide a positive number of shares", 400)

        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid stock symbol", 400)

        return render_template("quote.html", stock=stock, shares=shares)

    else:
        return render_template("quote.html", stock=None, shares=None)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("password2")

        if not username:
            flash("Must provide username", "warning")
            return redirect("/register")
        elif not password:
            flash("Must provide password", "warning")
            return redirect("/register")
        elif password != confirmation:
            flash("Passwords do not match", "warning")
            return redirect("/register")

        user_check = db.execute("SELECT * FROM users WHERE username = ?", username)
        if user_check:
            flash("Username already taken, please try another", "warning")
            return render_template("register.html")

        hash_password = generate_password_hash(password)
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_password
        )
        flash("Registered successfully!", "success")
        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        if not symbol:
            return apology("Must provide stock symbol", 400)

        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Must provide valid number of shares", 400)

        shares = int(shares)
        owned_shares = db.execute(
            "SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            symbol,
        )[0]["total_shares"]

        if owned_shares is None or owned_shares < shares:
            return apology("Not enough shares", 400)

        stock = lookup(symbol)
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            shares * stock["price"],
            session["user_id"],
        )
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
            session["user_id"],
            symbol,
            -shares,
            stock["price"],
        )

        flash("Sold!")
        return redirect("/")

    else:
        symbols = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            session["user_id"],
        )
        return render_template("sell.html", symbols=symbols)
