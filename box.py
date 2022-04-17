class box:
    def __init__(self,height,length,width) -> None:
        self.placed = False
        self.height = height
        self.length = length
        self.width = width
        self.volume = self.height * self.length * self.width
        self.coordinates = self.createCoordinates()
    
    def display(self):
        """
        Display the box's attributes cleanly
        """
        print(f"placed: {self.placed} height: {self.height} length: {self.length} width: {self.width} volume: {self.volume}")
    
    def getDimensions(self):
        """
        This method returns the height, width, and length in a dictionary.
        """
        return {"height":self.height,"length":self.length,"width":self.width}

    def createCoordinates(self):
        """
        Create the coordinate system based on dimensions. These dimensions need to be entered in as listed in the method, or the coordinates will be wrong.
        """
        coordinates = {
            "a":{"x":0,"y":0,"z":0},
            "b":{"x":0,"y":0,"z":self.height},
            "c":{"x":self.length,"y":0,"z":self.height},
            "d":{"x":self.length,"y":0,"z":0},
            "e":{"x":0,"y":self.width,"z":0},
            "f":{"x":0,"y":self.width,"z":self.height},
            "g":{"x":self.length,"y":self.width,"z":self.height},
            "h":{"x":self.length,"y":self.width,"z":0}
        }
        return coordinates

    def returnCoordinates(self):
        return self.coordinates