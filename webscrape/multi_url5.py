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
            feelTag TEXT);''')

        conn.execute('''CREATE TABLE IF NOT EXISTS Response (
            ResponseID INT NOT NULL PRIMARY KEY,
            Response TEXT ,
            ResponseInfo TEXT,
            ResponseTime TEXT,
            storyID INT NOT NULL,
            FOREIGN KEY (storyID) REFERENCES Review (StoryID) );''')

        conn.execute('''CREATE TABLE IF NOT EXISTS userUpdates (
            UpdateID INT NOT NULL PRIMARY KEY,
            UpdateText TEXT ,
            updateTime TEXT,
            storyID INT NOT NULL,
            FOREIGN KEY (storyID) REFERENCES Review (StoryID) );''')
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
    sql = ''' INSERT INTO userUpdates(UpdateID,UpdateText,updateTime,storyID) VALUES(?,?,?,?)'''
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
    cur.execute("SELECT * FROM userUpdates WHERE storyID = {}".format(storyId))
    updateDetails = cur.fetchall()
    for update in updateDetails:
        print(update)    

def main():
    conn = sqlite3.connect('deletethis.db')
    create_db(conn)
    false_urls = 0
    # Start in the file where all the info will go
    origin = "/Users/maxdi/source/webscraper-inital/allRevs"
    # For the complete website scrape between 50,000 and 90,000
    for num in range(72919,72920):
        os.chdir(origin)
        id = str(num) + "_" 
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
        # insideLoop = False
        # #If the id is actually a response id then do not re-download
        # for ip in respID:
        #     #print(ip.attrs["data-po-response-id"])
        #     if str(ip.attrs["data-po-response-id"]) == str(num):
        #         false_urls +=1
        #         insideLoop = True
        #         continue
        # if insideLoop:
        #     insideLoop = False
        #     continue

        realID = fullHTML.find("article")
        if str(realID.attrs["data-po-opinionid"]) != str(num):
            false_urls +=1
            continue

        os.mkdir(str(num))
        os.chdir(str(num))
        # using class tag -> potentially usefull for tags, but not getting if it is "what was good?", "what was bad?", ect.
        # allTags = fullHTML.find_all("a", class_="inline-block font-c-1 tooltip")
        # for i in allTags:
        #     print(i.text)

        # tag parent divs

        # Getting the actual review
        revHTML = fullHTML.find(id="opinion_body")
        f = open(id+"Story", "ab")
        review = revHTML.text.replace("\n","")
        review = review.replace("\r","")
        f.write(review.encode())
        f.close

        # Getting time of review
        timediv = fullHTML.find("time")
        timePreSub = timediv.attrs["datetime"]
        time = open(id+"Date", "ab")
        timeSub = str(timePreSub).replace("T",",")
        time.write(timeSub.encode())
        time.close()

        # get all good,bad,feeling tags
        parentDivs = fullHTML.find_all("div", class_="mb-4")
        for i in parentDivs:
            checker = str(i.h3)
            tags = i.find_all("a", class_="inline-block font-c-1 tooltip")    

            if "What was good?"  in checker:
                for tag in tags:
                    goodStr += tag.text
                    goodStr += ", "

            
            if "What could be improved?" in checker:
                for tag in tags:
                    # improved.append(tag.text)
                    improvedStr += tag.text
                    improvedStr += ", "

            if "How did you feel?" in checker:
                for tag in tags:
                    # feel.append(tag.text)
                    feelStr += tag.text
                    feelStr += ", "

        g = open(id+"Good_Tag", "ab")
        b = open(id+"Improved_Tag", "ab")
        feel = open(id+"Feel_Tag", "ab")
        goodCp = goodStr
        improveCp = improvedStr
        feelCp = feelStr
        # for line in goodStr:
        #     if line != '':
        #         goodCp += line 
        
        goodCp = goodStr.replace("  ","")
        goodCp = goodCp.replace("\r","")
        goodCp = goodCp.replace("\n","")
        goodCp = goodCp[:-2]

        improveCp = improvedStr.replace("  ","")
        improveCp = improveCp.replace("\r","")
        improveCp = improveCp.replace("\n","")
        improveCp = improveCp[:-2]

        feelCp = feelStr.replace("  ","")
        feelCp = feelCp.replace("\r","")
        feelCp = feelCp.replace("\n","")
        feelCp = feelCp[:-2]

        # for i in range(len(goodCp)):
        #     if goodCp[i] == " ":
        #         if goodCp[i+1] == " ":
        #             goodCp[i+1] = ""
        g.write(goodCp.encode())
        b.write(improveCp.encode())
        feel.write(feelCp.encode())
        g.close()
        b.close()
        feel.close()
        # Getting similar tags
        moreAbout = fullHTML.find_all("div", class_="other-tags")
        for i in moreAbout:
            tags = i.find_all("a", class_="inline-block font-c-1 tooltip")
            for tag in tags:
                similarStr += tag.text
                similarStr += ", "
        similarCp = similarStr
        similarCp = similarStr.replace("  ","")
        similarCp = similarCp.replace("\r","")
        similarCp = similarCp.replace("\n","")
        similarCp = similarCp[:-2]

        similar = open(id+"Similar","ab")
        similar.write(similarCp.encode())
        similar.close()
        
        # Getting username
        userNameAll =  fullHTML.find("div", class_="sticky-title inline-block")
        userDiv = userNameAll.find("div")
        username = open(id+"Username","ab")
        userN = userDiv.text.replace("\r","")
        userN = userN.replace("\n","")
        userN = userN.replace("  ","")
        username.write(userN.encode())
        username.close()        
  
        #Get number of reads
        currentList =  fullHTML.find("li", id="subscribers_read_count")
        try:
            currentReadNum = currentList.strong
        except AttributeError:
            pass
        readNum = ""
        currentreadNum = open(id+"Activity","ab")
        for i in currentReadNum:
            try:
                currentreadNum.write(i.encode())
                readNum += i
            except:
                pass
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
            i = loc.find("span", itemprop="name")
            locationStr += i.text
            locationStr += ", "
        locationCp = locationStr[:-2]
        locations = open(id+"About", "ab")
        locations.write(locationCp.encode())
        locations.close()
        
        titleTxt = ""
        # Get the title 
        titleTag = fullHTML.find("title")
        title = open(id+ "Title","ab")
        for i in titleTag:
            titleTxt += i
        titleT = titleTxt.replace("| Care Opinion", "")
        title.write(titleT.encode())
        title.close()
        prog = ""
        #Get the progress
        whereReviewUpToTag = fullHTML.find("aside", class_="author-subscriber")
        progressOfRev = whereReviewUpToTag.find("h2")
        progress = open(id+"Progress","ab")
        for i in progressOfRev:
            # print(i)
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
        for ide in respID:
            responseString = ""
            responseHeaderStr = ""
            resp = fullHTML.find("div", id=ide.attrs["data-po-response-id"])
            responseHTML = resp.find_all("blockquote", class_="froala-view")
            dateSumbmitted = resp.find("span", class_="response-submission-footer-content")           
            responseHeader = resp.find("div", class_= "inner-expansion-profile")

            try:
                responseHeaderStr = responseHeader.text
            except:
                pass
            resHeader = open(str(num) + "_" + ide.attrs["data-po-response-id"] +  "_" + "Response_Header", "ab")
            responseCp = responseHeaderStr
            responseCp = responseHeaderStr.replace("  ","")
            responseCp = responseCp.replace("\r",",")
            responseCp = responseCp.replace("\n",",")
            responseCp = responseCp.replace(",,,,",",")
            responseCp = responseCp.replace(",,,",",")
            responseCp = responseCp.replace(",,",",")
            responseCp = responseCp.replace(", ,",",")
            responseCp = responseCp[:-1]
            responseCp = responseCp[1:]
            responseCp = responseCp.replace(", ",",")
            responseCp = responseCp.replace(",",", ")
            resHeader.write(responseCp.encode())
            resHeader.close()

            for i in responseHTML:
                resp = open(str(num) + "_"+ide.attrs["data-po-response-id"]+ "_"+ "Response","ab")
                respTime = open(str(num) + "_"+ide.attrs["data-po-response-id"]+ "_" + "Response_Time","ab")
                respTime.write(dateSumbmitted.text.encode())
                responseString += i.text
            responseStr = responseString.replace("\r","")
            responseStr = responseStr.replace("\n","")
            resp.write(responseStr.encode())
            resp.close()
            res = (int(ide.attrs["data-po-response-id"]),responseStr,responseCp,dateSumbmitted.text,str(num))
            create_response(conn, res)
                    
        #Make updates folder; TODO where are update 
        os.chdir("..")
        os.mkdir("Updates")
        os.chdir("Updates")
        try:
            updateDiv = fullHTML.find_all("div", class_="author_response comment public")
            for i in updateDiv:
                updID = i.attrs["id"]
                blockTextSearch = i.find("blockquote")
                updateDiv = open(str(num) + "_"+updID+ "_" + "Update", "ab")
                blockText = blockTextSearch.text.replace("\r","")
                blockText = blockText.replace("\n","")
                updateDiv.write(blockText.encode())
                updateDiv.close()

                updateTime = i.find("a", class_="share-link")
                fullTime = updateTime.attrs["title"]
                upTime = open(str(num) + "_" +updID+ "_" + "Update_date","ab")
                upTime.write(str(fullTime).encode())
                upTime.close()
                update = (updID,blockText,fullTime,str(num))
                create_update(conn,update)
        except:
            pass
        

        rev = (str(num),review,userN,titleT,locationCp,timeSub,readNum,prog,goodCp,similarCp,improveCp,feelCp)
        create_review(conn,rev)
        #SELECT id From Review WHERE goodTag LIKE '%word1%'
    print(false_urls)
    # select_all_tasks(conn)
    # select_all_tags(conn,"goodTag","nurse")



if __name__ == '__main__':
    main()
