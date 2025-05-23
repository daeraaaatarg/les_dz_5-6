#import time
# press CTRL
# info about libraries
# ========understand the thing
#import inspect
#print(inspect.isfunction(time))
#print(inspect.isclass(time))
#print(inspect.ismodule(time))
# ========system of the comp
#import sys
#print(sys.platform)

# ========install modul - by terminal - pip install *name*

print("==============================================")

# ========exceptions==========
# if no mistakes in try - then excepts don't react
try:
    print("Hello")   # ok
    print(error)     # jump to except
    print("world")   # it doesn't work
except:
    print("error")   # from here
print("finish")      # just random
# baseexceptions
# one try, countless exceptions
try:
    print("start")
    print(10/0)
except NameError:          # doesn't work
    print("error")
except ZeroDivisionError:        #base one
    print("zero")
# unite
except (NameError, ZeroDivisionError):
    print("zero")
# try in try
try:
    print("first")
    try:
        print(error)
        print("no errors")
    except SyntaxError:
        print("syntax")
except NameError:
    print("error")

print("==============================================")

#====== my errors
#class BuildError(Exception):
#    def __str__(self):
#        return "we catch error"     #my error in PLAY

#def material(amount, limit):
#    if amount > limit:
#        return "enough cash"
#    else:
#        raise BuildError(amount)

#number = 120
#material(number, 300)

print("==============================================")

# warning
import warnings
# what and why
warnings.warn("Warning!", SyntaxWarning)
warnings.simplefilter("ignore", SyntaxWarning)