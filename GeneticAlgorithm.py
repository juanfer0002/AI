import random
import operator

'''
POPULATION, total of 20 invidivuals

The best are going to be those who matches more validations, and which fmin is the lowest

Crossover is going to be between 10 invidiuals, over 70%, done on one point
and they cross 1st with 2nd, 3rd with 4th, and so on...

Mutation is going to be over 80%. They can mutate any value greather than 0. 

Punishment if any individual doesn't fit:
a) The sum of the first 2 genotypes must be lesser or equal than 1000
b) The sum of the other 4 genotypes must be lesser or equal than 2000

'''
population = [
    [44, 956, 126, 164, 263, 1447],
    [203, 797, 394, 245, 489, 872],
    [195, 805, 108, 161, 1690, 41],
    [121, 879, 323, 361, 1284, 32],
    [23, 977, 484, 151, 493, 872],
    [19, 981, 265, 425, 1105, 205],
    [289, 711, 52, 372, 185, 1391],
    [173, 827, 208, 294, 112, 1386],
    [69, 931, 33, 388, 770, 809],
    [371, 629, 28, 231, 357, 1384],
    [3, 997, 150, 347, 1226, 277],
    [232, 768, 329, 64, 1379, 228],
    [384, 616, 367, 412, 1208, 13],
    [39, 961, 240, 106, 1241, 413],
    [8, 992, 306, 275, 674, 745],
    [345, 655, 331, 136, 949, 584],
    [291, 709, 474, 448, 143, 935],
    [1, 999, 314, 265, 249, 1172],
    [135, 865, 11, 112, 1041, 836],
    [17, 983, 153, 333, 159, 1355],
]


'''
FUNCTIONS AND RESTRICTIONS
'''

def multiplyAndSumVarsForCoefs(vars, coefs):
    r = 0

    for i in range(0, len(coefs)):
        r += coefs[i] * vars[i]
    # End for

    return r
# End f

def fmin(idv):
    fminCoefs = [3.9, 3.0, 3.6, 4.3, 3.65, 4.35]
    return multiplyAndSumVarsForCoefs(idv, fminCoefs)
# End f

def validateRestriction(idv, coefs, op, compareTo):
    val = multiplyAndSumVarsForCoefs(idv, coefs)
    return op(val, compareTo)
# End validateRestriction

def countValidRestrictions(idv):
    totalValid = 0

    totalValid += 0 | validateRestriction(idv, [4, 4, 0, 0, 0, 0], operator.le, 8800) # Dpto D1
    totalValid += 0 | validateRestriction(idv, [1, 1, 3, 3, 3, 3], operator.le, 8800) # Dpto D2
    totalValid += 0 | validateRestriction(idv, [6, 0, 2, 2, 0, 0], operator.le, 8800) # Dpto E1
    totalValid += 0 | validateRestriction(idv, [0, 2, 0, 0, 3, 3], operator.le, 8800) # Dpto E2
    totalValid += 0 | validateRestriction(idv, [0, 0, 6, 0, 6, 0], operator.le, 8800) # Dpto F1
    totalValid += 0 | validateRestriction(idv, [4, 4, 0, 4, 0, 4], operator.le, 8800) # Dpto F2
    totalValid += 0 | validateRestriction(idv, [0.1, 0.1, 0.5, 0.5, 0.5, 0.5], operator.le, 2400) # Dpto F2
    totalValid += 0 | validateRestriction(idv, [0, 0, 1, 1, 1, 1], operator.eq, 2000) # Dpto F2
    totalValid += 0 | validateRestriction(idv, [1, 1, 0, 0, 0, 0], operator.eq, 1000) # Dpto F2

    return totalValid

# End validateAllRestrictions


'''
GENETIC ALGORITHM
'''

minValue = 0


def orderByMaxValidRestrictionsAndMinValue(population):
    population = []
    population.sort(lambda o1,o2 : abs((a - e) / a))

# End orderByMinValueAndMaxValidRestrictions

def init():
    global minValue
    minValue = 1
    return 0
# End init



init()
print(minValue);