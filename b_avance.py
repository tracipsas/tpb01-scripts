import a_avance

ips = ["127.0.0.1", "10.2.3.254", "8.8.8.8"]
for ip in ips:
    print("{} -> {}".format(ip, a_avance.ip_to_bin(ip)))
