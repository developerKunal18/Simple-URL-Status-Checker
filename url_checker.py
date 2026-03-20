from urllib.request import urlopen
from urllib.error import URLError

url = input("Enter URL: ")

try:
    response = urlopen(url)
    print(f"Status: {response.getcode()} (Website is reachable)")
except URLError:
    print("Website is not reachable")
