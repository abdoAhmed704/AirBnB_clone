#!/usr/bin/python3
"""

"""
import os
import unittest
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """

    """

    def test_Not_NON(self):
        """
        check that every thing is Not non
        """
        one = BaseModel()

        self.assertIsNotNone(one.id)
        self.assertIsNotNone(one.created_at)
        self.assertIsNotNone(one.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        model = BaseModel()

        first_updated_at = model.updated_at

        save_updated_at = model.save()

        self.assertNotEqual(first_updated_at, save_updated_at)

    def test_to_dictionary(self):
        """test_to_dictionary"""
        obj = BaseModel()

        model_dict = obj.to_dict()

        self.assertIsInstance(model_dict, dict)


if __name__ == "__main__":
    unittest.main()
    
