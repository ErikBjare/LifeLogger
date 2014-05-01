__author__ = 'erb'

import unittest
import math

import pymongo
import pymongo.errors

from db import client, db
from db.model import Sheet
from db.datatypes import *


class DatabaseTestTemplate(unittest.TestCase):
    def setUp(self):
        self.db = client.lifelogger_test_notebook
        [self.db.drop_collection(collection) for collection in set(self.db.collection_names()) - {"system.indexes"}]

        self.users = self.db["users"]
        self.sheets = self.db["sheets"]

        self.test_user = self.users.find_one(
            self.users.insert({"username": "tester", "name": "Test McTest", "email": "tester@example.com"}))


class DatabaseTests(DatabaseTestTemplate):
    def setUp(self):
        DatabaseTestTemplate.setUp(self)

        self.erb = {"username": "erb", "name": "Erik Bjäreholt", "email": "erik.bjareholt@gmail.com"}
        self.tester = {"username": "tester", "name": "Test McTest", "email": "tester@example.com"}

    def test_collections(self):
        collections = db.collection_names()
        for collection in ["users", "sheets"]:
            self.assertTrue(collection in collections)

    def test_users(self):
        erb_id = self.users.insert(self.erb)
        tester_id = self.users.insert(self.tester)
        erb_found = self.users.find_one(erb_id)
        tester_found = self.users.find_one(tester_id)
        self.assertEqual(self.erb, erb_found)
        self.assertEqual(self.tester, tester_found)

    def test_duplicates(self):
        self.users.insert(self.erb)
        erb2 = self.erb.copy()
        erb2["email"] = "erb@example.com"
        erb3 = self.erb.copy()
        erb3["username"] = "erb2"
        self.assertRaises(pymongo.errors.DuplicateKeyError, self.users.insert, self.erb)
        self.assertRaises(pymongo.errors.DuplicateKeyError, self.users.insert, erb2)
        self.assertRaises(pymongo.errors.DuplicateKeyError, self.users.insert, erb3)


class SheetTests(DatabaseTestTemplate):
    def setUp(self):
        DatabaseTestTemplate.setUp(self)
        self.sheet = Sheet(self.test_user, db=self.db)

    def test_something(self):
        self.sheet.add_3_a_day("tiredness")
        self.assertEquals("tiredness", self.sheet.data["order"][-1][0])


class ModelTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_model(self):
        pass


class DatatypeTests(unittest.TestCase):
    def setUp(self):
        self.string_data = "asd"
        self.string = String(self.string_data)

        self.number_data = math.pi
        self.number = Number(self.number_data)

    def test_strings(self):
        self.assertEqual(self.string.data, "asd")
        self.assertEqual(str(self.string), "asd")

    def test_numbers(self):
        self.assertEqual(self.number.data, self.number_data)
        self.assertEqual(float(str(self.number)), self.number_data)