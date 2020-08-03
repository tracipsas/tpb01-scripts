import sqlite3
import sys
import re

DOMAIN_RE = re.compile(r"^https?://([\w\.]+).*")

def extract_domain(url):
    match = DOMAIN_RE.search(url)
    if match is None:
        return None
    return match.group(1)

def main():
    url = sys.argv[1]
    domain = extract_domain(url)
    if domain is None:
        print("\"{}\" n'est pas une URL valide".format(url))
        sys.exit(1)
    connection = sqlite3.connect("domain.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT category FROM domain WHERE domain = ?",
        (domain, )
    )
    tags = []
    for row in cursor.fetchall():
        # chaque ligne résultat est un tuple, ici contenant un seul
        # élément : la catégorie du domaine
        tags.append(row[0])
    print("{} --> {}".format(url, ", ".join(tags)))
    connection.close()

if __name__ == "__main__":
    main()
