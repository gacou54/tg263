# coding: utf-8
# author: Gabriel Couture
from typing import Pattern


class Structure:

    def __init__(
            self, regex: Pattern,
            primary_name: str,
            fmaid: str,
            target_type: str,
            major_category: str,
            minor_category: str,
            anatomic_group: str,
            description: str) -> None:
        self.regex = regex

        self.primary_name = primary_name
        self.fmaid = None if fmaid == 'nan' else int(fmaid)

        self.target_type = target_type
        self.major_category = major_category
        self.minor_category = minor_category
        self.anatomic_group = anatomic_group

        self.description = description
