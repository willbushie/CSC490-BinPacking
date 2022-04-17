# imports
from box import box
import json

# this is the bin class
class bin:
    """
    This class is for the larger bins, which there are infinite. The goal is to place smaller boxes into the least amount of (these) larger bins.
    """
    def __init__(self,height,length,width) -> None:
        self.height = 12 #height
        self.length = 9 #length
        self.width = 6 #width
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
        
        if placed is False:
            for i in range(len(self.strips)):
                if self.strips[i]["volume"] <= volume:
                    if max([dimensions["height"], dimensions["length"], dimensions["width"]]) <= max([self.strips[i]["length"],self.strips[i]["height"],self.strips[i]["width"]]):
                        if placed is False:
                            for j in range(len(rotations)):
                                if rotations[j]["length"] <= self.strips[i]["length"] and rotations[j]["height"] <= self.strips[i]["height"] and rotations[j]["width"] <= self.strips[i]["width"]:
                                    boxCoordinates = self.createCoordinates(rotations[j]["height"],rotations[j]["length"],rotations[j]["width"])
                                    stripACoordinates = {
                                        "a":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":self.strips[i]["coordinates"]["a"]["y"],"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["b"]["z"])},
                                        "b":{"x":self.strips[i]["coordinates"]["b"]["x"],"y":self.strips[i]["coordinates"]["b"]["y"],"z":self.strips[i]["coordinates"]["b"]["z"]},
                                        "c":{"x":self.strips[i]["coordinates"]["c"]["x"],"y":self.strips[i]["coordinates"]["c"]["y"],"z":self.strips[i]["coordinates"]["c"]["z"]},
                                        "d":{"x":self.strips[i]["coordinates"]["d"]["x"],"y":self.strips[i]["coordinates"]["d"]["y"],"z":(self.strips[i]["coordinates"]["d"]["z"] + boxCoordinates["c"]["z"])},
                                        "e":{"x":self.strips[i]["coordinates"]["e"]["x"],"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["f"]["z"])},
                                        "f":{"x":self.strips[i]["coordinates"]["f"]["x"],"y":self.strips[i]["coordinates"]["f"]["y"],"z":self.strips[i]["coordinates"]["f"]["z"]},
                                        "g":{"x":self.strips[i]["coordinates"]["g"]["x"],"y":self.strips[i]["coordinates"]["g"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]},
                                        "h":{"x":self.strips[i]["coordinates"]["h"]["x"],"y":self.strips[i]["coordinates"]["h"]["y"],"z":(self.strips[i]["coordinates"]["h"]["z"] + boxCoordinates["g"["z"]])},
                                    }
                                    stripBCoordinates = {
                                        "a":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["a"]["y"],"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "b":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["a"]["y"],"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["c"]["z"])},
                                        "c":{"x":self.strips[i]["coordinates"]["d"]["x"],"y":self.strips[i]["coordinates"]["d"]["y"],"z":(self.strips[i]["coordinates"]["d"]["z"] + boxCoordinates["c"]["z"])},
                                        "d":{"x":self.strips[i]["coordinates"]["d"]["x"],"y":self.strips[i]["coordinates"]["d"]["y"],"z":self.strips[i]["coordinates"]["d"]["z"]},
                                        "e":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]},
                                        "f":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["c"]["z"])},
                                        "g":{"x":self.strips[i]["coordinates"]["h"]["x"],"y":self.strips[i]["coordinates"]["h"]["y"],"z":(self.strips[i]["coordinates"]["h"]["z"] + boxCoordinates["c"]["z"])},
                                        "h":{"x":self.strips[i]["coordinates"]["h"]["x"],"y":self.strips[i]["coordinates"]["h"]["y"],"z":self.strips[i]["coordinates"]["h"]["z"]},
                                    }
                                    stripCCoordinates = {
                                        "a":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "b":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["f"]["z"])},
                                        "c":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["c"]["x"]),"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["f"]["z"])},
                                        "d":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["c"]["x"]),"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "e":{"x":self.strips[i]["coordinates"]["e"]["x"],"y":self.strips[i]["coordinates"]["e"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]},
                                        "f":{"x":self.strips[i]["coordinates"]["e"]["x"],"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["f"]["z"])},
                                        "g":{"x":(self.strips[i]["coordinates"]["e"]["x"] + boxCoordinates["g"]["x"]),"y":(self.strips[i]["coordinates"]["e"]["y"] + boxCoordinates["g"]["y"]),"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["g"]["z"])},
                                        "h":{"x":(self.strips[i]["coordinates"]["e"]["x"] + boxCoordinates["h"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]},
                                    }
                                    self.strips.pop(i)
                                    stripA = self.createStrip(stripACoordinates)
                                    stripB = self.createStrip(stripBCoordinates)
                                    stripC = self.createStrip(stripCCoordinates)
                                    self.strips.append(stripA)
                                    self.strips.append(stripB)
                                    self.strips.append(stripC)
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

    def createStrip(coordinates):
        """
        This method creates a strip dictionary to be added to the strips inside of the self.strips.
        It takes coordinates to build the height, lenght, width and volume.
        """
        height = (coordinates["b"]["z"] - coordinates["a"]["z"])
        length = (coordinates["d"]["x"] - coordinates["a"]["x"])
        width = (coordinates["e"]["y"] - coordinates["a"]["y"])
        strip = {
                "height":height,
                "length":length,
                "width":width,
                "volume":(length * width * height),
                "coordinates":coordinates
            }
        return strip


    def display(self):
        """
        This method will nicely print a bin's attributes and its contents.
        """
        print(f"height: {self.height}, length: {self.length}, width: {self.width}, total volume: {self.totalVolume}, usable volume: {self.usableVolume}")
        print(f"contains boxes: {self.contains}")
        print("strips:")
        for i in range(len(self.strips)):
            print(f"height: {self.strips[i]['height']}, length: {self.strips[i]['length']}, width: {self.strips[i]['width']}, volume: {self.strips[i]['volume']}")
            pretty = json.dumps(self.strips[i]['coordinates'], indent=4)
            print(pretty)

    def show3D(self):
        """
        This method attempts to show a 3 dimensional view of the filled spaces inside the bin
        """
        pass