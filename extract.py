'''
Use the Python os module and regular expressions to iterate through each file,
open it, and search for a telephone number
'''
import zipfile
import os
import re

#extract zipfile. can also use shutil
zip_obj = zipfile.ZipFile('extracted_content.zip', 'r')
zip_obj.extractall("extracted_content2")

#read the instruction.txt
with open(os.getcwd()+'/extracted_content2/extracted_content/instructions.txt') as f:
    content = f.read()
    print(content)


#function for search phone number pattern
def search_pattern (file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    content= f.read()

    if re.search(pattern, content):
        return re.search(pattern, content)
    else:
        return ''


#initiate result
result = []

#oswalk through the folders to locate the filepath.
for folder , sub_folders , files in os.walk(os.getcwd()+"/extracted_content2/extracted_content"):
    for f in files:
        filepath = (folder+'/'+f)
        result.append(search_pattern(filepath))

#print the regression result
for r in result:
    if r != '':
        print (r.group())
