# imports
from bin import bin
from box import box


if __name__ == "__main__":
    # create empty list of bins and a list of boxes with dimensions
    binsA = []
    binsB = []
    binsC = []
    boxesA = []
    boxesB = []
    boxesC = []
    
    # scenario A box creation
    for i in range(2):
        a = box(5,4,3)
        boxesA.append(a)
    for i in range(6):
        a = box(3,3,3)
        boxesA.append(a)
    for i in range(2):
        a = box(6,2,2)
        boxesA.append(a)
    # scenario A box placement

    
    # scenario B box creation
    for i in range(5):
        a = box(5,4,3)
        boxesB.append(a)
    for i in range(10):
        a = box(3,3,3)
        boxesB.append(a)
    for i in range(5):
        a = box(6,2,2)
        boxesB.append(a)
    # scenario B box placement


    # scenario C box creation
    for i in range(12):
        a = box(5,4,3)
        boxesC.append(a)    
    for i in range(12):
        a = box(3,3,3)
        boxesC.append(a)
    for i in range(6):
        a = box(6,2,2)
        boxesC.append(a)
    # scenario C box placement

    """ # testing if the box objects were created properly
    print("boxesA:")
    print(len(boxesA))
    for b in range(len(boxesA)):
        boxesA[b].display()
    print("boxesB:")
    print(len(boxesB))
    for b in range(len(boxesB)):
        boxesB[b].display()
    print("boxesC:")
    print(len(boxesC))
    for b in range(len(boxesC)):
        boxesC[b].display() """