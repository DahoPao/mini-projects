# log analyzer
# reads a log file and counts failed login attempts per ip
# made for ssh style logs, try it with the included sample_auth.log
# if an ip fails too many times it gets marked as suspicious
# and you can save the list to a file

import sys

DEFAULT_FILE = "sample_auth.log"


def get_failed_ip(line):
    # lines we care about look like:
    # "Failed password for root from 203.0.113.5 port 22 ssh2"
    if "Failed password" not in line:
        return None
    try:
        after = line.split(" from ", 1)[1]
        ip = after.split(" ", 1)[0]
        return ip
    except IndexError:
        return None


def analyze(lines, threshold):
    counts = {}
    for line in lines:
        ip = get_failed_ip(line)
        if ip:
            counts[ip] = counts.get(ip, 0) + 1

    if not counts:
        print("no failed logins found")
        return []

    print(f"\n{len(counts)} ip(s) with failed logins:")
    # sort by count, biggest first
    for ip in sorted(counts, key=counts.get, reverse=True):
        mark = "  <-- suspicious" if counts[ip] >= threshold else ""
        print(f"  {ip:<16} {counts[ip]} failed attempts{mark}")

    suspicious = [ip for ip in counts if counts[ip] >= threshold]
    print(f"\n{len(suspicious)} suspicious ip(s) (>= {threshold} attempts)")
    return suspicious


def main():
    print("log analyzer - failed ssh logins")
    filename = input(f"log file (enter = {DEFAULT_FILE}): ").strip() or DEFAULT_FILE
    try:
        f = open(filename, "r", encoding="utf-8", errors="ignore")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print("file not found:", filename)
        sys.exit(1)

    threshold = input("attempts to count as suspicious (enter = 5): ").strip()
    threshold = int(threshold) if threshold.isdigit() else 5

    suspicious = analyze(lines, threshold)

    # after using it for a bit i wanted the list saved somewhere, for firewall rules
    if suspicious:
        save = input("\nsave suspicious ips to suspicious.txt? (y/n): ").strip().lower()
        if save == "y":
            with open("suspicious.txt", "w") as out:
                for ip in suspicious:
                    out.write(ip + "\n")
            print("saved to suspicious.txt")


main()
