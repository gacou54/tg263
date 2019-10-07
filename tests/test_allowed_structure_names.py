# coding: utf-8
# author: Gabriel Couture
import unittest

from tg263.allowed_structure_names import is_structure_name_allowed


class TestAllowedStructureNames(unittest.TestCase):

    def setUp(self) -> None:
        self.an_allowed_structure_name = 'Prostate'
        self.a_not_allowed_structure_name = 'A_NOT_ALLOWED_STRUCTURE_NAME'

    def test_givenAnAllowedStructureName_whenAskingIfStructureNameAllowed_thenResultIsTrue(self) -> None:
        result = is_structure_name_allowed(self.an_allowed_structure_name)

        self.assertTrue(result)

    def test_givenANotAllowedStructureName_whenAskingIfStructureNameAllowed_thenResultIsFalse(self) -> None:
        result = is_structure_name_allowed(self.a_not_allowed_structure_name)

        self.assertFalse(result)
