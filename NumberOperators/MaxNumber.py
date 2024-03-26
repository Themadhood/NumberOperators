#program:       MaxNumber
#purpose:       handles numbers
#progamer:      Themadhood Pequot 3/22/2022

_FILE = "Numbers.MaxNumber"
_VERSION = "0.0.4"

_FG = "red"
_BG = "black"

try:
    from .CleenNumbers import *
except:
    from CleenNumbers import *

import tkinter as tk
from tkinter import ttk



class MaxNumber:
    _totalBuff = 0
    def __init__(self,maxNumber,buffs=None,name="",error=False):
        self._Error = error
        Error.Log(f"initiating {name} lvl","Log.txt")
        st = Error.time.time()
        
        self._max = maxNumber
        self._name = name
        self._winWigits = {}
        
        #lvl buff
        self._Buffs = buffs
        if self._Buffs == None:
            self._Buffs = {}
        self.UpdateTotalBuff()
        
        self.ResetCurrent()

########################################################################
########################## Make win Functions ##########################
########################################################################
    def NameLbl(self,parent,**args):
        if "Name" in self._winWigits:
            Error.Log(f"making new lbl for Name","Log.txt")
            #make lbl
            lbl = tk.Label(parent,text = f"{self._name}: ",**args)
            self._winWigits["Name"].append(lbl)
            return lbl
        else:
            #add name to wigits
            Error.Log(f"adding Name to win wigits","Log.txt")
            self._winWigits.update({"Name":[]})
            return self.NameLbl(parent=parent,**args)

        
    def FractionLbl(self,parent,**args):
        if "Fraction" in self._winWigits:
            Error.Log(f"making new lbl for Fraction","Log.txt")
            #make lbl
            lbl = tk.Label(parent,width= (5*2)+1,
                           text = f"{CleenNumbers(self._current,False)}\
/{CleenNumbers(self._max + self._totalBuff,False)}",**args)
            self._winWigits["Fraction"].append(lbl)
            return lbl
        else:
            #add name to wigits
            Error.Log(f"adding Fraction to win wigits","Log.txt")
            self._winWigits.update({"Fraction":[]})
            return self.FractionLbl(parent=parent,**args)

        
    def Progressbar(self,parent,style=None,length=233):
        if "Progressbar" in self._winWigits:
            Error.Log(f"making new Progress bar","Log.txt")
            #make progres bar
            bar = ttk.Progressbar(parent,orient="horizontal",
                                  mode="determinate",length=length,
                                  maximum=self._max + self._totalBuff,
                                  value=self._current,style=style)
            self._winWigits["Progressbar"].append(bar)
            return bar
        else:
            #add name to wigits
            Error.Log(f"adding Progressbar to win wigits","Log.txt")
            self._winWigits.update({"Progressbar":[]})
            return self.Progressbar(parent=parent,style=style)

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
        
        name = self.NameLbl(parent=frm,bg=bg,fg=fg,font=font)
        name.pack(side="left")
        
        bar = self.Progressbar(parent=frm,style=f"{fg}.Horizontal.TProgressbar")
        bar.pack(side="left",fill="x",expand=True)
        
        fraction = self.FractionLbl(parent=frm,bg=bg,fg=fg,font=font)
        fraction.pack(side="right")
        
        return frm

        
#############################################################################
############################# Update win Functions ##########################
#############################################################################        
    def ReloadFractionLbl(self):
        try:
            if "Fraction" in self._winWigits:
                Error.Log(f"Reloading lbls for Fraction","Log.txt")
                text = f"{CleenNumbers(self._current,False)}\
    /{CleenNumbers(self._max + self._totalBuff,False)}"
                #make lbl
                for lbl in self._winWigits["Fraction"]:
                    try:
                        lbl.config(text = text)
                    except Exception as e:
                        Error.UploadError([__Program__,__version__,
                               "MaxNumber","ReloadFractionLbl",
                               f"Failed to Reload Fraction",e],
                              "GameFoundations")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,
                               "MaxNumber","ReloadFractionLbl",
                               f"Failed to Reload Fractions",e],
                              "GameFoundations")

        
    def ReloadProgressbar(self):
        try:
        if "Progressbar" in self._winWigits:
            Error.Log(f"Reloading Progress bars","Log.txt")
            #make progres bar
            for bar in self._winWigits["Progressbar"]:
                try:
                    bar.config(maximum=self._max + self._totalBuffp)
                    bar["value"] = self._current
                except Exception as e:
                    Error.UploadError([__Program__,__version__,
                               "MaxNumber","ReloadProgressbar",
                               f"Failed to Reload Progressbar",e],
                              "GameFoundations")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,
                               "MaxNumber","ReloadProgressbar",
                               f"Failed to Reload Progressbars",e],
                              "GameFoundations")

    def ReloadAll(self):
        self.ReloadFractionLbl()
        self.ReloadProgressbar()


########################################################################
################################ Checks ################################
########################################################################

    def CheckIf0(self):
        """return true if current = 0"""
        if self._current > 0:
            return False
        return True

#########################################################################
############################### Sets ####################################
#########################################################################
        
    def SetBuff(self,name,amount):
        Error.Log(f"set buff {name} {amount}","Log.txt")
        try:
            if name in self._Buffs:
                self._Buffs[name] = amount
            else:
                self._Buffs.update({name:amount})
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,
                               "MaxNumber","SetBuf",
                               f"Failed to Set Buff",e],
                              "GameFoundations")
        self.UpdateTotalBuff()

    def SetMax(self,new):
        self._max = new
        self.ReloadAll()

    def SetCurrent(self,new):
        Max = self._max + self._totalBuff
        self._current = min(new,Max)
        self.ReloadAll()

    def SetAll(self,data):
        self.SetMax(data["Max"])
        self._Buffs = data["Buffs"]
        self.SetCurrent(data["Current"])
        self.UpdateTotalBuff()

    def ResetCurrent(self):
        self._current = self._max + self._totalBuff
        self.ReloadAll()

#########################################################################
################################ increses ###############################
#########################################################################

    def IncreseMax(self,amount):
        self._max += amount
        self.ReloadAll()

    def IncreseCurrent(self,amount):
        Max = self._max + self._totalBuff
        new = self._current+amount
        self._current = min(new,Max)
        self.ReloadAll()

#########################################################################
################################ Decreses ###############################
#########################################################################

    def DecreseMax(self,amount):
        Max = self._max + self._totalBuff
        self._max -= amount
        self._current = min(self._current,Max)
        self.ReloadAll()

    def DecreseCurrent(self,amount):
        self._current -= amount
        self.ReloadAll()

#########################################################################
################################ other ##################################
#########################################################################

    def Get(self):
        Error.Log(f"get lvl stats","Log.txt")
        return {"Current":self._current,
                "Max":self._max,
                "Buffs":self._Buffs,
                "Buff Total":self._totalBuff}

    def UpdateTotalBuff(self):
        Error.Log(f"updating total buff","Log.txt")
        try:
            self._totalBuff = 0
            for buff in self._Buffs:
                self._totalBuff += self._Buffs[buff]
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([__Program__,__version__,
                               "MaxNumber","UpdateTotalBuff",
                               f"Failed to Update Total Buff",e],
                              "GameFoundations")
            
        self.ReloadAll()
    
        
        






if __name__ == "__main__":
    root = tk.Tk()
    mn = MaxNumber(maxNumber=5,name="HP",error=True)
    frm = mn.MakeFrmBar(parent=root,bg=_BG,fg=_FG)
    frm.pack(fill="x")










