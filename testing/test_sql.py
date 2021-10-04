import requests  
from bs4 import BeautifulSoup
import os
import sqlite3 
import pandas as pd
import unittest

conn = sqlite3.connect('appDB.db')
class Test(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect('appDB.db')
    
    def test_different_stories(self):
        cur = conn.cursor()
        unique_stories = cur.execute("SELECT COUNT(DISTINCT Story) FROM Review")
        #In final we will assert = 10,500
        row_num = cur.execute("SELECT COUNT(1) FROM Review")
        cur.close()
        self.assertEqual(unique_stories, row_num)

    def test_different_time(self):
        cur = conn.cursor()
        unique_times = cur.execute("SELECT COUNT(DISTINCT StoryTime) FROM Review")
        #In final we will assert = 10,500
        row_num = cur.execute("SELECT COUNT(1) FROM Review")
        self.assertEqual(unique_times, row_num)
    
    def test_different_responses(self):
        cur = conn.cursor()
        unique_response = cur.execute("SELECT COUNT(DISTINCT Response) FROM Response")
        #In final we will assert = 10,500
        row_num = cur.execute("SELECT COUNT(1) FROM Response")
        self.assertEqual(unique_response, row_num)

    def test_different_reponse_time(self):
        cur = conn.cursor()
        unique_times = cur.execute("SELECT COUNT(DISTINCT ResponseTime) FROM Response")
        #In final we will assert = 10,500
        row_num = cur.execute("SELECT COUNT(1) FROM Response")
        self.assertEqual(unique_times, row_num)

    def test_different_update(self):
        cur = conn.cursor()
        unique_updates = cur.execute("SELECT COUNT(DISTINCT UpdateText) FROM userUpdates")
        #In final we will assert = 10,500
        row_num = cur.execute("SELECT COUNT(1) FROM userUpdates")
        self.assertEqual(unique_updates, row_num)

    def test_different_update_time(self):
        cur = conn.cursor()
        unique_times = cur.execute("SELECT COUNT(DISTINCT updateTime) FROM userUpdates")
        #In final we will assert = 10,500
        row_num = cur.execute("SELECT COUNT(1) FROM userUpdates")
        self.assertEqual(unique_times, row_num)

if __name__ == '__main__':
    unittest.main(verbosity=2)
