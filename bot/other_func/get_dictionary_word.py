__all__ = ()

import json
import pathlib
import random


def get_random_dictionary_word():
    with pathlib.Path("other_files", "sl_words.json").open(
        "r",
        encoding="utf-8",
    ) as fcc_file:
        fcc_data = json.load(fcc_file)
        return random.choice(fcc_data)
