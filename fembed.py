import re, sys

import requests


def fmbd(url):
    s = requests.Session()
    url = url.replace("/v/", "/f/")
    raw = s.get(url)
    api = re.search(r"(/api/source/[^\"']+)", raw.text)

    if api is not None:
        raw = s.post("https://www.fembed.com" + api.group(1)).json()
        for d in raw["data"]:
            by = s.head(d['file']).headers.get("Location", d['file'])
            print(f"{d['label']}/{d['type']}: {by}")

if __name__ == "__main__":
    fmbd(sys.argv[1])
