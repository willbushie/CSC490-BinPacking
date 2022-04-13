# imports

# this is the bin class
class bin:
    def __init__(self) -> None:
        self.height = 10
        self.length = 10
        self.width = 10
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
        volume = dimensions["height"] * dimensions["length"] * dimensions["width"]
        rotationA = dimensions
        rotationB = {"height":dimensions["length"],"length":dimensions["height"],"width":dimensions["width"]}
        rotationC = {"height":dimensions["width"],"length":dimensions["height"],"width":dimensions["length"]}
        rotations = [rotationA,rotationB,rotationC]
        for i in range(len(self.strips)):
            if self.strips[i]["volume"] <= volume:
                if max([dimensions["height"], dimensions["length"], dimensions["width"]]) <= max([self.strips[i]["length"],self.strips[i]["height"],self.strips[i]["width"]]):
                    pass
        # update self.stips with new strips
        # sort self.strips from smallest to largest on volume
        # based on if the method completed successfully (found and placed a strip) or not, return true or false

    # create the coordinate system based on dimensions
    def createCoordinates(self,height,length,width):
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
