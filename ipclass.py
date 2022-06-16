class Ip:
    def __init__ (self, ip):
        self.ip = ip.split("/")[0]
        self.amoutOfZero = 32 - int(ip.split("/")[1])
        self.binip = self.test()
        self.maxHosts = self.host(self.amoutOfZero)
        self.ipOfLink = self.linkip(self.binip, self.amoutOfZero)
        self.numberInLink = self.number(self.binip, self.amoutOfZero)
        self.broadcastaAddress = self.broadcast(self.binip, self.amoutOfZero)
        self.binmask = self.bin_mask()
        self.mask = self.musk()
    def bin_mask (self):
        mask = ''
        res = ''
        for i in range(32 - self.amoutOfZero):
            mask += '1'
        for i in range(self.amoutOfZero):
            mask += '0'
        for i in range(4):
            res += mask[i*8 : i*8+8] + '.'
        return res[0 : len(res) - 1]
    def musk (self):
        res = ''
        mask = self.binmask
        mask = mask.replace('.', '')
        for i in range (4):
            res += str(int(mask[i*8 : i*8+8], 2)) + '.'
        return res[0 : len(res) - 1]
    def test (self):
        ip = self.ip.split(".")
        for i in range(0, len(ip)):
            ip[i] = str(self.bin_2(ip[i]))
            while len(ip[i]) < 8:
                ip[i] = "0" + ip[i]
        return ".".join(ip)
    def bin_2 (self, n):
        n = int(n)
        b = ''
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        return b
    def host (self, n):
        return 2 ** n - 2
    def bin_10 (self, n):
        res = 0
        n = list(str(n))
        n.reverse()
        for i in range(len(n)):
            if n[i] == "1":
                res = res + 2 ** i
        return res
    def linkip (self, ip, zero):
        res = []
        ip = ip.split(".")
        i = 3
        min = []
        while zero > 0:
            if zero >= 8:
                min.insert(0, str(self.bin_10(ip[i])))
                zero = zero - 8
            else:
                min.insert(0, str(self.bin_10(ip[i][zero : 8])))
                zero = 0
            i = i - 1
        while len(min) < 4:
            min.insert(0, "0")
        for i in range(len(min)):
            res.insert(0, str(self.bin_10(int(ip[len(min) - 1 - i])) - int(min[len(min) - 1 - i])))
        return self.ip + " - " + ".".join(min) + " = " + ".".join(res)
    def number (self, ip, zero):
        ip = ip.split(".")
        ip = "".join(ip)
        return int(self.bin_10(ip[len(ip) - zero : len(ip)]))
    def broadcast (self, ip, mask):
        ip1 = ""
        res = ""
        ip = list(filter(lambda x: x != ".", list(ip)))
        while mask != 0:
            if ip[len(ip) - mask] == "0":
                ip[len(ip) - mask] = "1"
            mask -= 1
        ip = "".join(ip)
        for i in range(4):
            res = res + str(self.bin_10(ip[i*8 : (i + 1)*8])) + "."
        for i in range(4):
            ip1 = ip1 + ip[i*8 : (i+1)*8] + "."
        return ip1[0 : len(ip1) - 1] + " = " + res[0 : len(res) - 1]  
