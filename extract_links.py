import requests
import bs4
import sys

def extract_links(url, extract_self_links):
    page_content = requests.get(url).content
    soup = bs4.BeautifulSoup(page_content, "html.parser")
    links = []
    for a_tag in soup.find_all("a"):
        link = a_tag.get("href")
        if not extract_self_links and not link.startswith("http"):
            # do not capture
            continue
        links.append(link)
    return links

def main():
    url = sys.argv[1]
    if len(sys.argv) > 2:
        extract_self_links = sys.argv[2].lower() in ["self", "true", "yes"]
    else:
        extract_self_links = False
    for link in extract_links(url, extract_self_links):
        print(link)

if __name__ == "__main__":
    main()
