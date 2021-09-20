import tkinter as tk
from tkinter import *
from tkinter import ttk
# from ttkthemes.themed_tk import ThemedTk
# from ttkthemes.themed_style import ThemedStyle
import sqlite3
import requests  
from bs4 import BeautifulSoup
import os

conn = sqlite3.connect('app.db')

def select_specific_info(conn,tagName,similarTag,outputType):
    searchTerm = ""
    similarTerm = ""
    if tagName == "Select Tag":
        return 
    if outputType == "Select Tag":
        return
    # print("tag type is {}".format(tagName))
    # print("similar tag is {}".format(similarTag))
    # print("output type is {}".format(outputType))
    if "good" in tagName:
        searchTerm += "goodTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "improve" in tagName:
        searchTerm += "improvedTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "simi" in tagName:
        searchTerm += "similarTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "loc" in tagName:
        searchTerm += "locationTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "feel" in tagName:
        searchTerm += "feelTag"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "user" in tagName:
        searchTerm += "Username"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "time" in tagName:
        searchTerm += "StoryTime"
        similarTerm += "LIKE '%"
        similarTerm += similarTag
        similarTerm += "%'"
    elif "id" in tagName:
        searchTerm += "StoryID="
        similarTerm += similarTag

    outputTag = "" 
    if "id" in outputType:
        outputTag = "StoryID"
    elif "stor" in outputType:
       outputTag = "story"
    elif "all" in outputType:
        outputTag = "*"
    elif "sim" in outputType:
        outputTag = "similarTag"
    elif "good" in outputType:
        outputTag = "goodTag"
    elif "loc" in outputType:
        outputTag = "locationTag"
    elif "feel" in outputType:
        outputTag = "feelTag"
    elif "activit" in outputType:
        outputTag = "Activity"
    elif "prog" in outputType:
        outputTag = "Progress"
    elif "titl" in outputType:
        outputTag = "Title"
    elif "abou" in outputType:
        outputTag = "About"

    #TODO does not recognise id because it is a number not string
    cur = conn.cursor()
    cur.execute("SELECT {} FROM Review WHERE {} {}".format(outputTag,searchTerm,similarTerm))
    print("SELECT {} FROM Review WHERE {}{}".format(outputTag,searchTerm,similarTerm))
    # cur.execute("SELECT story FROM Review WHERE id=61079".format(outputTag,searchTerm,similarTerm))
    allTag = cur.fetchall()
    return allTag

def search():
    if tag_text.get() == "Select Tag":
        return 
    if output_text.get() == "Select Tag":
        return 
    info = select_specific_info(conn,tag_text.get(),spec_text.get(),output_text.get())
    for i in info:
        search_results.insert(END,(str(i)).strip('()\/n,""xa0'))
    print(info)

def clear_search_res():
    search_results.delete(0,END)

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
    sql = ''' INSERT INTO userUpdates(UpdateID,UpdateText,updateUsername,storyID) VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, allUpdate)
    conn.commit()

def webscrape_url():
    url = web_url.get()
    origin = "/Users/maxdi/source/webscraper-inital/appRevs"
    if len(url) != 36:
        error="Invalid URL. Make sure it is of form https://www.careopinion.org.au/#####" 
        search_results.insert(END,error)
        return
    os.chdir(origin)
    try:
        page = requests.get(url)
        fullHTML = BeautifulSoup(page.content,"html.parser")
    except:
        error = "Invalid URL"
        search_results.insert(END,error)
        return
    id = "_" + url[-5:]
    num = int(url[-5:])
    goodStr = ""
    similarStr = ""
    improvedStr = ""
    feelStr = ""
    locationStr = ""

    print_error="" 
    errors = fullHTML.find_all("div", class_="messages")
    erStr = str(errors)
    if "We couldn't find the story" in erStr:
        print_error = "Invalid URL"

    if "story was withdrawn" in erStr:
        print_error = "Invalid URL"

    if print_error != "":
        search_results.insert(END,print_error)
        return

    realID = fullHTML.find("article")
    if str(realID.attrs["data-po-opinionid"]) != str(num):
        print_error = "This URL is not for a review. Try again with review url"
    
    respID = fullHTML.find_all("ul" , class_="response-supplemental clearfix")
    #If the id is actually a response id then do not re-download
    for ip in respID:
        if str(ip.attrs["data-po-response-id"]) == str(num):
            print_error = "This URL is for a response. Try again with review url"
            break

    upID = fullHTML.find_all("div" , class_="author_response comment public")
    for uID in upID:
        if str(uID.attrs["data-po-opinionid"]) == str(num):
            print_error = "This URL is for an update. Try again with review url"
            break
    
    if print_error != "":
        search_results.insert(END,print_error)
        return
    try:
        os.mkdir(str(num))
        os.chdir(str(num))
    except FileExistsError:
        #TODO make a popup and ask if he would like to re-download
        print_error="Review has already been downloaded"
        search_results.insert(END,print_error)
        return
    
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
            pass
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
                
    #Make updates folder
    os.chdir("..")
    os.mkdir("Updates")
    os.chdir("Updates")
    try:
        updateDiv = fullHTML.find_all("div", class_="author_response comment public")
        for i in updateDiv:
            updID = i.attrs["id"]
            blockText = i.find("blockquote")
            updateDiv = open("Update_"+updID, "ab")
            updateDiv.write(blockText.text.encode())
            updateDiv.close()

            updateTime = i.find("a", class_="share-link")
            fullTime = updateTime.attrs["title"]
            upTime = open("Update_date_"+updID,"ab")
            upTime.write(str(fullTime).encode())
            upTime.close()
    except:
        nc=1
    #update = (updateID,updateText,updateUsername,str(num))
    #create_update(conn,update)
    rev = (str(num),review.text,userDiv.text,titleTxt,locationStr,timeSub,readNum,prog,goodStr,similarStr,improvedStr,feelStr)
    try:
        create_review(conn,rev)
    except:
        error_string = "This review has already been scraped"
        search_results.insert(END,error_string)
    successString = "Review {} has been added!".format(str(num))
    search_results.insert(END,successString)


def main():
    global spec_text
    global output_text
    global tag_text
    global search_results
    global web_url
    win = tk.Tk()

    DataTypes = [
        "Select Tag",
        "id",
        "story",
        "good Tag" ,
        "similar Tag",
        "improved Tag",
        "response Tag",
        "feel Tag",
        "location Tag"
        "about",
        "title"
    ]
    
    setStyle = "arc"
    setColour = "#00cece"
    
    style = ttk.Style()
    #style.configure("TLabel", background= setColour)
    style.configure("TButton", background= setColour)
    style.configure("OptionMenu", background= setColour)
    
    #Part title
    part_label = tk.Label
    win.title("DB search")
    win.geometry('700x700')
    win.resizable(False,False)
    win.backGroundImage = PhotoImage(file="background.png")
    win.backGroundImageLabel=Label(win, image=win.backGroundImage)
    win.backGroundImageLabel.place(x=0,y=0)
    # title_label = tk.Label(win,text = "Welcome! Use this to search for reviews in the databse:", font=('bold',10),pady=20,padx=100)
    # title_label.grid()

    win.canvas = Canvas(win,width=550,height=600)
    win.canvas.place(x=65,y=30)

    #tag label e.g improve,bad,location ect
    tag_text = tk.StringVar()
    tag_text.set(DataTypes[3])
    tag_label = ttk.Label(win,text = "Enter Search Tag:", font=('courier',12))
    tag_label.place(x=180, y=60)
    input_tag = ttk.OptionMenu(win,tag_text,*DataTypes)
    input_tag.place(x=385,y=60)

    #specific search e.g nurse, food, doctors
   
    spec_text = tk.StringVar()
    spec_label = ttk.Label(win,text = "Enter Specific Tag:", font=('courier',12))
    spec_label.place(x=180,y=100)
    input_spec = ttk.Entry(win,textvariable=spec_text)
    input_spec.place(x=380,y=100)

    #which output they would like id,rev
    output_text = tk.StringVar()
    output_text.set(DataTypes[0])
    output_label = ttk.Label(win,text = "Enter Output type:", font=('courier',12))
    output_label.place(x=180, y=140)
    input_output = ttk.OptionMenu(win,output_text,*DataTypes)
    input_output.place(x=385,y=140)

    #Webscrape new file 
    web_url = tk.StringVar()
    web_label = ttk.Label(win,text = "Enter URL:", font=('courier',12))
    web_label.place(x=180,y=180)
    input_web = ttk.Entry(win,textvariable=web_url)
    input_web.place(x=380,y=180)

    # Listbox that will show reviewed
    search_results = Listbox(win, height=20, width=80, border=0,justify=LEFT)
    #search_results.grid(row=10, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
    search_results.place(x=105, y=270)
    # Create scrollbar
    scrollbar = ttk.Scrollbar(win,orient='vertical')
    scrollbar.pack(side="right", fill="y")

    scrollbar2 = ttk.Scrollbar(win,orient='horizontal')
    scrollbar2.pack(side="bottom", fill="x")
    # Set scroll to listbox
    # search_results.configure(yscrollcommand=scrollbar.set)
    search_results.configure(xscrollcommand=scrollbar2.set)
    
    search_results.config(yscrollcommand = scrollbar.set, xscrollcommand = scrollbar2.set)

    # Set scroll to listbox
    scrollbar.config(command=search_results.yview)
    scrollbar2.config(command=search_results.xview)

    #buttons
    search_but = ttk.Button(win,text='Search', width=12,command=search)
    search_but.place(x=160,y=230)
    #webscrape button
    search_but = ttk.Button(win,text='Webscrape', width=12,command=webscrape_url)
    search_but.place(x=310,y=230)
    #clear
    clear_but = ttk.Button(win,text='Clear', width=12,command=clear_search_res)
    clear_but.place(x=460,y=230)
    # canvas1.create_window(200, 140, window=entry1)
    win.mainloop()
    #In cmd run pyinstaller graphics1.py to get an application

if __name__ == '__main__':
    main()
