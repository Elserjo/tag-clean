import sys
import os
import mutagen
from mutagen import MutagenError

#Thanks to https://pastebin.com/Ysb25hQh
tagList = [
    "ARTIST", "TITLE", "ALBUM", "DATE", "TRACKNUMBER", 
    "GENRE", "DISCNUMBER", "DISCTOTAL", "TRACKTOTAL",
    "COMPILATION",
]
argv = sys.argv[1:]

def removeMeta(fileName):
    try:
        meta = mutagen.File(fileName)
        fileTags = meta.tags
    except (MutagenError, AttributeError) as err:
        print ("error while opening: {}\n"
                "error code: {}"
                .format(fileName, err))
        return

    toClean = False #Do we need to clean?
    if fileTags is None:
        print("all tags is empty")
        return
    
    for key in fileTags.keys():
        if key.upper() not in tagList:
            print ("not matching:", key.upper())
            toClean = True

    if not toClean:
        print("nothing to clean")
        return

    trackTags = dict()
    for key, value in fileTags:
        if key in tagList:
            trackTags[key] = value    

    meta.delete()
    meta.update(trackTags)
    meta.save() 

for num, fileName in enumerate (argv, start=1):   
    fileBaseName = os.path.basename(fileName)
    fileExtension = os.path.splitext(fileBaseName)[1]
   
    print ("processing file: {} [ {} ]"
            .format(num, fileBaseName))

    if (fileExtension == ".m4a" or 
        fileExtension == ".mp3"):
        print ("can not handle {} extension"
                 .format(fileExtension))
        continue
    removeMeta(fileName)
