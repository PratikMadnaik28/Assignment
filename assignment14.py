import m1
import m2
import m3

print(m1.f1())
print(m2.f2())
print(m3.f3())



import mod
print(mod.f1())
print(mod.f2())
print(mod.f3())

from mod import f1, f2, f3
print(f1())
print(f2())
print(f3())

from mod import *
print(f1())
print(f2())
print(f3())

import mod as m
print(m.f1())
print(m.f2())
print(m.f3())