import requests  
from bs4 import BeautifulSoup
import os
import sqlite3 
import unittest

conn = sqlite3.connect('deletethis.db')
class Test(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect('deletethis.db')
    
    def test_respID(self):
        cur = conn.cursor()
        storyID = []
        AllstoryID = cur.execute("SELECT DISTINCT StoryID FROM Review;")
        for eachStoryID in AllstoryID:
            story_id = str(eachStoryID[0])
            storyID.append(story_id)

        wrongID = []
        resID = cur.execute("SELECT DISTINCT StoryID FROM Response;")
        for eachresID in resID:
            resp_id = str(eachresID[0])
            if resp_id not in storyID:
                wrongID.append(resp_id)

        cur.close()
        if wrongID:
            print("List of storyIDs that exists in Response but not in Review: ", wrongID)
    
    def test_updateID(self):
        cur = conn.cursor()
        storyID = []
        AllstoryID = cur.execute("SELECT DISTINCT StoryID FROM Review;")
        for eachStoryID in AllstoryID:
            story_id = str(eachStoryID[0])
            storyID.append(story_id)

        wrongupdateID = []
        updateID = cur.execute("SELECT DISTINCT StoryID FROM userUpdates;")
        for eachupdateID in updateID:
            update_id = str(eachupdateID[0])
            if update_id not in storyID:
                wrongupdateID.append(update_id)

        cur.close()
        if wrongupdateID:
            print("List of storyIDs that exists in userUpdates but not in Review: ", wrongupdateID)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)


