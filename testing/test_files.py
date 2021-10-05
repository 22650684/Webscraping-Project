def CompareFiles(str_file1,str_file2):
    '''
    This function compares two long string texts and returns their 
    differences as two sequences of unique lines, one list for each.
    '''
    #reading from text file and splitting str_file into lines - delimited by "\n"
    file1_lines = str_file1.split("\n")
    file2_lines = str_file2.split("\n")

    #unique lines to each one, store it in their respective lists
    unique_file1 = []
    unique_file2 = []

    #unique lines in str1
    for line1 in file1_lines:
        if line1 !='':
           if line1 not in file2_lines:
              unique_file1.append(line1)

    #unique lines in str2
    for line2 in file2_lines:
        if line2 != '':
           if line2 not in file1_lines:
              unique_file2.append(line2)

    return unique_file1, unique_file2

def Masker(pattern_lines, file2mask):
    '''
    This function masks some fields (based on the pattern_lines) with 
    dummy text to simplify the comparison
    '''
    #mask the values of all matches from the pattern_lines by a dummy data - 'xxxxxxxxxx'
    for pattern in pattern_lines:
        temp = pattern.findall(file2mask)
        if len(temp) != 0:
           for value in temp:
               if isinstance(value, str):
                  masked_file = file2mask.replace(str(value),'x'*10)
               elif isinstance(value, tuple):
                    for tup in value:
                        masked_file = file2mask.replace(str(tup),'x'*10)
    return masked_file

def main():
    #using one manually checked folder to compare format with all other folders
    file_about_path = ""
    file_activity_path = ""
    file_date_path = ""
    file_feel_tag_path = ""
    file_good_tag_path = ""
    file_improved_tag_path = ""
    file_similar_path = ""
    file_story_path = ""
    file_title_path = ""
    file_username_path = ""

    file_response_path = ""
    file_response_time = ""

    file_update_path = ""
    file_update_time = ""

    for num in range(50000, 90000):


if __name__ == "__main__":
    main()