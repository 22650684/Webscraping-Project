import os
import sqlite3 
from bs4 import BeautifulSoup

def scan_folder(parentfile, diff, allfiles):
    
    for file_name in os.listdir(parentfile):
        if file_name.endswith("Story") or file_name.endswith("Response") or file_name.endswith("Update"):
            samefile = 0
            with open(parentfile+"/"+file_name, 'r') as reader:
                content = reader.read()
                storyid =file_name[:5]
                for file_name2 in allfiles:
                    storyid2 = file_name2[:5]
                    file2Parent = "/mnt/c/Users/Juju/DB/project/webscrape/realScrape/" + storyid2
                    if "Response" in file_name2:
                        secPath = file2Parent+"/Responses/"+file_name2
                    elif "Update" in file_name2:
                        secPath = file2Parent+"/Updates/"+file_name2
                    else:
                        secPath = file2Parent+"/"+file_name2
                    with open(secPath, 'r') as reader2:
                        content2 = reader2.read()
                        dupmsg = file_name + " and " + file_name2
                        dupmsg2 = file_name2 + " and " + file_name                        
                        if content == content2 and content != "" and dupmsg not in diff and dupmsg2 not in diff and storyid != storyid2:
                            samefile = samefile + 1
                            if (samefile != 0):
                                strMsg = file_name + " and " + file_name2
                                diff.append(strMsg)
            
        else:
            current_path = "".join((parentfile, "/", file_name))
            
            if os.path.isdir(current_path):
                scan_folder(current_path, diff, allfiles)
    return diff
    

def loopFile(parentfile, allfiles):
    for file_name in os.listdir(parentfile):
        if file_name.endswith("Story") or file_name.endswith("Response") or file_name.endswith("Update"):
            allfiles.append(file_name)
            
        else:
            current_path = "".join((parentfile, "/", file_name))
            
            if os.path.isdir(current_path):
                loopFile(current_path, allfiles)
    return allfiles

def main():
    parentfile = "/mnt/c/Users/Juju/DB/project/webscrape/realScrape"
    diff = []
    allfiles = []
    allfiles = loopFile(parentfile, allfiles)
    scan_folder(parentfile, diff, allfiles) 
    if diff:
        print("The file names that have the same content:", diff)
        print("Number of files: ", str(len(diff)))
    else:
        print("Test OK")


if __name__ == "__main__":
    main()
