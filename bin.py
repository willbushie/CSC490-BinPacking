# imports
from operator import xor
from cv2 import reduce
from matplotlib import projections
from box import box
import json

import numpy as np
import matplotlib.pyplot as plt
from itertools import product, combinations
from mpl_toolkits.mplot3d import Axes3D
from functools import reduce

# this is the bin class
class bin:
    """
    This class is for the larger bins, which there are infinite. The goal is to place smaller boxes into the least amount of (these) larger bins.
    """
    def __init__(self,height,length,width) -> None:
        self.height = height 
        self.length = length 
        self.width = width 
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
    def fillStrip(self,box):
        """
        This method looks at the unfilled areas (strips) inside of a bin and attempts to place a box inside of the bin.\n 
        If this is accomplished, the bin will update bin.strips, and bin.contains.\n
        This method will return True if the operation has been successfully been completed, else it returns False.
        """
        dimensions = box.getDimensions()
        placed = False
        volume = dimensions["height"] * dimensions["length"] * dimensions["width"]
        rotationA = dimensions
        rotationB = {"height":dimensions["length"],"length":dimensions["height"],"width":dimensions["width"]}
        rotationC = {"height":dimensions["width"],"length":dimensions["height"],"width":dimensions["length"]}
        rotations = [rotationA,rotationB,rotationC]
        
        for i in range(len(self.strips)):
            if placed == False:
                if self.strips[i]["volume"] >= volume:
                    if max([dimensions["height"], dimensions["length"], dimensions["width"]]) <= max([self.strips[i]["length"],self.strips[i]["height"],self.strips[i]["width"]]):
                        for j in range(len(rotations)):
                            if placed is False:
                                if rotations[j]["length"] <= self.strips[i]["length"] and rotations[j]["height"] <= self.strips[i]["height"] and rotations[j]["width"] <= self.strips[i]["width"]:
                                    boxCoordinates = self.createCoordinates(rotations[j]["height"],rotations[j]["length"],rotations[j]["width"])
                                    stripACoordinates = {
                                        "a":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":self.strips[i]["coordinates"]["a"]["y"],"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["b"]["z"])},
                                        "b":{"x":self.strips[i]["coordinates"]["b"]["x"],"y":self.strips[i]["coordinates"]["b"]["y"],"z":self.strips[i]["coordinates"]["b"]["z"]},
                                        "c":{"x":self.strips[i]["coordinates"]["c"]["x"],"y":self.strips[i]["coordinates"]["c"]["y"],"z":self.strips[i]["coordinates"]["c"]["z"]},
                                        "d":{"x":self.strips[i]["coordinates"]["d"]["x"],"y":self.strips[i]["coordinates"]["d"]["y"],"z":(self.strips[i]["coordinates"]["d"]["z"] + boxCoordinates["c"]["z"])},
                                        "e":{"x":self.strips[i]["coordinates"]["e"]["x"],"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["f"]["z"])},
                                        "f":{"x":self.strips[i]["coordinates"]["f"]["x"],"y":self.strips[i]["coordinates"]["f"]["y"],"z":self.strips[i]["coordinates"]["f"]["z"]},
                                        "g":{"x":self.strips[i]["coordinates"]["g"]["x"],"y":self.strips[i]["coordinates"]["g"]["y"],"z":self.strips[i]["coordinates"]["g"]["z"]},
                                        "h":{"x":self.strips[i]["coordinates"]["h"]["x"],"y":self.strips[i]["coordinates"]["h"]["y"],"z":(self.strips[i]["coordinates"]["h"]["z"] + boxCoordinates["g"]["z"])}
                                    }
                                    stripBCoordinates = {
                                        "a":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["a"]["y"],"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "b":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["a"]["y"],"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["c"]["z"])},
                                        "c":{"x":self.strips[i]["coordinates"]["d"]["x"],"y":self.strips[i]["coordinates"]["d"]["y"],"z":(self.strips[i]["coordinates"]["d"]["z"] + boxCoordinates["c"]["z"])},
                                        "d":{"x":self.strips[i]["coordinates"]["d"]["x"],"y":self.strips[i]["coordinates"]["d"]["y"],"z":self.strips[i]["coordinates"]["d"]["z"]},
                                        "e":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]},
                                        "f":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["d"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["c"]["z"])},
                                        "g":{"x":self.strips[i]["coordinates"]["h"]["x"],"y":self.strips[i]["coordinates"]["h"]["y"],"z":(self.strips[i]["coordinates"]["h"]["z"] + boxCoordinates["c"]["z"])},
                                        "h":{"x":self.strips[i]["coordinates"]["h"]["x"],"y":self.strips[i]["coordinates"]["h"]["y"],"z":self.strips[i]["coordinates"]["h"]["z"]}
                                    }
                                    stripCCoordinates = {
                                        "a":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "b":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["f"]["z"])},
                                        "c":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["c"]["x"]),"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["f"]["z"])},
                                        "d":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["c"]["x"]),"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["e"]["y"]),"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "e":{"x":self.strips[i]["coordinates"]["e"]["x"],"y":self.strips[i]["coordinates"]["e"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]},
                                        "f":{"x":self.strips[i]["coordinates"]["e"]["x"],"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["f"]["z"])},
                                        "g":{"x":(self.strips[i]["coordinates"]["e"]["x"] + boxCoordinates["g"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":(self.strips[i]["coordinates"]["e"]["z"] + boxCoordinates["g"]["z"])},
                                        "h":{"x":(self.strips[i]["coordinates"]["e"]["x"] + boxCoordinates["h"]["x"]),"y":self.strips[i]["coordinates"]["e"]["y"],"z":self.strips[i]["coordinates"]["e"]["z"]}
                                    }
                                    # setting coordinates of the box after placement
                                    updatedBoxCoordinates = {
                                        "a":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":self.strips[i]["coordinates"]["a"]["y"],"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "b":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":self.strips[i]["coordinates"]["a"]["y"],"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["g"]["z"])},
                                        "c":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["g"]["x"]),"y":self.strips[i]["coordinates"]["a"]["y"],"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["g"]["z"])},
                                        "d":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["g"]["x"]),"y":self.strips[i]["coordinates"]["a"]["y"],"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "e":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["g"]["y"]),"z":self.strips[i]["coordinates"]["a"]["z"]},
                                        "f":{"x":self.strips[i]["coordinates"]["a"]["x"],"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["g"]["y"]),"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["g"]["z"])},
                                        "g":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["g"]["x"]),"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["g"]["y"]),"z":(self.strips[i]["coordinates"]["a"]["z"] + boxCoordinates["g"]["z"])},
                                        "h":{"x":(self.strips[i]["coordinates"]["a"]["x"] + boxCoordinates["g"]["x"]),"y":(self.strips[i]["coordinates"]["a"]["y"] + boxCoordinates["g"]["y"]),"z":self.strips[i]["coordinates"]["a"]["z"]}
                                    }
                                    box.coordinates = updatedBoxCoordinates
                                    self.contains.append(box)
                                    box.placed = True
                                    self.strips.pop(i)
                                    stripA = self.createStrip(stripACoordinates)
                                    stripB = self.createStrip(stripBCoordinates)
                                    stripC = self.createStrip(stripCCoordinates)
                                    if stripA["volume"] != 0:
                                        self.strips.append(stripA)
                                    if stripB["volume"] != 0:
                                        self.strips.append(stripB)
                                    if stripC["volume"] != 0:
                                        self.strips.append(stripC)
                                    self.usableVolume = self.usableVolume - volume
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
            "h":{"x":length,"y":width,"z":0}
        }
        return coordinates

    def createStrip(self,coordinates):
        """
        This method creates a strip dictionary to be added to the strips inside of the self.strips.\n
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
        print(f"height: {self.height}, length: {self.length}, width: {self.width}, total volume: {self.totalVolume}, usable volume: {self.usableVolume}, # of strips: {len(self.strips)}")
        print(f"cotains ({len(self.contains)}):")
        #for i in range(len(self.contains)):
        #    self.contains[i].display()
        print("strips:")
        for i in range(len(self.strips)):
            print(f"height: {self.strips[i]['height']}, length: {self.strips[i]['length']}, width: {self.strips[i]['width']}, volume: {self.strips[i]['volume']}")
            print(f"coordinates: {self.strips[i]['coordinates']}")
            #pretty = json.dumps(self.strips[i]['coordinates'], indent=4)
            #print(pretty)

    def show3D(self,title):
        """
        This method attempts to show a 3 dimensional view of the filled spaces inside the bin.\n
        This method currently does not work.
        """
        """ # Create axis
        x,y,z = np.indices((9,6,12)) #5,4,3
        boxA = (x < 4) & (y < 3) & (z < 5)
        boxB = (x < 4) & (y > 2) & (z < 5)
        # Create Data
        voxelarray = boxA | boxB
        # Controll Tranperency
        alpha = 0.5
        # Control color
        colors = np.empty(voxelarray.shape, dtype=object)
        #colors = np.empty(voxelarray.shape, dtype=object)
        colors[boxA] = "red"
        colors[boxB] = "blue"
        # Plot figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Voxels is used to customizations of the
        ax.voxels(voxelarray, facecolors=colors, edgecolor='k')
        plt.show() """

        """ # wireframes of two boxes one inside the other
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_aspect("auto")
        ax.set_autoscale_on(True)
        r = [-10, 10]
        for s, e in combinations(np.array(list(product(r,r,r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s,e), color="b")
        #ax.scatter([0],[0],[0],color="g",s=100)
        d = [-2, 2]
        for s, e in combinations(np.array(list(product(d,d,d))), 2):
            if np.sum(np.abs(s-e)) == d[1]-d[0]:
                ax.plot3D(*zip(s,e), color="g")
        plt.show() """

        # prepare some coordinates
        x, y, z = np.indices((9, 6, 12))
        # creation of transparent bin bounds
        transparentBin = (x < self.length) & (y < self.width) & (z < self.height)
        # loop through the strips and create extra
        if len(self.contains) > 1:
            boxes = []
            for i in range(len(self.contains)):
                boxCoordinates = self.contains[i].returnCoordinates()
                xResult = (x >= boxCoordinates["a"]["x"]) & (x < boxCoordinates["g"]["x"])
                yResult = (y >= boxCoordinates["a"]["y"]) & (y < boxCoordinates["g"]["y"])
                zResult = ((z >= boxCoordinates["a"]["z"]) & (z < boxCoordinates["g"]["z"]))
                section = (xResult) & (yResult) & (zResult)
                boxes.append(section)
            voxelsFinal = reduce(lambda x, y: x | y, boxes)
        elif len(self.contains) == 1:
            boxCoordinates = self.contains[0].returnCoordinates()
            xResult = (x >= boxCoordinates["a"]["x"]) & (x < boxCoordinates["g"]["x"])
            yResult = (y >= boxCoordinates["a"]["y"]) & (y < boxCoordinates["g"]["y"])
            zResult = ((z >= boxCoordinates["a"]["z"]) & (z < boxCoordinates["g"]["z"]))
            section = (xResult) & (yResult) & (zResult)
            voxelsFinal = section
        #boxCoordinatesA = self.contains[0].returnCoordinates()
        #boxCoordinatesB = self.contains[1].returnCoordinates()
        #opaque_cubes_1 = (x >= boxCoordinatesA["a"]["x"]) & (x < boxCoordinatesA["g"]["x"]) & (y >= boxCoordinatesA["a"]["y"]) & (y < boxCoordinatesA["g"]["y"]) & ((z >= boxCoordinatesA["a"]["z"]) & (z < boxCoordinatesA["g"]["z"]))
        #opaque_cubes_2 = (x >= boxCoordinatesB["a"]["x"]) & (x < boxCoordinatesB["g"]["x"]) & (y >= boxCoordinatesB["a"]["y"]) & (y < boxCoordinatesB["g"]["y"]) & ((z >= boxCoordinatesB["a"]["z"]) & (z < boxCoordinatesB["g"]["z"])) #((z >= 2) & (z < 7))
        #opaque_cubes_1 = (x - self.contains[0].coordinates["a"]["x"] < 9) & (y - self.contains[0].coordinates["a"]["y"] < 2) & (z - self.contains[0].coordinates["a"]["z"] < 2)
        #opaque_cubes_2 = (x - self.contains[1].coordinates["a"]["x"] < 4) & (y - self.contains[1].coordinates["a"]["y"] < 3) & (z - self.contains[1].coordinates["a"]["z"] < 7)
        #voxelsFinal = opaque_cubes_1 | opaque_cubes_2
        # combine the objects into a single boolean array
        baseBin = transparentBin
        # and plot everything
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.voxels(baseBin, facecolors='white', edgecolor='none', alpha=0.4)
        if len(self.contains) > 0:
            ax.voxels(voxelsFinal, facecolors='red', edgecolor='black', alpha=0.7)
        plt.show()


#test = bin(12,9,6)
#test.fillStrip(box(2,9,2))
#test.fillStrip(box(5,4,3))
#test.fillStrip(box(3,3,3))
#test.fillStrip(box(5,4,3))
#test.fillStrip(box(3,3,3))
#test.fillStrip(box(5,4,3))
#test.fillStrip(box(5,4,3))
#for b in range(len(test.contains)):
#    print(f"coordinates: {test.contains[b].coordinates}")
#test.show3D("testing graph")