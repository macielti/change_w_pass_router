from requests import Session
import requests
import base64
import os
import time

class HttpRouter():

    def __init__(self, host="192.168.4.1"):
        self.host = host
        self.session = Session()
        self.s = None

        ###
        headers = {
            'Host': self.host,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }

        response = self.session.get('http://%s/' % self.host, headers=headers, verify=False)


    
    def getAuthParm(self):

        ###
        headers = {
            'Host': self.host,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Origin': 'http://%s' % self.host,
            'DNT': '1',
            'Connection': 'close',
            'Referer': 'http://%s/' % self.host,
            'Content-Length': '0',
        }

        response = self.session.get('http://%s/cgi/getParm' % self.host, headers=headers, verify=False)

        self.userSetting = 1
        self.ret = 0
        ###

        # extract s
        start = response.text.find('"')
        end = response.text.find('"', start + 1)
        self.s = response.text[start + 1:end]
        print("Tempero:", self.s)
    
    def getBusy(self):

        headers = {
            'Host': self.host,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Origin': 'http://%s' % self.host,
            'DNT': '1',
            'Connection': 'close',
            'Referer': 'http://%s/' % self.host,
            'Content-Length': '0',
        }

        response = self.session.get('http://%s/cgi/getBusy' % self.host, headers=headers, verify=False)

        self.isLogined = 0
        self.isBusy = 0
        self.ret = 0
        
    
    def login(self, username="admin", password="admin"):

        # process UserName
        UserName = requests.get("http://localhost:1337/?val=%s&ss=%s&user=1" % (username, self.s)).text
        # process Passwd
        Passwd = requests.get("http://localhost:1337/?val=%s&ss=%s&user=0" % (password, self.s)).text
        

        headers = {
            'Host': self.host,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Origin': 'http://%s' % self.host,
            'DNT': '1',
            'Connection': 'close',
            'Referer': 'http://%s/' % self.host,
            'Content-Length': '0',
        }

        params = (
            ('UserName', UserName),
            ('Passwd', Passwd),
            ('Action', '1'),
            ('LoginStatus', '0'),
        )

        response = self.session.get('http://%s/cgi/login' % self.host, headers=headers, params=params, verify=False)

        if "ret=0" in response.text:
            return True
        return False

    def pos_login_i(self):

        headers = {
            'Host': self.host,
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            'Referer': 'http://%s/' % self.host,
            'Upgrade-Insecure-Requests': '1',
        }

        response = self.session.get('http://%s/' % self.host, headers=headers, verify=False)

        start = response.text.find("token=")
        end = response.text.find('"', start+7)

        self.token = response.text[start+7: end]

    def change_pass(self, passwd):

        command = "./change_pass.sh %s %s %s" % (self.token, self.session.cookies.values()[0], passwd)
        print(command)

if __name__ == "__main__":
    http = HttpRouter()
    http.getAuthParm()
    http.getBusy()
    http.login("admin", "admin")
    http.pos_login_i()
    http.change_pass("testando")
