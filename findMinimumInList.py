#! python3

def findMinimum(numberList):
    newMinimum = 0
    
    for i in range(len(numberList)):
        if i == 0:
            newMinimum = numberList[i]
        elif numberList[i] < newMinimum:
            newMinimum = numberList[i]
    return newMinimum

minimum = findMinimum([-880, 231, -235, -654, 180, 856, 407, -345, -390, 428, 987, -967, 
                       303, -61, 697, -290, 430, -692, 896, -225, -669, 439, 265, 424, -549, 
                       -919, -257, -546, 300])
print(minimum)