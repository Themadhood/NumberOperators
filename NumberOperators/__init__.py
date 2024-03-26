#program:       Numbers
#purpose:       
#progamer:      Themadhood Pequot 1/24/2022

_FILE = "Numbers.__init__"
_VERSION = "0.0.2"

try:
    from . import LVL as _LVL
    from . import MaxNumber as _MaxNumber
except:
    import LVL as _LVL
    import MaxNumber as _MaxNumber


tk = _LVL.tk
ttk = _LVL.ttk
LVL = _LVL.LVL
Error = _LVL.Error
CleenNumbers = _LVL.CleenNumbers


MaxNumber = _MaxNumber.MaxNumber




