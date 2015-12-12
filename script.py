import os
from os import listdir
from os.path import isfile

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

mypath = raw_input()
print "Current Directory is: ", os.getcwd()
os.chdir(mypath)
print "Working on : ", os.getcwd()
contents = list(listdir_nohidden(mypath))

for i in range(0,len(contents)):
  if(isfile(contents[i])):
    filename , file_extension = os.path.splitext(contents[i])
    folder_name = file_extension[1::1].title()
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
    os.rename(contents[i],folder_name +'/'+contents[i])
