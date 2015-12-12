import os
from os import listdir
from os.path import isfile

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

#takes input of the folder on which you to want to make changes

print"Input the folder address you want to work on Eg. /Users/Downloads"
mypath = raw_input()
print "Current Directory is: ", os.getcwd()
os.chdir(mypath)
print "Working on: ", os.getcwd()
contents = list(listdir_nohidden(mypath))
file_count, folder_count = 0,0
for i in range(0,len(contents)):
  if(isfile(contents[i])):
    file_count = file_count + 1
    filename , file_extension = os.path.splitext(contents[i])
    folder_name = file_extension[1::1].title()
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
      folder_count = folder_count + 1
    os.rename(contents[i],folder_name +'/'+contents[i])
print "Folders Created %d and Files Moved %d" %(folder_count , file_count)
