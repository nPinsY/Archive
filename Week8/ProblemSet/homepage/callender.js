document.addEventListener('DOMContentLoaded', function() {
    function createCalendar(month, year) {
        const daysInMonth = new Date(year, month, 0).getDate();
        let calendarHtml = "<table class='table table-bordered'><tr>";

        const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        for (let day of daysOfWeek) {
            calendarHtml += `<th>${day}</th>`;
        }

        calendarHtml += "</tr><tr>";

        let dayOfWeek = new Date(year, month - 1, 1).getDay();
        for (let i = 0; i < dayOfWeek; i++) {
            calendarHtml += "<td></td>";
        }

        for (let i = 1; i <= daysInMonth; i++) {
            if (dayOfWeek % 7 === 0) {
                calendarHtml += "</tr><tr>";
            }
            calendarHtml += `<td>${i}</td>`;
            dayOfWeek++;
        }

        while (dayOfWeek % 7 !== 0) {
            calendarHtml += "<td></td>";
            dayOfWeek++;
        }

        calendarHtml += "</tr></table>";
        document.getElementById('calendar').innerHTML = calendarHtml;
    }

    document.getElementById('generateCalendar').addEventListener('click', function() {
        let selectedMonth = document.getElementById('monthSelector').value;
        let selectedYear = document.getElementById('yearInput').value;
        createCalendar(parseInt(selectedMonth), parseInt(selectedYear));
    });

    let currentMonth = new Date().getMonth() + 1;
    let currentYear = new Date().getFullYear();
    createCalendar(currentMonth, currentYear);

    let buttonHomepage = document.querySelector('#buttonHomepage');
    buttonHomepage.addEventListener('click', function() {
        window.location.href = 'index.html';
    });

    let buttonList = document.querySelector('#buttonList');
    buttonList.addEventListener('click', function() {
        window.location.href = 'list.html';
    });

    let buttonVideo = document.querySelector('#buttonVideo');
    buttonVideo.addEventListener('click', function() {
        window.location.href = 'video.html';
    });
});
