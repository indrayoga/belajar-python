import sys

def convertToFahrenheit(degreesCelcius):
    return degreesCelcius * (9/5) + 32

def convertToCelcius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5/9)

if(sys.argv[1]=='celcius'):
    print(str(convertToCelcius(int(sys.argv[2]))))
else:
    print(convertToFahrenheit(int(sys.argv[2])))