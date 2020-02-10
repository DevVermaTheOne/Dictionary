import json
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("data.json"))

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()


def translate(w):
    if w in data:
      return data[w]
    else :
        key=get_close_matches(w,data.keys())[0]
    #    sim_ratio_old=0.0
        #for x in data :
        #    sim_ratio_new=similar(w,x)
        #    if(sim_ratio_new>sim_ratio_old):
        #        sim_ratio_old=sim_ratio_new
        #        key=x
        print("Do you mean", key,"? (Answer y to accept ")
        option=input()
        if(option == "y"):
            return  data[key]
        else:
            return "Word not present. Please double check it"


word = (input("Enter a word ")).lower()

print(translate(word))
