import sys
# from .class_ex import divides
# from .class_ex import *
from ..basic.class_ex import *

print(divides(25, 5))

print(sys.path)

"""CHANGE IN PYTHON3
import sys  - To import system all
from .class_ex import divides   - To import specific thing
from .class_ex import *             - To import all from a class
from ..basic.class_ex import *      - one level up
from ...parent.basic.class_ex import *      - two level up
"""

###MOREE
"""
Consider the following tree for example:

mypkg
├── base.py
└── derived.py
Now, your derived.py requires something from base.py. In Python 2, you could do it like this (in derived.py):

from base import BaseThing
Python 3 no longer supports that since it's not explicit whether you want the 'relative' or 'absolute' base. In other words, if there was a Python package named base installed in the system, you'd get the wrong one.

Instead it requires you to use explicit imports which explicitly specify location of a module on a path-alike basis. Your derived.py would look like:

from .base import BaseThing
The leading . says 'import base from module directory'; in other words, .base maps to ./base.py.

Similarly, there is .. prefix which goes up the directory hierarchy like ../ (with ..mod mapping to ../mod.py), and then ... which goes two levels up (../../mod.py) and so on.

"""