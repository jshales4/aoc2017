#day3.py
def distance(input):
    min=input
    if int(input**.5)%2==1:
        level = int(input**.5)
    else: level = int(input**.5)-1
    for x in range(4):
        axis = level**2 + (level+1)/2 + x*(level+1)
        if min>abs(input-axis):
            min = abs(input-axis)
        if min>abs(axis-min):
            min=abs(axis-min)
    return min+(level-1)/2+1

def isCorner(position):
    if int(position**.5)%2==1:
        level = int(position**.5)
    else: level = int(position**.5)-1
    for x in range(4):
        if position == level**2 + (level+1) + x*(level+1):
            return True
    return False

def main():
    input = 277678
    print(distance(input))
    print(isCorner(13))
    print(isCorner(14))
    print(isCorner(21))
    
        #if min>abs(input-axis):
            #min = abs(input-axis
        #print(min+(level-1)/2+1)
main()