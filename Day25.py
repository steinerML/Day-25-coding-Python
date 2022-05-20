import math as kk #Import package math as kk
print(dir())
print(kk.pi)
print(round(kk.pi,4))
print("End of math import exercise")


from random import * #Import package random completely (*)

print(randint(20,30)) #Print a random integer between 20 and 30 included

print("End of random import exercise")

import numpy #Import numpy package

print(dir(numpy)) #Prints the whole content of the numpy package
print(numpy.log(10)) #Print using numpy log(10)

print("End of numpy import exercise")

from pandas import plotting #Import panda subpackage, in this case .plotting

print(dir(pandas.plotting)[:3]) #Print the first 3 elements of pandas.plotting

print(dir(pandas.plotting)) #Prints the whole content of the plotting subpackage

print("End of pandas import exercise")