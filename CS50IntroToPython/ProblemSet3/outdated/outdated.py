# Months
months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

# Library
from dateutil.parser import parse

# Def main
def main():
    user_input = input("Date: ").strip().title()
    _yyyy_ = user_input[-4:]
    _mm_ = ""

    ## DESIGNATE MONTHS ##
    for month in months:
        if month in user_input:
            _mm_ = months[month]
            variation_A(_yyyy_, _mm_, user_input)
            break
    if not _mm_:
        first_slash = user_input.find("/")
        _mm_ = user_input[:first_slash]
        try:
            if int(_mm_) > 12:
                return main()
        except ValueError:
            return main()
        variation_B(_yyyy_, _mm_, user_input)

    ## VARIATION A ##
def variation_A(_yyyy_, _mm_, user_input):
    comma = user_input.find(",")
    if comma == -1:
        return main()
    else:
        _dd_ = user_input[comma - 2:comma].strip()

    try:
        if int(_dd_) > 31:
            return main()
    except ValueError:
        return main()

    reply(_yyyy_, _mm_, _dd_)

    ## VARIATION B ##
def variation_B(_yyyy_, _mm_, user_input):
    first_slash = user_input.find("/")
    second_slash = user_input.find("/", first_slash + 1)

    _dd_ = user_input[first_slash + 1:second_slash]

    if int(_dd_) > 31:
        return main()
    else:
        reply(_yyyy_, _mm_, _dd_)

    ## FINAL DATE ##
def reply(_yyyy_, _mm_, _dd_):
    try:
        final_date = parse(f"{_yyyy_}-{_mm_}-{_dd_}")
        print(final_date.date())
    except ValueError:
        return main()

# Call main
main()