###
import requests  
from bs4 import BeautifulSoup
import os
import sqlite3 
import pandas as pd

def create_db(conn):
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS Review
            (StoryID INT NOT NULL PRIMARY KEY,
            Story TEXT ,
            Username TEXT ,
            Title TEXT,
            About TEXT,
            StoryTime STR,
            Activity TEXT,
            Progress TEXT,
            goodTag TEXT,
            similarTag TEXT,
            improvedTag TEXT,
            feelTag TEXT)''')

        conn.execute('''CREATE TABLE IF NOT EXISTS Response
            (ResponseID INT NOT NULL PRIMARY KEY,
            Response TEXT ,
            ResponseInfo TEXT,
            ResponseTime TEXT,
            storyID INT NOT NULL,
            FOREIGN KEY (storyID) REFERENCES Story (StoryID) )''')

        conn.execute('''CREATE TABLE IF NOT EXISTS Updates
            (UpdateID INT NOT NULL PRIMARY KEY,
            Update TEXT ,
            updateUsername Text,
            storyID INT NOT NULL,
            FOREIGN KEY (storyID) REFERENCES Story (StoryID) )''')
        conn.commit()
        print("Table created successfully")
    except:
        pass

def create_review(conn, review):
    sql = ''' INSERT INTO Review(StoryID,Story,Username,Title,About,StoryTime,Activity,Progress,goodTag,similarTag,improvedTag,feelTag) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, review)
    conn.commit()

def create_response(conn, allResponse):
    sql = ''' INSERT INTO Response(ResponseID,Response,ResponseInfo,ResponseTime,storyID) VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, allResponse)
    conn.commit()

def create_update(conn, allUpdate):
    sql = ''' INSERT INTO Updates(UpdateID,Update,updateUsername,storyID) VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, allUpdate)
    conn.commit()
    
def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Review")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_tags(conn,tagName,similarTag):
    cur = conn.cursor()
    cur.execute("SELECT id FROM Review WHERE {} LIKE '%{}%'".format(tagName,similarTag))
    allId = cur.fetchall()
    for i in allId:
        print(i)

def select_story_res(conn, storyId):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Response WHERE storyID = {}".format(storyId))
    resDetails = cur.fetchall()
    for eachRes in resDetails:
        print(eachRes)

def select_story_update(conn, storyId):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Updates WHERE storyID = {}".format(storyId))
    updateDetails = cur.fetchall()
    for update in updateDetails:
        print(update)    

def main():
    conn = sqlite3.connect('test5.db')
    create_db(conn)
    false_urls = 0
    # Start in the file where all the info will go
    origin = "/Users/maxdi/source/webscraper-inital/allRevs"
    # For the complete website scrape between 50,000 and 90,000
    for num in range(83100,83130):
        os.chdir(origin)
        id = "_" + str(num)
        goodStr = ""
        similarStr = ""
        improvedStr = ""
        feelStr = ""
        locationStr = ""
        URL = "https://www.careopinion.org.au/" + str(num)
        #URL = input("Enter Value:" )
        page = requests.get(URL)
        # Simulating starting from 81,000 so need to add "810"
        
        fullHTML = BeautifulSoup(page.content,"html.parser")


        errors = fullHTML.find_all("div", class_="messages")
        erStr = str(errors)
        if "We couldn't find the story" in erStr:
            false_urls +=1
            continue

        if "story was withdrawn" in erStr:
            false_urls +=1
            continue

        respID = fullHTML.find_all("ul" , class_="response-supplemental clearfix")
        insideLoop = False
        #If the id is actually a response id then do not re-download
        for ip in respID:
            #print(ip.attrs["data-po-response-id"])
            if str(ip.attrs["data-po-response-id"]) == str(num):
                false_urls +=1
                insideLoop = True
                continue
        if insideLoop:
            insideLoop = False
            continue

        os.mkdir(str(num))
        os.chdir(str(num))
        # using class tag -> potentially usefull for tags, but not getting if it is "what was good?", "what was bad?", ect.
        # allTags = fullHTML.find_all("a", class_="inline-block font-c-1 tooltip")
        # for i in allTags:
        #     print(i.text)

        # tag parent divs

        # Getting the actual review
        review = fullHTML.find(id="opinion_body")
        f = open("Story" + id, "ab")
        f.write(review.text.encode())
        f.close

        # Getting time of review
        timediv = fullHTML.find("time")
        timeSub = timediv.attrs["datetime"]
        time = open("Date"+id, "ab")
        time.write(str(timeSub).encode())
        time.close()

        # get all good,bad,feeling tags
        parentDivs = fullHTML.find_all("div", class_="mb-4")
        for i in parentDivs:
            checker = str(i.h3)
            tags = i.find_all("a", class_="inline-block font-c-1 tooltip")    

            if "What was good?"  in checker:
                for tag in tags:
                    # good.append(tag.text)
                    goodStr += tag.text

            
            if "What could be improved?" in checker:
                for tag in tags:
                    # improved.append(tag.text)
                    improvedStr += tag.text

            if "How did you feel?" in checker:
                for tag in tags:
                    # feel.append(tag.text)
                    feelStr += tag.text

        g = open("Good_Tag"+id, "ab")
        b = open("Improved_Tag"+id, "ab")
        feel = open("Feel_Tag"+id, "ab")

        g.write(goodStr.encode())
        b.write(improvedStr.encode())
        feel.write(feelStr.encode())
        g.close()
        b.close()
        feel.close()

        # Getting similar tags
        moreAbout = fullHTML.find_all("div", class_="other-tags")
        for i in moreAbout:
            tags = i.find_all("a", class_="inline-block font-c-1 tooltip")
            for tag in tags:
                # similar.append(tag.text)
                similarStr += tag.text
        similar = open("Similar"+id,"ab")
        similar.write(similarStr.encode())
        similar.close()
        
        # Getting username
        userNameAll =  fullHTML.find("div", class_="sticky-title inline-block")
        userDiv = userNameAll.find("div")
        username = open("Username"+id,"ab")
        username.write(userDiv.text.encode())
        username.close()
        
  
        #Get number of reads
        currentList =  fullHTML.find("li", id="subscribers_read_count")
        try:
            currentReadNum = currentList.strong
        except AttributeError:
            nc=1
        readNum = ""
        currentreadNum = open("Activity"+id,"ab")
        for i in currentReadNum:
            print(i)
            try:
                currentreadNum.write(i.encode())
                readNum += i
            except:
                n34=0
        currentreadNum.close()

        # Getting responses
        # responseHTML = fullHTML.find_all("blockquote", class_="froala-view")
        # for i in responseHTML:
        #     # print(i.text)
        #     # response = i.text
        #     responseStr += i.text

        # resp = open("response"+id,"ab")
        # resp.write(responseStr.encode())
        # resp.close()

        # Getting location
        location = fullHTML.find_all("span", itemtype="http://schema.org/Organization")
        for loc in location:
            locationStr += loc.text
        locations = open("About"+id, "ab")
        locations.write(locationStr.encode())
        locations.close()
        
        titleTxt = ""
        # Get the title 
        titleTag = fullHTML.find("title")
        title = open("Title"+id,"ab")
        for i in titleTag:
            titleTxt += i
            title.write(i.encode())
        title.close()
        prog = ""
        #Get the progress
        whereReviewUpToTag = fullHTML.find("aside", class_="author-subscriber")
        progressOfRev = whereReviewUpToTag.find("h2")
        progress = open("Progress"+id,"ab")
        for i in progressOfRev:
            print(i)
            progress.write(i.encode())
            prog += i
        progress.close()

        #Make the response folder and add response names
        os.mkdir("Responses")
        os.chdir("Responses")
        #Response Header

        #Response Date
        # responseDate = fullHTML.findAll("span", class_="response-submission-footer-content")
        # resDate = open("responseDate"+id, "ab")
        # responseDateStr = ""
        # for date in responseDate:
        #     responseDateStr += date.text
        # resDate.write(responseDateStr.encode())
        # resDate.close()
        for id in respID:
            responseStr = ""
            resp = fullHTML.find("div", id=id.attrs["data-po-response-id"])
            responseHTML = resp.find_all("blockquote", class_="froala-view")
            dateSumbmitted = resp.find("span", class_="response-submission-footer-content")
            
            responseHeader = resp.find("div", class_= "inner-expansion-profile")
            try:
                responseHeaderStr = responseHeader.text
            except:
                nc=1
            resHeader = open("Response_Header_"+id.attrs["data-po-response-id"], "ab")
            resHeader.write(responseHeaderStr.encode())
            resHeader.close()
            for i in responseHTML:
                resp = open("Response_"+id.attrs["data-po-response-id"],"ab")
                respTime = open("Response_Time"+id.attrs["data-po-response-id"],"ab")
                respTime.write(dateSumbmitted.text.encode())
                resp.write(i.text.encode())
                resp.close()
                responseStr += i.text
            res = (int(id.attrs["data-po-response-id"]),responseStr,responseHeaderStr,dateSumbmitted.text,str(num))
            create_response(conn, res)
                    
        #Make updates folder; TODO where are update 
        os.chdir("..")
        os.mkdir("Updates")
        os.chdir("Updates")
        #update = (updateID,updateText,updateUsername,str(num))
        #create_update(conn,update)

        rev = (str(num),review.text,userDiv.text,titleTxt,locationStr,timeSub,readNum,prog,goodStr,similarStr,improvedStr,feelStr)
        create_review(conn,rev)
        #SELECT id From Review WHERE goodTag LIKE '%word1%'
    print(false_urls)
    # select_all_tasks(conn)
    # select_all_tags(conn,"goodTag","nurse")



if __name__ == '__main__':
    main()
