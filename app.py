import json
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()


def translate(w):
    if w in data:
      return data[w]
    else :
        sim_ratio_old=0.0
        for x in data :
            sim_ratio_new=similar(w,x)
            if(sim_ratio_new>sim_ratio_old):
                sim_ratio_old=sim_ratio_new
                key=x
        print("Do you mean ", key, " ? (Answer in y/n)")
        option=input()
        if(option == "y"):
            return  data[key]
        else:
            return "Word not present. Please double check it"


word = (input("Enter a word ")).lower()

print(translate(word))
