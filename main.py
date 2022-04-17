# imports
from bin import bin
from box import box




if __name__ == "__main__":
    
    """ # testing
    print("\n\ncreating bin and box")
    binn = bin(12,9,6)
    boxx = box(5,4,3)
    print("dispalying bin before any placenemnts")
    binn.display()
    print("attempting to place one box inside of bin")
    binn.fillStrip(boxx.getDimensions())
    print("displaying bin after placement")
    binn.display()
    print("attempting to place second box inside of bin")
    binn.fillStrip(boxx.getDimensions())
    print("displaying bin after second placement")
    binn.display()
    print("attempting to place third box inside of bin")
    binn.fillStrip(boxx.getDimensions())
    print("displaying bin after third placement")
    binn.display() """


    # create empty list of bins and a list of boxes with dimensions
    """ # scenario A box creation - passed, one bin used
    binsA = [bin(12,9,6)]
    boxesA = []
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
    while(len(boxesC) > 0):
        for i in range(len(binsC)):
            if len(boxesC) != 0:
                if binsC[i].fillStrip(boxesC[0]) == True:
                    boxesC.pop(0)
                elif binsC[i].fillStrip(boxesC[0]) == False and (len(binsC)-1 > i):
                    i += 1
                elif binsC[i].fillStrip(boxesC[0]) == False and (len(binsC)-1 == i):
                    binsC.append(bin(12,9,6))
                    break
                #print(f"running... {len(boxesC)}")
    #print(f"total bins used: {len(binsB)}")
    for j in range(len(binsC)):
        #print(f"total boxes left: {len(boxesC)}")
        binsC[j].display() """
        
    
    """ # scenario B box creation - passed, 3 boxes used
    binsB = [bin(12,9,6)]
    boxesB = []
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
    while(len(boxesC) > 0):
        for i in range(len(binsC)):
            if len(boxesC) != 0:
                if binsC[i].fillStrip(boxesC[0]) == True:
                    boxesC.pop(0)
                elif binsC[i].fillStrip(boxesC[0]) == False and (len(binsC)-1 > i):
                    i += 1
                elif binsC[i].fillStrip(boxesC[0]) == False and (len(binsC)-1 == i):
                    binsC.append(bin(12,9,6))
                    break
                #print(f"running... {len(boxesC)}")
    #print(f"total bins used: {len(binsB)}")
    for j in range(len(binsC)):
        #print(f"total boxes left: {len(boxesC)}")
        binsC[j].display() """



    """ # scenario C box creation - passed, 3 boxes filled
    binsC = [bin(12,9,6)]
    boxesC = []
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
    while(len(boxesC) > 0):
        for i in range(len(binsC)):
            if len(boxesC) != 0:
                if binsC[i].fillStrip(boxesC[0]) == True:
                    boxesC.pop(0)
                elif binsC[i].fillStrip(boxesC[0]) == False and (len(binsC)-1 > i):
                    i += 1
                elif binsC[i].fillStrip(boxesC[0]) == False and (len(binsC)-1 == i):
                    binsC.append(bin(12,9,6))
                    break
                #print(f"running... {len(boxesC)}")
    #print(f"total bins used: {len(binsB)}")
    for j in range(len(binsC)):
        #print(f"total boxes left: {len(boxesC)}")
        binsC[j].display() """

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