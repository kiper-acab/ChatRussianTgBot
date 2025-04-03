__all__ = ()

import json
import pathlib
import random


def get_random_accent_word():
    with pathlib.Path("other_files", "accents.json").open(
        "r",
        encoding="utf-8",
    ) as fcc_file:
        fcc_data = json.load(fcc_file)
        return random.choice(fcc_data)
