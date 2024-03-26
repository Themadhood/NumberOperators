#program:       CleenNumbers
#purpose:       cleens up data
#progamer:      Themadhood Pequot 5/27/2022

_FILE = "Numbers.CleenNumbers"
_VERSION = "0.0.1"

import Error

_WKey = {"Thousand":10**3,               "Million":10**6,
         "Billion":10**9,                "Trillion":10**12,
         "Quadrillion":10**15,           "Quintillion":10**18,
         "Sextillion":10**21,            "Septillion":10**24,
         "Octillion":10**27,             "Nonillion":10**30,
         "Decillion":10**33,             "Undecillion":10**36,
         "Duodecillion":10**39,          "Tredecillion":10**42,
         "Quattuordecillion":10**45,     "Quindecillion":10**48,
         "Sexdecillion":10**51,          "Septendecillion":10**54,
         "Octodecillion":10**57,         "Novemdecillion":10**60,
         "Vigintillion":10**63,          "Unvigintillion":10**66,
         "Duovigintillion":10**69,       "Trevigintillion":10**72,
         "Quattuorvigintillion":10**75,  "Quinvigintillion":10**78,
         "Sexvigintillion":10**81,       "Septenvigintillion":10**84,
         "Octovigintillion":10**87,      "Nonvigintillion":10**90,
         "Trigintillion":10**93,         "Untrigintillion":10**96,
         "Duotrigintillion":10**99}

_LKey = {"K":10**3,         "M":10**6,          "B":10**9,
         "t":10**12,        "q":10**15,         "Q":10**18,
         "s":10**21,        "S":10**24,         "o":10**27,
         "n":10**30,        "d":10**33,         "u":10**36,
         "D":10**39,        "T":10**42,         "qu":10**45,
         "Qu":10**48,       "se":10**51,        "Se":10**54,
         "O":10**57,        "N":10**60,         "V":10**63,
         "U":10**66,        "du":10**69,        "tr":10**72,
         "qU":10**75,       "QU":10**78,        "sE":10**81,
         "SE":10**84,       "Oc":10**87,        "No":10**90,
         "Tr":10**93,       "Un":10**96,        "Du":10**99}

def CleenNumbers(number,Word = True):
    #Make the number manigable
    if Word:
        keys = list(_WKey)
        dct = _WKey
    else:
        keys = list(_LKey)
        dct = _LKey
        
    lKey = None
    for key in keys:
        if dct[key] > number:
            break
        else:
            lKey = key

    cleen=number
    if lKey != None:
        n=number//dct[lKey]
        cleen = f"{n} {lKey}"
        
    return cleen






if __name__ == "__main__":
    while True:
        number = input("#: ")
        print(CleenNumbers(int(number)))












