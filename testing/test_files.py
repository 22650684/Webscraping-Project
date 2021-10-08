import os
import re

def IfEmptyFile(file):
    if os.path.getsize(file) == 0:
        return True
    else:
        return False

def CheckAbout(file, counter, id):
    if IfEmptyFile(file) == True:
        counter += 1
    else:
        print("find if contains digits")
    #if file contains digit true, not string and not empty
    pass

def CheckDate(file, counter):
    if IfEmptyFile(file) == True:
        counter += 1
    else:
        format = re.search("[0-2021][-][0-12][-][0-32][,][0-24][:][0-59]", file)
        if file == format:
            return True

def CheckTags(file):
        #check completely
        pass
    #if file contains strings and commas after every one, two or three words

def CheckProgress(file, counter):
    if IfEmptyFile(file) == True:
        counter += 1
    else:
        format = re.search()
    #if file has correct format -> starts with 'this story has'
    #if file not empty
    pass

def CheckStory(file):
    #if file not empty
    pass

def CheckTitle(file):
    #if file not empty
    #contains string and not numbers
    pass

def CheckUsername(file):
    #if file not empty
    #contains right format 'Posted By'
    pass

def CheckResponse(file):
    #if file not empty if meant to have response
    #if file contains string
    pass 

def CheckResponseHeader(file):
    #if file not empty if meant to have response
    #if file contains string
    #if format right -> contains commas
    pass

def CheckResponseTime(file):
    #if file not empty if meant to have response
    #if file has right format 'Submitted on XXXXXX at XX:XX'
    pass

def CheckUpdate(file):
    #if file not empty if meant to have update
    #if file has strings
    pass

def CheckUpdateTime(file):
    #if file not empty if meant to have update
    #if file right format 'Submitted on XXXXX at XX:XX and published ....'
    pass

def main():
    counter = 0
    f_id_about = open("/Users/jakha/Documents/Professional Computing/webscrape_files/70000/70000_Date", "r")

    CheckAbout(f_id_about, counter)

    path_all_files = "/Users/jakha/Documents/Professional Computing/webscrape_files"

    # for num in range(70000, 70002):
    #     id = str(num)
    #     story_folder = os.path.join(path_all_files, id)
        
        
    #     # f_id_about = open(story_folder + id + "_About")
    #     f_id_activity = open(story_folder + id + "_Activity")
    #     f_id_date = open(story_folder + id + "_Date")
    #     f_id_feel = open(story_folder + id + "_Feel")
    #     f_id_good = open(story_folder + id + "_Good")
    #     f_id_improved = open(story_folder + id + "_Improved")
    #     f_id_progress = open(story_folder + id + "_Progress")
    #     f_id_similar = open(story_folder + id + "_Similar")
    #     f_id_story = open(story_folder + id + "_Story")
    #     f_id_title = open(story_folder + id + "_Title")
    #     f_id_username = open(story_folder + id + "_Username")

    #     CheckDate()
    
        #access each folder
        ###acesss all files in folder
        ###access files in response folder
        ###access files in updates folder

if __name__ == "__main__":
    main()


