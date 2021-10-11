import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def IfEmptyFile(path):
    if os.path.getsize(path) == 0:
        return True
    else:
        return False

def CheckAbout(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_About" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_About" + ":File format incorrect")
            return False

def CheckActivity(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Activity" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\d", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_Activity" + ":File format incorrect")
            return False

# def CheckDate(path, empty_counter, format_counter):
#     if IfEmptyFile(path) == True:
#         empty_counter += 1
#         #print(empty_counter)
#     else:
#         file = open(path, 'r')
#         lines = file.read()
#         print(lines)
#         format = re.search("^[0-2021][-]([0-1][0-2])[-]([0-3][0-1])[,]([0-2][0-3])[:]([0-5][0-9])[:]([0-5][0-9])$", lines)
#         if format:
#             print("True")
#             return True
#         else:
#             format_counter += 1
#             print(format_counter)

def CheckFeelTags(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + ":Feel tags file empty")
        return None
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            print(str(id) + "_Feel_Tag" + ":File format incorrect")
            return False

def CheckGoodTags(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + ":Good tags file empty")
        return None
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            print(str(id) + "_Good_Tag" + ":File format incorrect")
            return False

def CheckImprovedTags(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + ":Improved Tags file empty")
        return None
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            print(str(id) + "_Improved_Tag" + ":File format incorrect")
            return False

def CheckSimilar(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + ":Similar file empty")
        return None
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            print(str(id) + "_Similar" + ":File format incorrect")
            return False
    
def CheckProgress(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Progress" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("^(This story has)(.*)$", lines)
        if format:
            #print(True)
            return True
        else: 
            print(str(id) + "_Progress" + ":File format incorrect")
            return False
           

def CheckStory(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Story" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_Story" + ":File format incorrect")
            return False

def CheckTitle(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Title" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_Title" + ":File format incorrect")

    #if file not empty
    #contains string and not numbers

def CheckUsername(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Username" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("^(Posted By)(.*)$", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_Username" + ":File format incorrect")

def CheckResponse(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Response" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_Response" + ":File format incorrect")

def CheckResponseHeader(path, id):
    if IfEmptyFile(path) == True:
        print(str(id) + "_ResponseHeader" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_ResponseHeader" + ":File format incorrect")

# def CheckResponseTime(path, format_counter):
#     if len(os.listdir(path + '/Responses')) == 0:
#         pass
#     else:
#         file = open(path, 'r')
#         lines = file.read()
#         format = re.search("^Submitted on [0-31][/][0-12][/][0-2021] at [0-23][:][0-59]$", lines)
#         if format:
#             print(True)
#             return True
#         else:
#             format_counter += 1
#             print(format_counter)
#     #if file not empty if meant to have response
#     #if file has right format 'Submitted on XXXXXX at XX:XX'

def CheckUpdate(path, format_counter):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Update" + ":File empty when shouldn't be")
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\w", lines)

        if format:
            #print(True)
            return True
        else:
            print(str(id) + "_Update" + ":File format incorrect")

def checkresponses_url(path,id,story_folder):
    if IfEmptyFile(path) == True:
        print(str(id) + "_Update" + ":File empty when shouldn't be")
    else:
        for files in path[0:1]: #take the first file in the response folder
            if files.is_dir():
                file = str(files)
                url_num = file.split('_')[1] #getting the url for response
    
        url = "https://www.careopinion.org.au/"+str(url_num) #going through each responses url
        response_url = BeautifulSoup(urlopen(url),'html.parser')
        response_title=''
        response = response_url.find("title")
        for i in response:
            response_title+=i
            response_title=response_title.replace(" | Care Opinion", "")

        f_id_title = story_folder + "/" + id + "_Title"
        file2 = open(f_id_title,'r') #getting title from story url
        lines = file2.read()
    
        if str(lines) == str(response_title):
            return True

        else:
            print("Url invalid")



# def CheckUpdateTime(path, format_counter):
    # if len(os.listdir(path + '/Updates')) == 0:
    #     pass
    # else:
    #     file = open(path, 'r')
    #     lines = file.read()
    #     format = re.search("^Submitted on [0-31][/][0-12][/][0-2021] at [0-23][:][0-59] and published on Care Opinion at [0-23][:][0-59]$", lines)
    #     if format:
    #         print(True)
    #         return True
    #     else:
    #         format_counter += 1
    #         print(format_counter)
    # #if file not empty if meant to have update
    # #if file right format 'Submitted on XXXXX at XX:XX and published ....'
        

def main():
    
    # id = 70000
    # f_id_about = "/Users/jakha/Documents/Professional Computing/webscrape_files/70000/70000_About"

    # CheckAbout(f_id_about, id)

    origin = "/Users/jakha/Documents/Professional Computing/webscrape_files/"

    for num in range(70000, 72000):

        id = str(num)
        story_folder = os.path.join(origin, id)

        if os.path.exists(story_folder):
            
            f_id_about = story_folder + "/" + id + "_About"
            f_id_activity = story_folder + "/" + id + "_Activity"
            # f_id_date = story_folder + "_Date"
            f_id_feel = story_folder + "/" + id + "_Feel_Tag"
            f_id_good = story_folder + "/" + id + "_Good_Tag"
            f_id_improved = story_folder + "/" + id + "_Improved_Tag"
            f_id_progress = story_folder + "/" + id + "_Progress"
            f_id_similar = story_folder + "/" + id + "_Similar"
            f_id_story = story_folder + "/" + id + "_Story"
            f_id_title = story_folder + "/" + id + "_Title"
            f_id_username = story_folder + "/" + id + "_Username"
            f_id_responses_folder = story_folder + "/Responses"

            CheckAbout(f_id_about, id)
            CheckActivity(f_id_activity, id)
            CheckProgress(f_id_progress, id)
            CheckStory(f_id_story, id)
            CheckTitle(f_id_title, id)
            CheckUsername(f_id_username, id)
            CheckFeelTags(f_id_feel, id)
            CheckGoodTags(f_id_good, id)
            CheckImprovedTags(f_id_improved, id)
            CheckSimilar(f_id_similar, id)
            checkresponses_url(f_id_responses_folder,id,story_folder)

            

            if len(os.listdir(story_folder + '/Responses')) == 0:
                print(str(id) + ":Doesn't have responses")
            else:
                print(str(id) + ": need to find response ID")

            f_id_updates_folder = story_folder + "/Updates"

            if len(os.listdir(story_folder + '/Updates')) == 0:
                print(str(id) + ":Doesn't have updates")
            else:
                print(str(id) + ":need to find update ID")
            

if __name__ == "__main__":
    main()


