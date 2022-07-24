import sys
import mutagen

#Thanks to https://pastebin.com/Ysb25hQh
tagList = ["ARTIST", "TITLE", "ALBUM", "DATE", "TRACKNUMBER", 
            "GENRE", "DISCNUMBER", "DISCTOTAL", "TRACKTOTAL"]
argv = sys.argv[1:]

def setMeta(fileName):
    meta = mutagen.File(fileName)
    fileTags = meta.tags
    trackTags = dict()
    #for field in fileTags:
    for key, value in fileTags:
        if key in tagList:
            trackTags[key] = value    

    meta.delete()
    meta.update(trackTags)
    meta.save() 
    print ("[",fileName,"]", "was processed")

for fileName in argv: 
    setMeta(fileName)

