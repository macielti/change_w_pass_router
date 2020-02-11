from http_router import HttpRouter
import time

wordlist = ["João", "Maria", "Joaquin", "adsadas", "sdsdsd", "sdsd", "dsdsdsd", "sdsdsds", "admin", "hello"]

for w in wordlist:
    
    http = HttpRouter()
    http.getAuthParm()
    http.getBusy()
    test = http.login("admin", w)
    time.sleep(2)
    if test:
        print(w)
        break
