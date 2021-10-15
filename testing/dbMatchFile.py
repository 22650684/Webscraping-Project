import os
import sqlite3 
from bs4 import BeautifulSoup

def scan_folder(parentfile, diff):
    for file_name in os.listdir(parentfile):
        if "_" in file_name:
            diff = eachfile(file_name, parentfile, diff)
            
        else:
            current_path = "".join((parentfile, "/", file_name))
            
            if os.path.isdir(current_path):
                scan_folder(current_path, diff)
    return diff

def eachfile(file_name,parentfile, diff):
    conn = sqlite3.connect('healthReviewsChangeDB.db')
    cur = conn.cursor()
    dbcol = ''
    dbTable = ''
    story_ID = file_name[:5]
    filename =file_name[6:]
    if "About" in filename:
        dbcol = 'About'
        dbTable = 'Review'
    elif "Activity" in filename:
        dbcol = 'Activity'
        dbTable = 'Review'
    elif filename == 'Date':
        dbcol = 'StoryTime'
        dbTable = 'Review'
    elif "Feel_Tag" in filename:
        dbcol = 'feelTag'
        dbTable = 'Review'
    elif "Good_Tag" in filename:
        dbcol = 'goodTag'
        dbTable = 'Review'
    elif "Improved_Tag" in filename:
        dbcol = 'improvedTag'
        dbTable = 'Review'
    elif "Progress" in filename:
        dbcol = 'Progress'
        dbTable = 'Review'
    elif "Similar" in filename:
        dbcol = 'similarTag'
        dbTable = 'Review'
    elif "Story" in filename:
        dbcol = 'Story'
        dbTable = 'Review'
    elif "Title" in filename:
        dbcol = 'Title'
        dbTable = 'Review'
    elif "Username" in filename:
        dbcol = 'Username'
        dbTable = 'Review'
    
    elif filename.endswith("Response"):
        dbcol = 'Response'
        story_ID = filename[:5]
        dbTable = 'Response'
    elif "Response_Header" in filename:
        dbcol = 'ResponseInfo'
        story_ID = filename[:5]
        dbTable = 'Response'
    elif "Response_Time" in filename:
        dbcol = 'ResponseTime'
        story_ID = filename[:5]
        dbTable = 'Response'

    elif filename.endswith("Update"):
        dbcol = 'UpdateText'
        story_ID = filename[:5]
        dbTable = 'userUpdates'
    elif "Update_date" in filename:
        dbcol = 'updateTime'
        story_ID = filename[:5]
        dbTable = 'userUpdates'

    exeStat =  "SELECT "+ dbcol+ " FROM "+dbTable+" WHERE StoryID IS "+ story_ID +";" 
            
    AllDBcontent = cur.execute(exeStat)
    for eachcontent in AllDBcontent:
        with open(parentfile+"/"+file_name, 'r') as reader:
            content = reader.read()
            if eachcontent[0] != content:
                diff.append(file_name)
    cur.close()
    return diff

def main():
    parentfile = "/mnt/c/Users/Juju/DB/project/webscrape/realScrape"
    diff = []
    scan_folder(parentfile, diff) 
    if diff:
        print("The file name that the content is different from the Database:", diff)
        print("Number of files: ", str(len(diff)))
    else:
        print("Test OK")


if __name__ == "__main__":
    main()
