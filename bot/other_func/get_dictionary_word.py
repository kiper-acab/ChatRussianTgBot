__all__ = ()

import json
import os
import random


def get_random_dictionary_word():
    with open(
        os.path.join("other_files", "sl_words.json"),
        "r",
        encoding="utf-8",
    ) as fcc_file:
        fcc_data = json.load(fcc_file)
        return random.choice(fcc_data)
