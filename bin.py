# imports

# this is the bin class
class bin:
    def __init__(self) -> None:
        self.height = 10
        self.length = 10
        self.width = 10
        self.totalVolume = self.height * self.length * self.width
        self.usableVolume = self.totalVolume
        self.strips = [
            {
                "height":self.height,
                "length":self.length,
                "width":self.width,
                "volume":self.height * self.length * self.width
            }
        ]

    # find the appropiate section
    def fillStrip(self,dimensions):
        volume = dimensions["height"] * dimensions["length"] * dimensions["width"]
        rotationA = dimensions
        rotationB = {"height":dimensions["length"],"length":dimensions["height"],"width":dimensions["width"]}
        rotationC = {"height":dimensions["width"],"length":dimensions["height"],"width":dimensions["length"]}
        for index in range(len(self.strips)):
            if self.strips[index]["volume"] <= volume:
                # find if the item can be placed in an orientation that works inside of the bin
        # update self.stips with new strips
        # sort self.strips from smallest to largest on volume
        # based on if the method completed successfully (found and placed a strip) or not, return true or false
