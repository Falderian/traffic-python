import requests

urls = ["socks5.txt", "socks4.txt", "http.txt"]
base_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/"
list = []

for url in urls:
    request = requests.get(
        f"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/{url}"
    ).text.split("\n")
    [list.append(x) for x in request]
