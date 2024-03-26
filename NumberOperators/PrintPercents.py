#program:       PrintPercents
#purpose:       
#progamer:      Themadhood Pequot 1/25/2024

_FILE = "PrintPercents"
_VERSION = "0.0.1"

import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

def PrintByX(llen,index,count,percent,prefix="",error=False):
    X = llen // 10
    L = llen // 2
    try:
        if index == llen:
            print(f"{prefix}100% complete")
            
        elif index == L:
            print(f"{prefix}50% complete")
            count = L + X
            percent = 60
            
        elif index == count and percent != 50 and percent != 100:
            print(f"{prefix}{percent}% complete")
            count += X
            percent += 10

    except Exception as e:
        if error:
            raise
        Error.UploadError([_FILE,_VERSION,"","PrintByX",
                                    f"failed to asertain %",e],"Functions")
    return count,percent



def PrintBy25(llen,index,prefix="",error=False):
    X = llen // 10
    L = llen // 2
    XXV = llen // 4
    try:
        if index == llen:
            print(f"{prefix}100% complete")
            
        elif index == L+XXV:
            print(f"{prefix}75% complete")
            
        elif index == L:
            print(f"{prefix}50% complete")
            
        elif index == XXV:
            print(f"{prefix}25% complete")

        elif index == 0:
            print(f"{prefix}0% complete")

    except Exception as e:
        if error:
            raise
        Error.UploadError([_FILE,_VERSION,"","PrintBy25",
                                    f"failed to asertain %",e],"Functions")

def PrintAll(current,total):
    print((current/total)*100)




if __name__ == "__main__":
    count = percent = 0
    for i in range(0,11):
        count,percent = PrintByX(10,i,count,percent,error=True)

    print()
    
    for i in range(0,5):
        PrintBy25(4,i,error=True)
















