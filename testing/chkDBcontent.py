import requests  
from bs4 import BeautifulSoup
import os
import sqlite3 
import unittest

conn = sqlite3.connect('healthReviewsDB.db')
class Test(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect('healthReviewsDB.db')
    
    def test_empty_stories(self):
        cur = conn.cursor()
        stories = []
        empty_stories = cur.execute("SELECT StoryID FROM Review WHERE Story IS NULL;")
        for empty_row in empty_stories:
            stories.append(empty_row[0])
        cur.close()
        if stories:
            msg = "(Review) StoryID of Stories which are empty: "+ str(stories)
            self.assertTrue(False, msg)

    def test_image_stories(self):
        cur = conn.cursor()
        storiesIMG = []
        img_stories = cur.execute("SELECT StoryID FROM Review WHERE Story LIKE '%@image*%';")
        for imgrow in img_stories:
            storiesIMG.append(imgrow[0])
        cur.close()
        if storiesIMG:
            msg = "(Review) StoryID of Stories which are images: "+ str(storiesIMG)
            self.assertTrue(False,msg)

    def test_title(self):
        cur = conn.cursor()
        testTitle = []
        notEmpty_title = cur.execute("SELECT StoryID FROM Review WHERE Title IS NULL;")
        for TITLErow in notEmpty_title:
            testTitle.append(TITLErow[0])
        cur.close()
        if testTitle:
            msg = "(Review) StoryID of Titles which are empty: "+ str(testTitle)
            self.assertTrue(False,msg)

    def test_username(self):
        cur = conn.cursor()
        testUsername = []
        test_name = cur.execute("SELECT StoryID FROM Review WHERE Username NOT LIKE '%Posted By%' AND Username IS NULL;")
        for uname in test_name:
            testUsername.append(uname[0])
        cur.close()
        if testUsername:
            msg = "(Review) StoryID of Wrong username format: "+ str(testUsername)
            self.assertTrue(False, msg)
    
    def test_storytime(self):
        cur = conn.cursor()
        testStime = []
        storyTImetest = cur.execute("SELECT StoryID FROM Review WHERE StoryTime LIKE '%[a-Z]%' OR StoryTime IS NULL;")
        for sTIme in storyTImetest:
            testStime.append(sTIme[0])
        cur.close()
        if testStime:
            msg = "(Review) StoryID of Wrong time format: " + str(testStime)
            self.assertTrue(False, msg)

    def test_activity(self):
        cur = conn.cursor()
        testActivity = []
        activitytest = cur.execute("SELECT StoryID FROM Review WHERE Activity NOT GLOB '*[0-9]*';")
        for eachActivity in activitytest:
            testActivity.append(eachActivity[0])
        cur.close()
        if testActivity:
            msg = "(Review) StoryID of Activity which is empty (supposingly equal to 0): " + str(testActivity)
            self.assertTrue(False, msg)

    def good_tag(self):
        cur = conn.cursor()
        goodtag = []
        testgoodTag = cur.execute("SELECT StoryID FROM Review WHERE goodTag NOT LIKE '%13 health%' AND goodTag LIKE '%[0-9]%';")
        for eachGtag in testgoodTag:
            goodtag.append(eachGtag[0])
        cur.close()
        if goodtag:
            msg = "(Review) StoryID of goodTags contains number: "+ str(goodtag)
            self.assertTrue(False, msg)

    def similar_tag(self):
        cur = conn.cursor()
        similartag = []
        testsimilarTag = cur.execute("SELECT StoryID FROM Review WHERE similarTag NOT LIKE '%13 health%' AND similarTag LIKE '%[0-9]%';")
        for eachStag in testsimilarTag:
            similartag.append(eachStag[0])
        cur.close()
        if similartag:
            msg = "(Review) StoryID of similarTags contains number: "+ str(similartag)
            self.assertTrue(False, msg)
    
    def feel_tag(self):
        cur = conn.cursor()
        feeltag = []
        testfeelTag = cur.execute("SELECT StoryID FROM Review WHERE feelTag NOT LIKE '%13 health%' AND feelTag LIKE '%[0-9]%';")
        for eachFtag in testfeelTag:
            feeltag.append(eachFtag[0])
        cur.close()
        if feeltag:
            msg = "(Review) StoryID of feelTags contains number: "+ str(feeltag)
            self.assertTrue(False, msg)
    
    def improved_tag(self):
        cur = conn.cursor()
        improvedtag = []
        testimprovedTag = cur.execute("SELECT StoryID FROM Review WHERE improvedTag NOT LIKE '%13 health%' AND improvedTag LIKE '%[0-9]%';")
        for eachItag in testimprovedTag:
           improvedtag.append(eachItag[0])
        cur.close()
        if improvedtag:
            msg = "(Review) StoryID of improvedTags contains number: "+ str(improvedtag)
            self.assertTrue(False, msg)

    def test_resTIme(self):
        cur = conn.cursor()
        testresTime = []
        tResTime= cur.execute("SELECT ResponseID FROM Response WHERE ResponseTime NOT LIKE '%Submitted on%' AND ResponseTime IS NULL;")
        for eachResTime in tResTime:
            testresTime.append(eachResTime[0])
        cur.close()
        if testresTime:
            msg = "(Response) ResponseID of Wrong ResponseTime: " + str(testresTime)
            self.assertTrue(False, msg)
    
    def test_updateTIme(self):
        cur = conn.cursor()
        testupdateTime = []
        tUpdateTime= cur.execute("SELECT UpdateID FROM userUpdates WHERE updateTime NOT LIKE '%Submitted on%' AND updateTime IS NULL;")
        for eachUpTime in tUpdateTime:
            testupdateTime.append(eachUpTime[0])
        cur.close()
        if testupdateTime:
            msg = "(userUpdates) UpdateID of Wrong updateTime: " + str(testupdateTime)
            self.assertTrue(False, msg)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

