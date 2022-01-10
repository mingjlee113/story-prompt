from collections import Counter
import json

if __name__ == "__main__":
    try:
        f = open("logs.txt", "r")
    except IOError:
        print "Error opening file. Hint: check if the file exist"
        raise SystemExit
    
    entries = []
    
    for line in f:
        l = json.loads(line)
        entries.append(l)
    
    distanceList = sorted([float(e["NUMBER"]) for e in entries])
    
    if len(distanceList) > 0:
        print "The longest distance is: %f." % distanceList[len(distanceList)-1]
        print "The shortest distance is %f." % distanceList[0]

    unitList = Counter(str(e['UNIT_OF_MEASURE']) for e in entries)
    placeList = Counter(str(e['PLACE']) for e in entries)
    adjList = Counter(str(e['ADJECTIVE']) for e in entries)
    nounList = Counter(str(e['NOUN']) for e in entries)

    print "The most common unit is %s" % unitList.most_common()
    print "The most common place is %s" % placeList.most_common()
    print "The most common adjective is %s" % adjList.most_common()
    print "The most common noun is %s" % nounList.most_common()
    f.close()

