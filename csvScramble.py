import random
def scramble():
    '''
    This function can be used to randomly rearrange a CSV file. Only works on CharmManager's primary save file though as those are hard coded in.
    '''
    #Specifically used to shuffle the charm manager's save file.
    source = open("charmData.csv","r")

    intermediary = []
    for i in source:
        intermediary.append(i)
    source.close()

    scrambled = open("charmData.csv","w")
    while len(intermediary)>0:
        r = random.randrange(0,len(intermediary))
        scrambled.write(intermediary.pop(r))
    scrambled.close()

scramble()
