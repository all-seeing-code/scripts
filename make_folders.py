import os,sys
from os import listdir
from os.path import isfile

#function to take care of hidden files
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

#mypath = raw_input('Input the folder address you want to work on Eg. /Users/Downloads : ')
mypath = sys.argv[1]
print mypath
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
