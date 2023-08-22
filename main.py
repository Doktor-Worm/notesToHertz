notes = ["df5","bf4","gf4","ef4","gf4","bf4","df5","bf4","gf4","ef4","gf4","bf4","gf4","b4","ef4","gf4","f4","ef4","df4"]
hertz = []
alphabet = ['c','df','d','ef','e','f','gf','g','af','a','bf','b']
def toSemi(xx):
    semis = 0
    if '5' in xx:
        semis += 12
    subString = xx[0:2:1]
    incrementor = 0
    for i in alphabet:
        if subString == i:
            semis+= incrementor
            incrementor = 0
        else:
            incrementor +=1
    return semis


def noteToHertz(ff):
    semitones = toSemi(ff)
    exponent = (semitones-9)/12
    exponentDone = 2**exponent
    hertz = exponentDone*440

    return hertz


for i in notes:
    hertz.append(noteToHertz(i))

print(hertz)

