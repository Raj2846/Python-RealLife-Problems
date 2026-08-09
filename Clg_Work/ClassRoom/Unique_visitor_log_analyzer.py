"""
A server access log
access_log.txt has one entry per line: IP_ADDRESS - TIMESTAMP - PAGE. Read the
file and report the number of unique visitor IPs (using a set), the total
number of requests, and the single most-visited page. A line that does not
split into exactly three ' - '-separated fields must be skipped and counted as
malformed rather than crashing the program. A missing log file must be handled
with a clear, user-friendly message.
"""

def analyzer_log(filename):
    unique_ips = set()
    total_req = 0
    most_visited_page = 0
    malformed = 0
    pages_count = {}
    first_appereance = {}
    try:
        with open(filename, "r") as fp:
            
            for line in fp:
                line = line.strip()

                if not line:
                    continue

                fields = line.split(" - ")
                # print(fields)

                # count the wrong data lines
                if (len(fields)) != 3:
                    malformed += 1
                    continue

                ip, time, page = fields

                # we store only unique ip addres
                unique_ips.add(ip)
                total_req += 1

                if page not in pages_count:
                    pages_count[page] = 1
                    first_appereance[page] = total_req
                else:
                    pages_count[page] += 1
    except FileNotFoundError:
        print(f"Error : The file '{filename}' was not found ")
        return   

    print(f"Unique IP addresses: {len(unique_ips)}")
    print(f"Total requests: {total_req}")

    if pages_count:
        most_visited_page = max(pages_count, key=lambda page: (
            pages_count[page], -first_appereance[page]))
        
        print(f"Most Visited Pages are {most_visited_page}",
            f"({pages_count[most_visited_page]} visits)"
            )

analyzer_log("access_log.txt")