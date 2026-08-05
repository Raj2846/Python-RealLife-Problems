"""
•1.
Print the current date and time in the format: DD-Mon-YYYY HH:MM AM/PM (e.g.,
03-Aug-2026 02:30 PM).
"""

from datetime import date,datetime,time,timedelta,timezone


now = datetime.now()
formatted_time = now.strftime("%d-%b-%Y %I:%M %p")
print(formatted_time)   