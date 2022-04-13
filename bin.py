# imports

# this is the bin class
class bin:
    """
    This class is for the larger bins, which there are infinite. The goal is to place smaller boxes into the least amount of (these) larger bins.
    """
    def __init__(self,height,length,width) -> None:
        self.height = 5 #height
        self.length = 5 #length
        self.width = 5 #width
        self.totalVolume = self.height * self.length * self.width
        self.usableVolume = self.totalVolume
        self.contains = []
        self.strips = [
            {
                "height":self.height,
                "length":self.length,
                "width":self.width,
                "volume":(self.height * self.length * self.width),
                "coordinates":self.createCoordinates(self.height,self.length,self.width)
            }
        ]

    # find the appropiate section
    def fillStrip(self,dimensions):
        """
        This method looks at the unfilled areas (strips) inside of a bin and attempts to place a box inside of the bin.\n 
        If this is accomplished, the bin will update bin.strips, and bin.contains.\n
        This method will return True if the operation has been successfully been completed, else it returns False.
        """
        placed = False
        volume = dimensions["height"] * dimensions["length"] * dimensions["width"]
        rotationA = dimensions
        rotationB = {"height":dimensions["length"],"length":dimensions["height"],"width":dimensions["width"]}
        rotationC = {"height":dimensions["width"],"length":dimensions["height"],"width":dimensions["length"]}
        rotations = [rotationA,rotationB,rotationC]
        for i in range(len(self.strips)):
            if self.strips[i]["volume"] <= volume:
                if max([dimensions["height"], dimensions["length"], dimensions["width"]]) <= max([self.strips[i]["length"],self.strips[i]["height"],self.strips[i]["width"]]):
                    # how is the item placed?
                    # update self.stips with new strips
                    
                    self.strips.sort(key=lambda item: item.get("volume"))
                    placed = True
        # based on if the method completed successfully (found and placed a strip) or not, return true or false
        return placed

    def createCoordinates(self,height,length,width):
        """
        Create the coordinate system based on dimensions. These dimensions need to be entered in as listed in the method, or the coordinates will be wrong.
        """
        coordinates = {
            "a":{"x":0,"y":0,"z":0},
            "b":{"x":0,"y":0,"z":height},
            "c":{"x":length,"y":0,"z":height},
            "d":{"x":length,"y":0,"z":0},
            "e":{"x":0,"y":width,"z":0},
            "f":{"x":0,"y":width,"z":height},
            "g":{"x":length,"y":width,"z":height},
            "h":{"x":length,"y":width,"z":0},
        }
        return coordinates
