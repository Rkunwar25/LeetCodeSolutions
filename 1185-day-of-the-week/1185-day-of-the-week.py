class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday"]

        # Days in each month
        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        def is_leap(y):
            return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

        total_days = 0

        # Count days from 1971 to year-1
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365

        # Count days from Jan to month-1
        for m in range(1, month):
            total_days += month_days[m - 1]
            if m == 2 and is_leap(year):
                total_days += 1

        # Add current month days
        total_days += day

        # Jan 1, 1971 was Friday → index 5
        return days[(total_days + 4) % 7]
