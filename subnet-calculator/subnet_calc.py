# subnet calculator
# type an ip with a cidr like 192.168.1.10/24 and it shows the subnet info
# you can also type a normal mask instead of /number, like 192.168.1.10/255.255.255.0

import sys


def ip_to_int(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        raise ValueError("ip must have 4 numbers")
    n = 0
    for p in parts:
        if not p.isdigit() or int(p) > 255:
            raise ValueError("bad ip: " + ip)
        n = (n << 8) + int(p)
    return n


def int_to_ip(n):
    return f"{n >> 24 & 255}.{n >> 16 & 255}.{n >> 8 & 255}.{n & 255}"


def mask_to_cidr(mask_int):
    # count the 1 bits and check the mask is valid (all 1s then all 0s)
    bits = f"{mask_int:032b}"
    if "01" in bits:
        raise ValueError("mask is not valid, 1s and 0s are mixed")
    return bits.count("1")


def calc(ip_str, cidr):
    ip = ip_to_int(ip_str)

    # make the mask: /24 means 24 ones then zeros -> 255.255.255.0
    mask = (0xffffffff << (32 - cidr)) & 0xffffffff
    network = ip & mask
    broadcast = network | (~mask & 0xffffffff)

    # -2 because network and broadcast can't be used by hosts
    usable = 2 ** (32 - cidr) - 2

    print()
    print(f"ip address:      {ip_str}/{cidr}")
    print(f"subnet mask:     {int_to_ip(mask)}")
    print(f"wildcard mask:   {int_to_ip(~mask & 0xffffffff)}")
    print(f"network:         {int_to_ip(network)}")
    print(f"broadcast:       {int_to_ip(broadcast)}")
    if usable > 0:
        print(f"first host:      {int_to_ip(network + 1)}")
        print(f"last host:       {int_to_ip(broadcast - 1)}")
    print(f"usable hosts:    {usable}")


def main():
    print("subnet calculator (type q to quit)")
    while True:
        text = input("\nip/cidr> ").strip().lower()
        if text == "q":
            break
        if "/" not in text:
            print("need a / part, example: 192.168.1.10/24")
            continue

        ip_str, mask_part = text.split("/", 1)

        try:
            ip_to_int(ip_str)
            # the advanced part: accept a normal mask too, not just /24 style
            if "." in mask_part:
                cidr = mask_to_cidr(ip_to_int(mask_part))
            else:
                cidr = int(mask_part)
            if not 0 <= cidr <= 32:
                raise ValueError("cidr must be 0-32")
            calc(ip_str, cidr)
        except ValueError as e:
            print("error:", e)


main()
