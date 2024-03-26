#program:       LVL
#purpose:       handle lvls
#progamer:      Themadhood Pequot 3/21/2024

_INCREMENT = 2
_FILE = "Numbers.LVL"
_VERSION = "0.0.5"
#window settings
_FG = "red"
_BG = "black"


try:
    from .CleenNumbers import *
except:
    from CleenNumbers import *

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
    

class LVL:
    _totalBuff = 0
    def __init__(self,lvl=1,xp=0,name="",icrmt=_INCREMENT,lvlupcmd=None,
                 lvlBuffs=None,error=False):
        self._Error = error
        Error.Log(f"initiating {name} lvl","Log.txt")
        st = Error.time.time()
        
        self._name = name.capitalize()
        self._lvlupcmd = lvlupcmd
        self._winWigits = {}
        
        #lvl
        self._lvl = lvl
        if self._lvl == 0:
            self._lvl += 1

        #XP
        self._xp = xp
        self._nextLVLxp = self._icrmt = icrmt
        while xp >= self._nextLVLxp:
            self._nextLVLxp *= self._icrmt

        #lvl buff
        self._lvlBuffs = lvlBuffs
        if self._lvlBuffs == None:
            self._lvlBuffs = {}
        self.UpdateTotalBuff()
        
        
        #Final calibration
        self.LvlCheck()
        Error.Log(f"{name} lvl initiating runtime: {Error.LenTime(st)}",
                  "Log.txt")
        
#############################################################################
############################### Make win Functions ##########################
#############################################################################
    def LVLLbl(self,parent,**args):
        if "Name" in self._winWigits:
            Error.Log(f"making new lbl for lvl","Log.txt")
            #make str
            text = f"LVL: {self._lvl + self._totalBuff}"
            if self._name != "":
                text = f"{self._name} {text}"
            #make lbl
            lbl = tk.Label(parent,text = text,**args)
            self._winWigits["Name"].append(lbl)
            return lbl
        else:
            #add name to wigits
            Error.Log(f"adding name to win wigits","Log.txt")
            self._winWigits.update({"Name":[]})
            return self.LVLLbl(parent=parent,**args)

        
    def XPLbl(self,parent,displayXP=True,**args):
        if "XP" in self._winWigits:
            Error.Log(f"making new lbl for XP","Log.txt")
            #make str
            text = "XP:"
            if displayXP:
                text += f" {CleenNumbers(self._xp,False)}"
            #make lbl
            lbl = tk.Label(parent,text = text,**args)
            self._winWigits["XP"].append((lbl,displayXP))
            return lbl
        else:
            #add name to wigits
            Error.Log(f"adding XP to win wigits","Log.txt")
            self._winWigits.update({"XP":[]})
            return self.XPLbl(parent=parent,**args)

        
    def XPProgressLbl(self,parent,**args):
        if "XPProgresslbl" in self._winWigits:
            Error.Log(f"making new lbl for XP Progress","Log.txt")
            #make lbl
            lbl = tk.Label(parent,width= (5*2)+1,
                           text = f"{CleenNumbers(self._xp,False)}\
/{CleenNumbers(self._nextLVLxp,False)}",
                           **args)
            self._winWigits["XPProgresslbl"].append(lbl)
            return lbl
        else:
            #add name to wigits
            Error.Log(f"adding XPProgresslbl to win wigits","Log.txt")
            self._winWigits.update({"XPProgresslbl":[]})
            return self.XPProgressLbl(parent=parent,**args)

        
    def XPProgressbar(self,parent,style=None,length=100):
        if "XPProgressbar" in self._winWigits:
            Error.Log(f"making new XP Progress bar","Log.txt")
            #make progres bar
            bar = ttk.Progressbar(parent,orient="horizontal",length=length,
                                  mode="determinate",maximum=self._nextLVLxp,
                                  value=self._xp,style=style)
            self._winWigits["XPProgressbar"].append(bar)
            return bar
        else:
            #add name to wigits
            Error.Log(f"adding XPProgressbar to win wigits","Log.txt")
            self._winWigits.update({"XPProgressbar":[]})
            return self.XPProgressbar(parent=parent,style=style)

    def XPbtn(self,parent,pack=False,grid=False,place=False,args={},**kargs):
        if "XPbtn" in self._winWigits:
            Error.Log(f"making new btn for adding XP","Log.txt")
            #make btn
            bar = tk.Button(parent,text ="+",command=self._AddXP,**kargs)
            self._winWigits["XPbtn"].append((bar,pack,grid,place,args))
            return bar
        else:
            #add name to wigits
            Error.Log(f"adding XPbtn to win wigits","Log.txt")
            self._winWigits.update({"XPbtn":[]})
            return self.XPbtn(parent=parent,pack=pack,grid=grid,place=place,
                              args=args,**kargs)

    def Frm(self,parent,**args):
        if "frm" in self._winWigits:
            Error.Log(f"making new frm","Log.txt")
            #make frm
            frm = tk.Frame(parent,**args)
            self._winWigits["frm"].append(frm)
            return frm
        else:
            #add name to wigits
            Error.Log(f"adding frm to win wigits","Log.txt")
            self._winWigits.update({"frm":[]})
            return self.Frm(parent=parent,**args)

    def MakeFrmBar(self,parent,bg,fg):
        Error.Log(f"making new preset frm bar","Log.txt")
        font = (f'timesnewroman 9 bold')
        
        frm = self.Frm(parent=parent,bg=bg,height=25)
        
        lvl = self.LVLLbl(parent=frm,bg=bg,fg=fg,font=font)
        lvl.pack(side="left",padx=3)
        
        xp = self.XPLbl(parent=frm,displayXP=False,bg=bg,fg=fg,font=font)
        xp.pack(side="left",expand=True,anchor="e")
        
        xpbar = self.XPProgressbar(parent=frm,style=f"{fg}.Horizontal.TProgressbar")
        xpbar.pack(side="left",fill="x")
        
        xpprog = self.XPProgressLbl(parent=frm,bg=bg,fg=fg,font=font)
        xpprog.pack(side="left",expand=True,anchor="w")
        
        add = self.XPbtn(parent=frm,bg=fg,fg=bg,font=font)
        add.pack(side="right")
        
        return frm

        
#############################################################################
############################# Update win Functions ##########################
#############################################################################

    def ReloadLVLLbl(self):
        try:
            if "Name" in self._winWigits:
                Error.Log(f"Reloading lbls for lvl","Log.txt")
                #make str
                text = f"LVL: {self._lvl + self._totalBuff}"
                if self._name != "":
                    text = f"{self._name} {text}"
                #make lbl
                for lbl in self._winWigits["Name"]:
                    try:
                        lbl.config(text = text)
                    except:
                        Error.UploadError([_FILE,_VERSION,"LVL","ReloadLVLLbl",
                               f"failer to reload lvl lbl",e],
                              "GameFoundations")
        except Exception as e:
            if not self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","ReloadLVLLbl",
                               f"failer to reload lvl lbls",e],
                              "GameFoundations")

        
    def ReloadXPLbl(self):
        try:
            if "XP" in self._winWigits:
                Error.Log(f"Reloading lbls for XP","Log.txt")
                #make str
                text = f"XP: {CleenNumbers(self._xp,False)}"
                #make lbl
                for lbl in self._winWigits["XP"]:
                    try:
                        if lbl[1]:
                            lbl[0].config(text = text)
                    except Exception as e:
                        Error.UploadError([_FILE,_VERSION,"LVL","ReloadXPLbl",
                               f"failer to reload xp lbl",e],
                              "GameFoundations")
        except Exception as e:
            if not self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","ReloadXPLbl",
                               f"failer to reload xp lbls",e],
                              "GameFoundations")

        
    def ReloadXPProgressLbl(self):
        try:
            if "XPProgresslbl" in self._winWigits:
                Error.Log(f"Reloading lbls for XP Progress","Log.txt")
                text = f"{CleenNumbers(self._xp,False)}\
    /{CleenNumbers(self._nextLVLxp,False)}"
                #make lbl
                for lbl in self._winWigits["XPProgresslbl"]:
                    try:
                        lbl.config(text = text)
                    except Exception as e:
                        Error.UploadError([_FILE,_VERSION,"LVL",
                                           "ReloadXPProgressLbl",
                               f"failer to reload xp progress",e],
                              "GameFoundations")
        except Exception as e:
            if not self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","ReloadXPProgressLbl",
                               f"failer to reload xp progresses",e],
                              "GameFoundations")

        
    def ReloadXPProgressbar(self):
        try:
            if "XPProgressbar" in self._winWigits:
                Error.Log(f"Reloading XP Progress bars","Log.txt")
                #make progres bar
                for bar in self._winWigits["XPProgresslbl"]:
                    try:
                        bar.config(maximum=self._nextLVLxp)
                        bar["value"] = self._xp
                    except Exception as e:
                        Error.UploadError([_FILE,_VERSION,"LVL","ReloadXPProgressbar",
                               f"failer to reload xp progress bar",e],
                              "GameFoundations")
        except Exception as e:
            if not self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","ReloadXPProgressbar",
                               f"failer to reload xp progress bars",e],
                              "GameFoundations")

    def ReloadAll(self):
        self.ReloadLVLLbl()
        self.ReloadXPLbl()
        self.ReloadXPProgressLbl()
        self.ReloadXPProgressbar()

        
        
#############################################################################
############################### Set Functions ###############################
#############################################################################
    def SetName(self,name):
        Error.Log(f"set name to {name}","Log.txt")
        self._name = name.capitalize()
        self.ReloadLVLLbl()
        
    def SetlvlBuff(self,name,amount):
        Error.Log(f"set buff {name} {amount}","Log.txt")
        if name in self._lvlBuffs:
            self._lvlBuffs[name] = amount
        else:
            self._lvlBuffs.update({name:amount})
        self.UpdateTotalBuff()

    def SetXp(self,amount):
        Error.Log(f"set xp {amount}","Log.txt")
        self._xp = amount
        lvldifrence = self.LvlCheck()
        return lvldifrence

    def SetIcrmt(self,icrmt):
        Error.Log(f"set incramint {icrmt}","Log.txt")
        self._icrmt = icrmt
        self.LvlCheck()

        
#############################################################################
############################ random Functions ###############################
#############################################################################

    def Admin(self,admin=False):
        Error.Log(f"set lvl admin","Log.txt")
        try:
            for btn in self._winWigits["XPbtn"]:
                if btn[1]:#pack
                    try:
                        btn[0].pack_forget()
                    except:
                        pass
                    if admin:
                        btn[0].pack(btn[4])
                if btn[2]:#grid
                    try:
                        btn[0].grid_forget()
                    except:
                        pass
                    if admin:
                        btn[0].grid(btn[4])
                if btn[3]:#place
                    try:
                        btn[0].place_forget()
                    except:
                        pass
                    if admin:
                        btn[0].place(btn[4])
                    
        except Exception as e:
            if not self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","Admin",
                               f"admin failer",e],"GameFoundations")

    def Get(self):
        Error.Log(f"get lvl stats","Log.txt")
        return {"LVL":self._lvl,
                "XP":self._xp,
                "LVL Buffs":self._lvlBuffs,
                "LVL Buff Total":self._totalBuff}

    def UpdateTotalBuff(self):
        Error.Log(f"updating total buff","Log.txt")
        self._totalBuff = 0
        for buff in self._lvlBuffs:
            self._totalBuff += self._lvlBuffs[buff]
        
        self.ReloadLVLLbl()
            
    def AddXP(self,amount):
        Error.Log(f"add {amount} xp","Log.txt")
        self._xp += amount
        lvldifrence = self.LvlCheck()
        
        self.ReloadXPLbl()
        self.ReloadXPProgressLbl()
        self.ReloadXPProgressbar()
        
        return lvldifrence

    def _AddXP(self):
        Error.Log(f"{self._name} add xp prompt","Log.txt")
        try:
            amount = simpledialog.askinteger(" ","Add XP",
                                             parent=self._frm,
                                             minvalue=-9999999999999,
                                             maxvalue=9999999999999)
            if amount != None:
                self.AddXP(amount)
        except Exception as e:
            if not self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Lvl","_AddXP",
                               f"failer to prompt to add xp",e],
                              "GameFoundations")
    
#############################################################################
############################### Set Functions ###############################
#############################################################################
    def _Check(self):
        Error.Log(f"check lvl","Log.txt")
        try:
            lvl = xp = 1
            while xp < self._xp:
                lvl += 1
                xp *= self._icrmt
            if lvl >= self._lvl:
                return True
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","_Check",
                               f"Failed to chek lvl",e],
                              "GameFoundations")
        return False
        
    def _LvlUp(self):
        Error.Log(f"lvlup","Log.txt")
        try:
            self._lvl += 1
            self._nextLVLxp *= self._icrmt
            if self._lvlupcmd != None:
                self._lvlupcmd()
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","_LvlUp",
                               f"Failed to run a external lvl up",e],
                              "GameFoundations")

    def LvlUp(self):
        Error.Log(f"lvlup","Log.txt")
        try:
            self._xp = self._nextLVLxp
            self.LvlCheck()
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","LvlUp",
                               f"Failed to lvl up",e],
                              "GameFoundations")

    def LvlCheck(self):
        Error.Log(f"lvl check","Log.txt")
        difrence = 0
        try:
            while self._xp >= self._nextLVLxp:
                if self._Check():
                    self._LvlUp()
                    difrence += 1
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","LvlCheck",
                               f"Failed to chek lvl difrence",e],
                              "GameFoundations")
        self.ReloadAll()
        return difrence

    def SetLVL(self,NewLvl):
        Error.Log(f"set lvl {NewLvl}","Log.txt")
        try:
            if NewLvl > self._lvl:
                difrence = 0
                while NewLvl > self._lvl:
                    self._LvlUp()
                    difrence += 1
                return difrence
            else:
                print(f"New LVL is Lessthan or equil to current lvl")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","SetLVL",
                               f"Failed to set lvl to: {NewLvl}",e],
                              "GameFoundations")
        self.ReloadAll()
    
    def LvlBy10s(self,amount = 1):
        Error.Log(f"lvl by 10","Log.txt")
        try:
            devided = self._lvl//10
            if devided >=1:
                if amount <= devided:
                    return True
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"LVL","LvlBy10s",
                        f"Failed to devide lvl by 10 an copare to {amount}",e],
                              "GameFoundations")
        return False





if __name__ == "__main__":
    root = tk.Tk()
    lvl = LVL(error=True)
    frm = lvl.MakeFrmBar(parent=root,bg=_BG,fg=_FG)
    frm.pack(fill="x")
















