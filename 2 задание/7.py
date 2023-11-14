
import math
x=(0.1722)
y=(6.33)
z=(0.000325)
a=5*math.atan(x)
b=1/4*math.acos(x)
c=x+3*(abs(x-y))+x**2
d=(abs(x-y))*z+x**2
q=c/d
e=q*b
s=a-e
print(s)
