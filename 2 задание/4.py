
import math
x=(4000)
y=(-0.875)
z=(-0.000475)
a=(abs(math.cos(x)-math.cos(y)))**(1+2*(math.sin(y)**2))
b=(1+z+(z**2)/(2+z**3)/3+(z**4)/4)
s=a*b
print(s)
