def ip_to_bin(ip):
    parts = [int(part) for part in ip.split(".")]
    result = ""
    for part in parts:
        result += bin(part)[2:].zfill(8)
    return result

my_ip = "192.168.257.13"
res = ip_to_bin(my_ip)
print(res)
