name2 = 'SMARTBOX (для Mk5 - исп. п/н 2230050000 12312312312312 123123123; для Mk4 - исп. п/н 2230051000)'



# index = name2.rfind(' ', 0, 38 )
# print(name2[0:38])
# print(index)
# print(len(name2)-38)

def editstring(oldstring):
    startpoint = 0
    endpoint = 38
    maxlen = 38
    stop = 0
    newstring = ''
    while(stop == 0):
        index = oldstring.rfind(' ', startpoint, endpoint)
        newstring = newstring + oldstring[startpoint+1:index]+'\n'
        endpoint = index + maxlen
        startpoint = index+1
        if( (len(oldstring) - startpoint) < maxlen):
            stop = 1
            newstring = newstring + oldstring[startpoint:len(oldstring)]
    return newstring

newname = editstring(name2)
print(newname)