class box:
    def __init__(self,height,length,width) -> None:
        self.placed = False
        self.height = height
        self.length = length
        self.width = width
        self.volume = self.height * self.length * self.width
    
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