from telnetlib import Telnet

class Router():
    
    def __init__(self, host="192.168.4.1", port=23):
        self.tn = Telnet(host, port)
    
    def login(self, password):
        """Authenticate telnet session."""
        self.tn.read_until(b"password:")
        command = password.encode()
        self.tn.write(command + b"\r")
        self.tn.read_until(b"TP-Link(conf)#")
    
    def change_w_pass(self, new_pass):
        """Change Wireless password"""
        command = ("wlctl set --sec psk wpa2 auto " + new_pass + "\r").encode()
        self.tn.write(command)
        self.tn.read_until(b"cmd:SUCC")
    
    def close(self):
        """Close telnet session."""
        self.tn.write(b"exit\r")

if __name__ == "__main__":
    router = Router()
    router.login(password="admin")
    print("LOGIN - OK")
    router.change_w_pass("testedesenha")
    print("CHANGE PASS - OK")
    router.close()
    print("CLOSE CONN - OK")
