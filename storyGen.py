import json
import sys

# Validate the Json string. See if the Json string is missing any element. 
def validJson(jsonDict):
    usage = """Usage: python storyGen.py '{ "NUMBER": "100", "UNIT_OF_MEASURE": "meters", "PLACE": "work", "ADJECTIVE": "black", "NOUN": "iPhone" }'\n"""
    elements = ["NUMBER", "UNIT_OF_MEASURE", "PLACE", "ADJECTIVE","NOUN"]
    for e in elements:
        # making sure NUMBER can be converted to a number for statistics application. 
        if e == "NUMBER" and e in jsonDict:
            try:
                float(jsonDict[e])
            except ValueError:
                print "\nPlease make sure NUMBER can be converted to a number.\n%s" % usage
                raise SystemExit

        if e not in jsonDict:
            print "\nMissng %s" %e
            print "\n%sPlease check your input JSON string. Exiting...\n" % usage
            raise SystemExit

# Storing the User input to a log file for the statistics application
def logging(jsonDict):
    logging = open('logs.txt', "a")
    logging.write(json.dumps(jsonDict) + '\n')
    logging.close()

# Generating story base on user input and template.
def storyGen(template, jsonDict):
    print template % (str(jsonDict['NUMBER']), jsonDict["UNIT_OF_MEASURE"], jsonDict["PLACE"], jsonDict["ADJECTIVE"], jsonDict["NOUN"])


if __name__ == "__main__":
    data = sys.argv[1]
    template = "One day Anna was walking her %s %s commute to %s and found a %s %s on the ground."

    try:
        jsonDict = json.loads(data)
    except ValueError as e:
        print "Please enter a valid JSON string."
        raise SystemExit
    
    validJson(jsonDict)
    logging(jsonDict)
    storyGen(template, jsonDict)
