#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Extrait des informations sur les numéros de cartes fournis."""

__author__ = "Thomas Bagrel"
__maintainer__ = "Thomas Bagrel"
__copyright = "Copyright 2019, TRACIP SAS"
__credits__ = ["TRACIP R&D"]
__licence__ = "AGPLv3"
__version__ = "0.1.1"
__email__ = "tbagrel@tracip.fr"
__status__ = "Testing"

import re
import click
import sys

MODE_TO_STDFILE = {
    "r": sys.stdin,
    "w": sys.stdout
}

STD_PATH = "-"
ENC = "utf-8"
DEFAULT_OUTPUT_FORMAT = "{card_norm}\t{is_valid}\t{type_norm}"

UNKNOW_TYPE_NORM = "unknow"
UNKNOW_TYPE = "Unknow"

VALID = "yes"
INVALID = "no"

TYPE_DB = [
    (re.compile(r"^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$"), "mastercard", "MasterCard"),
    (re.compile(r"^4[0-9]{12}(?:[0-9]{3})?$"), "visa", "Visa"),
    (re.compile(r"^3[47][0-9]{13}$"), "american_express", "American Express"),
    (re.compile(r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$"), "dinners_club", "Dinners Club"),
    (re.compile(r"^6(?:011|5[0-9]{2})[0-9]{12}$"), "discover", "Discover"),
    (re.compile(r"^(?:2131|1800|35\d{3})\d{11}$"), "jcb", "JCB")
]

RE_ONLY_NUMERIC = re.compile(r"^[0-9]+$")

class open_dash:
    """Context manager permettant de gérer les cas où le chemin passé en
    paramètres désigne l'entrée/sortie standard ("-")"""

    def __init__(self, path, mode="r", encoding="utf-8", **kwargs):
        """Constructeur"""
        if mode not in MODE_TO_STDFILE:
            raise Exception(
                "Mode \"{}\" is not supported by this context manager."
                .format(mode))
        self.path = path
        self.mode = mode
        self.encoding = encoding,
        self.kwargs = kwargs
        self.std_used = self.path == STD_PATH

    def __enter__(self):
        """Exécuté lors de l'entrée dans le context manager."""
        if self.std_used:
            self.file = MODE_TO_STDFILE[self.mode]
        else:
            self.file = open(
                self.path, self.mode, self.encoding, **self.kwargs)
        return (self.file, self.std_used)

    def __exit__(self, type, value, traceback):
        """Exécuté lors de la sortie du context manager."""
        if self.std_used:
            self.file.close()

def process_dirty_card(card, output_format, output_file):
    """Traite la carte passée en paramètres, qui peut contenir des espaces,
    tirets, caractères de fin de ligne..."""
    card_norm = card.strip().replace("-", "").replace(" ", "")
    valid = True
    if RE_ONLY_NUMERIC.match(card_norm) is None:
        valid = False
    if valid:
        sum_ = 0
        for (i, raw_num) in enumerate(reversed(card_norm)):
            value = (1 + i % 2) * int(raw_num)
            if value > 9:
                value -= 9
            sum_ += value
        valid = sum_ % 10 == 0
    if not valid:
        output_file.write(output_format.format(
            card=card,
            card_norm=card_norm,
            is_valid=INVALID,
            type_norm=UNKNOW_TYPE_NORM,
            type=UNKNOW_TYPE
        ) + "\n")
    else:
        process_valid_card(card, card_norm, output_format, output_file)

def process_valid_card(card, card_norm, output_format, output_file):
    """Traite la carte passée en paramètres, qui doit être uniquement
    constituée de chiffres et valide."""
    (type_norm, type_) = (UNKNOW_TYPE_NORM, UNKNOW_TYPE)
    for (re_c, t_norm, t) in TYPE_DB:
        if re_c.search(card_norm) is not None:
            (type_norm, type_) = (t_norm, t)
            break
    output_file.write(output_format.format(
        card_norm=card_norm,
        card=card,
        is_valid=VALID,
        type_norm=type_norm,
        type=type_
    ) + "\n")

@click.command()
@click.option(
    "-i", "--input-path",
    type=click.Path(
        exists=True, file_okay=True, dir_okay=False, allow_dash=True
    ),
    default=STD_PATH,
    help=(
        "Chemin vers le fichier d'entrée contenant les numéros de cartes à "
        "traiter (un par ligne)"
    )
)
@click.option(
    "-o", "--output-path",
    type=click.Path(
        exists=False, file_okay=True, dir_okay=False, allow_dash=True
    ),
    default=STD_PATH,
    help=(
        "Chemin vers le fichier de sortie qui contiendra les informations sur "
        "les numéros de cartes traités"
    )
)
@click.option(
    "-f", "--output-format",
    type=str,
    help=(
        "Format des lignes dans le fichier de sortie. Doit être une chaîne de "
        "format valide en Python, et peut contenir les variables suivantes :\n"
        "    - {card_norm} : le numéro de carte traité, normalisé\n"
        "    - {card} : le numéro de carte traité (non normalisé)\n"
        "    - {is_valid} : [yes/no] indiquant si la carte est valide ou non\n"
        "    - {type_norm} : le type de carte, normalisé\n"
        "    - {type} : le type de carte (non normalisé)\n"
        "Un caractère '\\n' est ajouté automatiquement à la fin de la chaîne "
        "de format. Il n'y a donc pas besoin de l'ajouter manuellement"
    ),
    default=DEFAULT_OUTPUT_FORMAT
)
@click.option(
    "-h", "--output-header",
    type=str,
    help=(
        "Header à ajouter en tête du fichier de sortie"
    ),
    default=None
)
def main(input_path, output_path, output_format, output_header):
    """Extrait des informations sur les numéros de cartes fournis."""
    with open_dash(input_path, "r", encoding=ENC) as (input_file, stdin_used):
        with open_dash(output_path, "w", encoding=ENC) as \
                (output_file, stdout_used):
            if output_header is not None:
                output_file.write(output_header + "\n")
            for line in input_file:
                process_dirty_card(line, output_format, output_file)
            if not stdout_used:
                print("--- Done!")

if __name__ == "__main__":
    main()
