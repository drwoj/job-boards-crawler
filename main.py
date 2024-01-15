import httpx
from selectolax.parser import HTMLParser

url = "https://justjoin.it/"
url2 = "https://justjoin.it/all-locations/data/experience-level_junior/remote_yes"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

response = httpx.get(url2, headers=headers)
html = HTMLParser(response.text)
jobs = html.css("div.css-2crog7")

for job in jobs:
    print(job.css_first("h2.css-16gpjqw").text())


