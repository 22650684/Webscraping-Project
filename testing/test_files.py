import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def IfEmptyFile(path):
    if os.path.getsize(path) == 0:
        return True
    else:
        return False

def CheckAbout(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_About\n")
        #print(str(id) + "_About" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_About\n")
            #print(str(id) + "_About" + ":File format incorrect")
            return False

def CheckActivity(path, id, activity_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        activity_empty.write(str(id) + "\n")
        #print(str(id) + "_Activity" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\d", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Activity\n")
            #print(str(id) + "_Activity" + ":File format incorrect")
            return False

def CheckDate(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Date\n")
        #print(str(id) + "_Date" + ":File empty when shouldn't be")
        #print(empty_counter)
        return None
    else:
        file = open(path, 'a+')
        lines = file.read()
        #print(lines)
        format = re.search("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[,]([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", lines)
        if format:
            #print("True")
            return True
        else:
            incorrect_format.write(str(id) + "_Date\n")
            #print(str(id) + "_Date" + ":File format incorrect")
            return False

def CheckFeelTags(path, id, tags_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        tags_empty.write(str(id) + ":Feel tags file empty\n")
        #print(str(id) + ":Feel tags file empty")
        return None
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            incorrect_format.write(str(id) + "_Feel_Tags\n")
            #print(str(id) + "_Feel_Tag" + ":File format incorrect")
            return False

def CheckGoodTags(path, id, tags_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        tags_empty.write(str(id) + ":Good tags file empty\n")
        #print(str(id) + ":Good tags file empty")
        return None
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            incorrect_format.write(str(id) + "_Good_Tags\n")
            #print(str(id) + "_Good_Tag" + ":File format incorrect")
            return False

def CheckImprovedTags(path, id, tags_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        tags_empty.write(str(id) + ":Improved tags file empty\n")
        #print(str(id) + ":Improved Tags file empty")
        return None
    else:
        file = open(path, 'r')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            incorrect_format.write(str(id) + "_Improved_Tags\n")
            #print(str(id) + "_Improved_Tag" + ":File format incorrect")
            return False

def CheckSimilar(path, id, tags_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        tags_empty.write(str(id) + ":Similar tags file empty\n")
        #print(str(id) + ":Similar file empty")
        return None
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\D", lines)
        if format:
            return True
        else:
            incorrect_format.write(str(id) + "_Similar_Tags\n")
            #print(str(id) + "_Similar" + ":File format incorrect")
            return False
    
def CheckProgress(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Progress\n")
        #print(str(id) + "_Progress" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("^(This story)(.*)$", lines)
        if format:
            #print(True)
            return True
        else: 
            incorrect_format.write(str(id) + "_Progress\n")
            #print(str(id) + "_Progress" + ":File format incorrect")
            return False
           

def CheckStory(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write((str(id) + "_Story\n"))
        #print(str(id) + "_Story" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Story\n")
            #print(str(id) + "_Story" + ":File format incorrect")
            return False

def CheckTitle(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Title\n")
        #print(str(id) + "_Title" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Title\n")
            #print(str(id) + "_Title" + ":File format incorrect")
            return False

    #if file not empty
    #contains string and not numbers

def CheckUsername(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Username\n")
        #print(str(id) + "_Username" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("^(Posted By)(.*)$", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Username\n")
            #print(str(id) + "_Username" + ":File format incorrect")
            return False

def CheckResponse(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Response\n")
        #print(str(id) + "_Response" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Response\n")
            #print(str(id) + "_Response" + ":File format incorrect")
            return False

def CheckResponseHeader(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Response_Header\n")
        #print(str(id) + "_ResponseHeader" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\w", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Response_Header\n")
            #print(str(id) + "_ResponseHeader" + ":File format incorrect")
            return False

def CheckResponseDate(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Response_Date\n")
        #print(str(id) + "_ResponseTime" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        #print(lines)
        format = re.search("^Submitted on (0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d at ([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", lines)
        if format:
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Response_Date")
            #print(str(id) + "_ResponseTime" + ":File format incorrect")
            return False

def CheckUpdate(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Update\n")
        #print(str(id) + "_Update" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        format = re.search("\w", lines)
        #print(lines)
        if format:
            #print(id + "Update True")
            #print(True)
            return True
        else:
            incorrect_format.write(str(id) + "_Update\n")
            #print(str(id) + "_Update" + ":File format incorrect")
            return False

def CheckUpdateDate(path, id, file_empty, incorrect_format):
    if IfEmptyFile(path) == True:
        file_empty.write(str(id) + "_Update_Date\n")
        #print(str(id) + "_UpdateDate" + ":File empty when shouldn't be")
    else:
        file = open(path, 'a+')
        lines = file.read()
        #print(lines)
        format = re.search("^Submitted on ((0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d) at ([0-1]?[0-9]|2[0-3]):[0-5][0-9] and published on Care Opinion (.*)$", lines)
        if format:
            #print(id + ":Update Date True")
            return True
        else:
            incorrect_format.write(str(id) + "_Update_Date\n")
            #print(str(id) + "_UpdateDate" + ":File format incorrect")
            return False

# def checkresponses_url(path,id,story_folder):
#     if IfEmptyFile(path) == True:
#         print(str(id) + "_Update" + ":File empty when shouldn't be")
#     else:
#         for files in path[0:1]: #take the first file in the response folder
#             if files.is_dir():
#                 file = str(files)
#                 url_num = file.split('_')[1] #getting the url for response
    
#         url = "https://www.careopinion.org.au/"+str(url_num) #going through each responses url
#         response_url = BeautifulSoup(urlopen(url),'html.parser')
#         response_title=''
#         response = response_url.find("title")
#         for i in response:
#             response_title+=i
#             response_title=response_title.replace(" | Care Opinion", "")

#         f_id_title = story_folder + "/" + id + "_Title"
#         file2 = open(f_id_title,'r') #getting title from story url
#         lines = file2.read()
    
#         if str(lines) == str(response_title):
#             return True

#         else:
#             print("Url invalid")
def check_response_update_url(id,title_path, resp_or_up, save_errors,story_id):
    #finding url title
    url = "https://www.careopinion.org.au/"+str(id) #going through each responses url
    page = requests.get(url)
        # Simulating starting from 81,000 so need to add "810"
        
    fullHTML = BeautifulSoup(page.content,"html.parser")
    titleTag = fullHTML.find("title")
    titleTxt = ""
    for i in titleTag:
        titleTxt += i
    title_url = titleTxt.replace("| Care Opinion", "")

    #Finding .txt title
    title_file=open(title_path,'r')
    title_txt = title_file.read()
    if title_url != title_txt:
        # print(title_txt)
        # print(title_url)
        print(str(story_id))
        save_errors.write(str(story_id)+"_"+str(id) + resp_or_up+ "\n")



def main():
    
    # id = 70000
    # f_id_about = "/Users/jakha/Documents/Professional Computing/webscrape_files/70000/70000_About"

    # CheckAbout(f_id_about, id)
    count = 0

    origin = "/Users/maxdi/source/webscraper-inital/oldRevs"
    url_count = "/Users/maxdi/source/webscraper-inital"

    file_empty = open(url_count + "_Empty_Files_URLs", "a+")
    file_empty.write("File empty when shouldn't be: \n")

    activity_empty = open(url_count + "_Activity_Empty_URLs", "a+")
    activity_empty.write("Empty Activity URLs: \n")

    tags_empty = open(url_count + "_Empty_Tags_URLs", "a+")
    tags_empty.write("Empty Tags URLs: \n")

    incorrect_format = open(url_count + "_Incorrect_Format_URLs", "a+")
    incorrect_format.write("URLs with incorrect format: \n")

    no_responses = open(url_count + "_No_Responses_URLs", "a+")
    no_responses.write("URLs with no responses: \n")

    no_updates = open(url_count + "_No_Updates_URLs", "a+")
    no_updates.write("URLs with no updates: \n")

    urls_dont_match = open(url_count + "_urls_dont_weird", "a+")
    urls_dont_match.write("URLs that don't match: \n")

    
    
    for num in range(60840, 60890):

        id = str(num)
        story_folder = origin+ "/" +str(num)
        # story_folder = os.path.join(origin, id)
        # os.chdir(origin)
        # count += 1
        if os.path.exists(story_folder):
        # try:
            # os.chdir(story_folder)
            f_id_about = story_folder + "/" + id + "_About"
            f_id_activity = story_folder + "/" + id + "_Activity"
            f_id_date = story_folder + "/" + id + "_Date"
            f_id_feel = story_folder + "/" + id + "_Feel_Tag"
            f_id_good = story_folder + "/" + id + "_Good_Tag"
            f_id_improved = story_folder + "/" + id + "_Improved_Tag"
            f_id_progress = story_folder + "/" + id + "_Progress"
            f_id_similar = story_folder + "/" + id + "_Similar"
            f_id_story = story_folder + "/" + id + "_Story"
            f_id_title = story_folder + "/" + id + "_Title"
            f_id_username = story_folder + "/" + id + "_Username"

            CheckAbout(f_id_about, id, file_empty, incorrect_format)
            CheckActivity(f_id_activity, id, activity_empty, incorrect_format)
            CheckDate(f_id_date, id, file_empty, incorrect_format)
            CheckProgress(f_id_progress, id, file_empty, incorrect_format)
            CheckStory(f_id_story, id, file_empty, incorrect_format)
            CheckTitle(f_id_title, id, file_empty, incorrect_format)
            CheckUsername(f_id_username, id, file_empty, incorrect_format)
            CheckFeelTags(f_id_feel, id, tags_empty, incorrect_format)
            CheckGoodTags(f_id_good, id, tags_empty, incorrect_format)
            CheckImprovedTags(f_id_improved, id, tags_empty, incorrect_format)
            CheckSimilar(f_id_similar, id, tags_empty, incorrect_format)

            #store urls with no responses and updates in a file put on git
            #store urls with no tags file
            #urls with proper errors in same file

            f_id_responses_folder = story_folder + "/Responses"
            if len(os.listdir(f_id_responses_folder)) == 0:
                no_responses.write(str(id) + "\n")
                #print(str(id) + ":Doesn't have responses")
            else:
                for file in os.listdir(f_id_responses_folder):
                    if file.endswith("_Response"):
                        url_num = file.split('_')[1]
                        check_response_update_url(url_num,f_id_title, "_Response", urls_dont_match,id)
                        f_id_response = os.path.join(f_id_responses_folder, file)
                        #print(f_id_response)
                        CheckResponse(f_id_response, id, file_empty, incorrect_format)
                    elif file.endswith("_Response_Header"):
                        f_id_response_header = os.path.join(f_id_responses_folder, file)
                        #print(f_id_response_header)
                        CheckResponseHeader(f_id_response_header, id, file_empty, incorrect_format)
                    elif file.endswith("_Response_Time"):
                        f_id_response_date = os.path.join(f_id_responses_folder, file)
                        #print(f_id_response_date)
                        CheckResponseDate(f_id_response_date, id, file_empty, incorrect_format)

            f_id_updates_folder = story_folder + "/Updates"
            if len(os.listdir(story_folder + '/Updates')) == 0:
                no_updates.write(str(id) + "\n")
                #print(str(id) + ":Doesn't have updates")
            else:
                #print(str(id) + ":need to find update ID")
                for file in os.listdir(f_id_updates_folder):
                    if file.endswith("_Update"):
                        up_num = file.split('_')[1]
                        f_id_update = os.path.join(f_id_updates_folder, file)
                        check_response_update_url(up_num,f_id_title, "_Update", urls_dont_match,id)
                        CheckUpdate(f_id_update, id, file_empty, incorrect_format)
                    elif file.endswith("_Update_date"):
                        f_id_update_date = os.path.join(f_id_updates_folder, file)
                        CheckUpdateDate(f_id_update_date, id, file_empty, incorrect_format)
            count += 1
        # except:
        #     pass

            
            
    print(count)
    no_responses.close()
    no_updates.close()
    file_empty.close()
    tags_empty.close()
    activity_empty.close()
    incorrect_format.close()
    urls_dont_match.close()

if __name__ == "__main__":
    main()


