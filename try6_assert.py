"""
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
"""

def KelvinToFahrenheit(Temp):
    assert (Temp >= 0), "colder than absolute zero"
    return ((Temp-273)*1.8)+32


print( KelvinToFahrenheit(273) )
print( int(KelvinToFahrenheit(505.78)) )
print( KelvinToFahrenheit(-5) )
