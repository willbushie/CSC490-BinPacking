# imports
from bin import bin
from box import box

def fillBins(boxes,height=12,length=9,width=6,scenario="Blank"):
    """
    This method will fill bins of specified size when passed a list of boxes.\n
    Needs height, length, and width, if no values are provided, they will be 12, 9, 6.
    """
    bins = [bin(height,length,width)]
    while(len(boxes) > 0):
        for i in range(len(bins)):
            if len(boxes) != 0:
                if bins[i].fillStrip(boxes[0]) == True:
                    boxes.pop(0)
                elif bins[i].fillStrip(boxes[0]) == False and (len(bins)-1 > i):
                    i += 1
                elif bins[i].fillStrip(boxes[0]) == False and (len(bins)-1 == i):
                    bins.append(bin(height,length,width))
                    break
                #print(f"running... {len(boxes)}")
    #print(f"total bins used: {len(binsB)}")
    for j in range(len(bins)):
        #print(f"total boxes left: {len(boxes)}")
        bins[j].display() # display bin attributes
        #bins[j].show3D(f"Bin {j} of {scenario}") # show 3D figure of bin and its contents

if __name__ == "__main__":
    
    # scenario A bin filling - passed, 1 bin used
    print("\n========== SCENARIO A ==========")
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
    fillBins(boxesA,scenario="A")        
    
    # scenario B bin filling - passed, 2 bins used
    print("\n========== SCENARIO B ==========")
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
    fillBins(boxesB,scenario="B")


    # scenario C bin filling - passed, 3 bins used
    print("\n========== SCENARIO C ==========")
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
    fillBins(boxesC,scenario="C")