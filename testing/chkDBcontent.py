import requests  
from bs4 import BeautifulSoup
import os
import sqlite3 
import unittest

conn = sqlite3.connect('deletethis.db')
class Test(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect('deletethis.db')
    
    def test_empty_stories(self):
        cur = conn.cursor()
        stories = []
        empty_stories = cur.execute("SELECT StoryID FROM Review WHERE Story IS NULL;")
        for empty_row in empty_stories:
            stories.append(empty_row)
        cur.close()
        if stories:
            print("Stories which are empty: ", stories)

    def test_image_stories(self):
        cur = conn.cursor()
        storiesIMG = []
        img_stories = cur.execute("SELECT StoryID FROM Review WHERE Story LIKE '%@image*%';")
        for imgrow in img_stories:
            storiesIMG.append(imgrow)
        cur.close()
        if img_stories:
            print("Stories which are images: ", storiesIMG)

    def test_title(self):
        cur = conn.cursor()
        testTitle = []
        notEmpty_title = cur.execute("SELECT StoryID FROM Review WHERE Title IS NULL;")
        for TITLErow in notEmpty_title:
            testTitle.append(TITLErow)
        cur.close()
        if testTitle:
            print("Titles which are empty: ", testTitle)

    def test_username(self):
        cur = conn.cursor()
        testUsername = []
        test_name = cur.execute("SELECT StoryID FROM Review WHERE Username NOT LIKE '%Posted By%' AND Username IS NULL;")
        for uname in test_name:
            testUsername.append(uname)
        cur.close()
        if testUsername:
            print("Wrong username format: ", testUsername)
    
    def test_storytime(self):
        cur = conn.cursor()
        testStime = []
        storyTImetest = cur.execute("SELECT StoryID FROM Review WHERE StoryTime NOT LIKE '%[a-Z]%' OR StoryTime IS NULL;")
        for sTIme in storyTImetest:
            testStime.append(sTIme)
        cur.close()
        if testStime:
            print("Wrong time format: ", testStime)

    def test_tag(self):
        cur = conn.cursor()
        testtag = []
        testAllTag = cur.execute("SELECT StoryID FROM Review WHERE goodTag OR similarTag OR improvedTag or feelTag LIKE '%[0-9]%';")
        for eachtag in testAllTag:
            test_goodtag.append(eachGtag)
        cur.close()
        if testtag:
            print("Tags contains number: ", testtag)

    def test_resTIme(self):
        cur = conn.cursor()
        testresTime = []
        tResTime= cur.execute("SELECT ResponseID FROM Response WHERE ResponseTime NOT LIKE '%Submitted on%' AND ResponseTime IS NULL;")
        for eachResTime in tResTime:
            testresTime.append(eachResTime)
        cur.close()
        if testresTime:
            print("Wrong ResponseTime: ", testresTime)
    
    def test_updateTIme(self):
        cur = conn.cursor()
        testupdateTime = []
        tUpdateTime= cur.execute("SELECT UpdateID FROM userUpdataes WHERE updateTime NOT LIKE '%Submitted on%' AND updateTime IS NULL;")
        for eachUpTime in tUpdateTime:
            testupdateTime.append(eachUpTime)
        cur.close()
        if testupdateTime:
            print("Wrong ResponseTime: ", testupdateTime)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

