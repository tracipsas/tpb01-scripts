import a_basique

ips = ["127.0.0.1", "10.2.3.254", "8.8.8.8"]
for ip in ips:
    print("{} -> {}".format(ip, a_basique.ip_to_bin(ip)))
