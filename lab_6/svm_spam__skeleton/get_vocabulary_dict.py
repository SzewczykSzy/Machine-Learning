#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    vocabulary_dict = {}

    with open("C:/Users/szyme/Documents/Studia/VI Semestr/ML/lab_6/svm_spam__skeleton/data/vocab.txt", encoding="utf-8") as file:
        for line in file:
            (key, value) = line.split()
            vocabulary_dict[int(key)] = value

    return vocabulary_dict
