def test (just_ip):
        just_ip = just_ip.split(".")
        for i in range(0, len(just_ip)):
            just_ip[i] = str(bin_2(just_ip[i]))
            while len(just_ip[i]) < 8:
                just_ip[i] = "0" + just_ip[i]
        return ".".join(just_ip)
def bin_2 (n):
    n = int(n)
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b