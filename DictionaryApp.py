import json
import difflib as d
file = json.load(open("076 data.json",'r'))

def def_funct(w):
    w = w.lower()
    if w in file:
        return file[w]
    elif len(d.get_close_matches(w,file.keys()))>0:
        o=input("is it about {}. Press Y if Yes otherwise N if No: ".format(d.get_close_matches(w,file.keys())[0]))
        o =o.upper()
        if o == "Y":
            return file[d.get_close_matches(w,file.keys())[0]]
        else:
            return "we didn't understand you entered"    

    else:
        return "The word does not exist please double check it"


word=input("Enter the word: ")
output = def_funct(word)
if type(output) is list:
    for i in output:
        print(i)
else:
    print(output)

