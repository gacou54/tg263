# coding: utf-8
# author: Gabriel Couture
import unittest

from tg263 import ALLOWED_STRUCTURES
from tg263.structures import is_structure_name_allowed, find_structure
from tg263.exceptions import StructureNameNotAllowedException


class TestAllowedStructureNames(unittest.TestCase):

    def setUp(self) -> None:
        with open('./tests/data/some_allowed_names.csv') as fh:
            self.some_allowed_structure_names = fh.readlines()

        self.a_not_allowed_structure_name = 'A_NOT_ALLOWED_STRUCTURE_NAME'

    def test_givenSomeAllowedStructureName_whenAskingIfStructureNameAllowed_thenResultIsAlwaysTrue(self) -> None:
        for a_structure_name in self.some_allowed_structure_names:
            result = is_structure_name_allowed(a_structure_name)

            self.assertTrue(result)

    def test_givenANotAllowedStructureName_whenAskingIfStructureNameAllowed_thenResultIsFalse(self) -> None:
        result = is_structure_name_allowed(self.a_not_allowed_structure_name)

        self.assertFalse(result)

    def test_givenAnAllowedStructureNameAndAnAllowedStructure_whenFindingStructure_thenResultIsExpectedStructure(self) -> None:
        an_allowed_structure_name = self.some_allowed_structure_names[0]
        expected_structure = ALLOWED_STRUCTURES[0]

        result = find_structure(an_allowed_structure_name)

        self.assertIs(result, expected_structure)

    def test_givenANotAllowedStructureName_whenFindingStructure_thenRaiseStructureNameNotAllowedException(self) -> None:
        self.assertRaises(
            StructureNameNotAllowedException,
            lambda: find_structure(self.a_not_allowed_structure_name)
        )
