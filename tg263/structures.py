# coding: utf-8
# author: Gabriel Couture
import functools

from tg263.structure import Structure
from tg263.dictionary import ALLOWED_STRUCTURES
from tg263.exceptions import StructureNameNotAllowedException


def is_structure_name_allowed(structure_name: str) -> bool:
    return functools.reduce(
        lambda j, i: j or False if i.regex.match(structure_name) is None else True,
        ALLOWED_STRUCTURES,
        False
    )


def find_structure(structure_name: str) -> Structure:
    for allowed_structure_name in ALLOWED_STRUCTURES:
        if allowed_structure_name.regex.match(structure_name) is not None:
            return allowed_structure_name

    raise StructureNameNotAllowedException
