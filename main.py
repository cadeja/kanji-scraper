import httpx
from selectolax.parser import HTMLParser

def get_html(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"
    }

    resp = httpx.get(url, headers=headers)
    html = HTMLParser(resp.text)
    return html


def main():
    url = ""
    html = get_html(url)

if __name__ == "__main__":
    main()