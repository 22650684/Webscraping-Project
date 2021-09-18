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
