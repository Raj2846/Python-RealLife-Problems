"""
A server access log
access_log.txt has one entry per line: IP_ADDRESS - TIMESTAMP - PAGE. Read the
file and report the number of unique visitor IPs (using a set), the total
number of requests, and the single most-visited page. A line that does not
split into exactly three ' - '-separated fields must be skipped and counted as
malformed rather than crashing the program. A missing log file must be handled
with a clear, user-friendly message.
"""

with open("access_log.txt","r") as fp:
    for i in fp:
        id,date,time,call,ass=i.strip(" ").split("-")
        print(time)