import os
import time
class info:
    name = ''
    author = ''
    date = ''
    version = ''
    desc = ''
def start_main(fn):
    if os.path.isfile(fn+".pinfo") == True:
        print('Warning: '+fn+".pinfo already exists. 5 seconds to run, or close program.")
        time.sleep(5)
        infofile = open(fn+".pinfo","w")
        infofile.write("Pinfo Configuration")
        infofile = open(fn+".pinfo","a")
        infofile.write("\n"+info.name)
        infofile.write("\n"+info.author)
        infofile.write("\n"+info.date)
        infofile.write("\n"+info.version)
        infofile.write("\n"+info.desc)
        infofile.close()
    else:
        infofile = open(fn+".pinfo","x")
        infofile = open(fn+".pinfo","w")
        infofile.write("Pinfo Configuration")
        infofile = open(fn+".pinfo","a")
        infofile.write("\n"+info.name)
        infofile.write("\n"+info.author)
        infofile.write("\n"+info.date)
        infofile.write("\n"+info.version)
        infofile.write("\n"+info.desc)
        infofile.close()
def infocreate(name,author,date,version,desc,fn):
    info.name = "Name:"+name
    info.author = "Author:"+author
    info.date = "Date:"+date
    info.version = "Version:"+version
    info.desc = "Description:"+desc
    start_main(fn)
def setup():
    name = input("What is the name: ")
    author = input("What is the author: ")
    date = input("What is the date: ")
    version = input("What is the version: ")
    desc = input("What is the description: ")
    fn = input("What should pinfo name be? e.g SAK = SAK.pinfo: ")
    info.name = "Name:"+name
    info.author = "Author:"+author
    info.date = "Date:"+date
    info.version = "Version:"+version
    info.desc = "Description:"+desc
    start_main(fn)
