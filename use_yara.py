import yara
import pprint

def my_callback(data):
    # data est le dictionnaire renvoyé par Yara pour chaque règle,
    # avec l'ensemble des matchs trouvés pour cette dernière
    # (stockés dans le champ "strings")
    pprint.pprint(data)
    if data["rule"] == "zipFile":
        filetype = "ZIP"
    else:
        filetype = "ELF"
    print("--> {} Fichiers {} reconnus : {}".format(
        len(data["strings"]),
        filetype,
        ", ".join((str(elt[0]) for elt in data["strings"]))
    ))
    print()

rules = yara.compile(filepath="rules.yara")
matches = rules.match(
    "example.tar",
    callback=my_callback,
    which_callbacks=yara.CALLBACK_MATCHES
)
