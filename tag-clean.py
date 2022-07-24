import sys
import mutagen

tagList = ["artist", "title", "album", "date", "tracknumber", 
            "genre", "discnumber", "disctotal", "tracktotal"]
argv = sys.argv[1:]

def getMeta(fileName):
    meta = mutagen.File(fileName)
    fileTags = meta.tags
    isDel = True
    i = 0
    #for field in fileTags:
    while i < len (fileTags.keys()):
        currentTag = fileTags.keys()[i]
        print(currentTag, i)
        i = i + 1
        for verifyTag in tagList:
            if verifyTag == currentTag:
                isDel = False
                break
            else:
                isDel = True
        if isDel:
            print ("Will be deleted:", currentTag) 
            meta.pop(currentTag)
            meta.save()

for fileName in argv: 
    getMeta(fileName)

