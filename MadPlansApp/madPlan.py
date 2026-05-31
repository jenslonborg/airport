from calendar import weekday
from enum import Enum
from msilib import sequence
import sys
from itertools import repeat
import random

class Diatary(Enum):
    Vegetar = 1
    Okse    = 2
    Kylling = 3
    Fisk    = 4
    Gris    = 5
    Mix     = 6

class Meal:
    def __init__(self, name, duration, diatary, recipeLink = "", ingredients = {}):
        self.name         = name
        self.duration     = duration
        self.diatary      = diatary
        self.recipeLink   = recipeLink
        self.ingiridients = ingredients

class Weekday(Enum):
    Mandag  = 1
    Tirsdag = 2
    Onsdag  = 3
    Torsdag = 4
    Fredag  = 5

def autoSekvens(s,r):
    l = list(repeat(1,s-2*r))
    l.extend(list(repeat(2,r)))  
    random.shuffle(l) 
    return l

def listToIntList(l):
    if type(l) == str:
        l = l.split("&")
        return [eval(i) for i in l]
    else:
        return [l]


def argsToDict(sysargv):
    argsDict = {
        "spisedage"  : 5,
        "resterdage" : 2,
        "sekvens"    : "2&2&1",
        "skipdag"    : 0
    }
    if  (len(sysargv) % 2) == 0:
        i = 0
        while (i < len(sysargv)):
            k = sysargv[i].strip("-")
            v = sysargv[i+1]
            if (eval(v) != 0):
                argsDict[k] = eval(v)
            else: 
                argsDict[k] = v
            i += 2

    
    argsDict["skipdag"] = listToIntList(argsDict["skipdag"])
    argsDict["sekvens"] = listToIntList(argsDict["sekvens"])

    if sum(argsDict["sekvens"]) != argsDict["spisedage"]:
        print("Sekvens matcher ikke antal spisedage. Genererer sekvens automatisk")
        argsDict["sekvens"] = autoSekvens(argsDict["spisedage"],argsDict["resterdage"])
    if argsDict["sekvens"].count(2) != argsDict["resterdage"]:
        print("Sekvens matcher ikke antal resterdage. Genererer sekvens automatisk")
        argsDict["sekvens"] = autoSekvens(argsDict["spisedage"],argsDict["resterdage"])
    return argsDict 

if __name__ == "__main__":
    meals1D = [
        Meal("Karry suppe",                 1, Diatary.Vegetar,  "Opskriftsbog"),
        Meal("Spinat vafler",               1, Diatary.Fisk,    ),
        Meal("Kartoffel-porre suppe",       1, Diatary.Vegetar , "Opskriftsbog"),"https://www.valdemarsro.dk/spinatvafler/"
        Meal("Crispy Kylling burger",       1, Diatary.Kylling, "https://www.valdemarsro.dk/burger-med-crispy-kylling/"),
        Meal("Karbonader",                  1, Diatary.Gris,    "Opskriftsbog"),
        Meal("Pitabrød med tun",            1, Diatary.Fisk),
        Meal("Rugbrød med fiskedeller",     1, Diatary.Fisk),
        Meal("Tortilla m fyld",             1, Diatary.Mix),
        Meal("Pokebowl m kylling",          1, Diatary.Kylling,  "https://bellasmadunivers.dk/opskrift/hjemmelavet-poke-bowl-med-teriyaki-kylling/"),       
        Meal("Pasta carbonara",             1, Diatary.Gris,     "https://www.valdemarsro.dk/carbonara_opskrift/"), 
        Meal("Sund okse risret",            1, Diatary.Okse,     "https://www.instagram.com/reel/C17TGAaNOiy/?utm_source=ig_web_copy_link"), 
        Meal("Avokado-æggemad",             1, Diatary.Vegetar,  "https://www.instagram.com/reel/C1RjYD4NlUs/?utm_source=ig_web_copy_link"),
        Meal("Torske-Tacos",                1, Diatary.Fisk,     "https://mambeno.dk/opskrifter/fish-tacos-med-paneret-torsk-mangosalat-og-dressing/"),
        Meal("Kebab med grøntsager",        1, Diatary.Okse,     "https://mambeno.dk/opskrifter/durum-med-kebab-groentsager-dressing-og-pommes-frites/ + https://mambeno.dk/opskrifter/hjemmelavede-fladbroed/")
        
    ]
    
    meals2D = [
        Meal("Kylling i pikant",            2, Diatary.Kylling, "Opskriftsbog"),
        Meal("Mac and Cheese",              2, Diatary.Okse,     "https://mambeno.dk/opskrifter/krydret-mac-and-cheese-med-oksekoed-og-kidneyboenner-til-to-dage/"),
        Meal("Pasta kødsovs",               2, Diatary.Okse),
        Meal("Okse-ris-ret",                2, Diatary.Okse,    "Opskriftsbog"),
        Meal("Sød kartoffel gryde",         2, Diatary.Vegetar,  "https://stinna.dk/aftensmad/soed-kartoffel-gryde.html"),
        Meal("Lasagne",                     2, Diatary.Okse,    "https://www.valdemarsro.dk/lasagne/"),        
        Meal("Bønne gryde",                 2, Diatary.Vegetar,  "https://www.valdemarsro.dk/boennegryde/"),
        Meal("Frikadeller",                 2, Diatary.Gris,    "Opskriftsbog"),
        Meal("Pitabrød med skinke",         2, Diatary.Gris),
        Meal("Butter chicken",              2, Diatary.Kylling, "https://gourministeriet.dk/cremet-butter-chicken/?fbclid=IwAR1W2yApwRrK1cG281-Qyyu3J-cAiyc9WWLDInnjhFy3u5nAoWPoVKZqPxo"),
        Meal("Quesadillas med kylling",     2, Diatary.Kylling, "https://martinys.dk/quesadillas-med-kylling/"),
        Meal("Vegetar lasagne",             2, Diatary.Vegetar, "https://www.louisesmadblog.dk/super-laekker-vegetarlasagne/"),
        Meal("Tærte",                       2, Diatary.Gris),
        Meal("Thai inspireret farsbrød",    2, Diatary.Kylling),"https://mambeno.dk/opskrifter/thai-inspireret-farsbroed-med-ris-kokossauce-og-peanuts-til-to-dage/"
    ]
    argsDict = argsToDict(sys.argv[1:])
    madplan = {
        Weekday(1) : "-",
        Weekday(2) : "-",
        Weekday(4) : "-",
        Weekday(5) : "-"
    }
    daycounter = 1
    for el in argsDict["sekvens"]:
        t = 1
        while t <= el:
            # Check if this day needs to be skipped
            while argsDict["skipdag"].count(daycounter) > 0:
                daycounter += 1
            ugedag = Weekday(daycounter)
            if el == 1:
                meal1D = random.choice(meals1D)
                madplan[ugedag] = meal1D.name
                if (meal1D.recipeLink != ""):
                    madplan[ugedag] = madplan[ugedag] + " - " + meal1D.recipeLink
                daycounter += 1
                t += 1
            else:
                meal2D = random.choice(meals2D)
                madplan[ugedag] = meal2D.name
                if (meal2D.recipeLink != ""):
                    madplan[ugedag] = madplan[ugedag] +  " - " + meal2D.recipeLink
                daycounter += 1
                while argsDict["skipdag"].count(daycounter) > 0:
                    daycounter += 1
                ugedag = Weekday(daycounter)
                madplan[ugedag] = "Rester"
                daycounter += 1
                t += 2
    for k,v in madplan.items():
        print(k.name + " : " + v)
                    




        
                






    
