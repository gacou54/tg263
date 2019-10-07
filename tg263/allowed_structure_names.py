# coding: utf-8
# author: Gabriel Couture
import functools

from tg263.dictionary import ALLOWED_STRUCTURE_NAMES


def is_structure_name_is_allowed(structure_name: str) -> bool:
    return functools.reduce(
        lambda j, i: j or False if i.regex.match(structure_name) is None else True,
        ALLOWED_STRUCTURE_NAMES,
        False
    )
