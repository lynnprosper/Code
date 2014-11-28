import urllib.request
import time

def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "https://twitter.com/statuses", "...", "...")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    resp = urllib.request.urlopen("https://twitter.com/statuses/update.json", params)
    resp.read()
def get_price():
    page = urllib.request.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
    text = page.read().decode("utf8")
    where = text.find("10")
    start_of_price = where + 2
    end_of_price = start_of_price + 2
    return (text[start_of_price:end_of_price])
price_now = input("Do you want to see the price now (Y/N)\n")
if price_now == "Y":
    send_to_twitter(get_price())
else:
    price = 99
    while price > 4:
        time.sleep(900)
        price =get_price()
    send_to_twitter("BUY!")
