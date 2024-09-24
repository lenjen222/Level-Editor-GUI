from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty

class Backend(QObject):
    # Signals to communicate with QML if needed
    colorSelected = pyqtSignal(str)
    tileSelected = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._selectedColor = "white"
        # Initialize the grid data with default color "white"
        self.grid_data = [["white" for _ in range(100)] for _ in range(100)]  # Example grid size

    # Property to get and set the selected color
    @pyqtProperty(str)
    def selectedColor(self):
        return self._selectedColor

    @selectedColor.setter
    def selectedColor(self, value):
        self._selectedColor = value

    # Slot to set the selected color from QML
    @pyqtSlot(str)
    def setSelectedColor(self, color):
        self.selectedColor = color
        print(f"Selected color set to: {color}")

    #slot to handle to clear level pop up
    @pyqtSlot()
    def clearLevel(self):
        # Reset grid_data to default color ("white")
        self.grid_data = [["white" for _ in range(100)] for _ in range(100)]
        print("Level cleared.")

    @pyqtSlot(int, result=str)
    def getTileColor(self, index):
        row = index // 100
        col = index % 100
        return self.grid_data[row][col]

    # Slot to set the color of a tile based on index
    @pyqtSlot(int)
    def setTileColor(self, index):
        # Calculate row and column from index
        row = index // 100  # Assuming grid width is 100
        col = index % 100
        self.grid_data[row][col] = self.selectedColor
        print(f"Tile at index {index} set to color {self.selectedColor}")

    # Slot to save the grid data to a file
    @pyqtSlot()
    def saveToFile(self):
        with open('level_data.txt', 'w') as f:
            for row in self.grid_data:
                f.write(" ".join(row) + "\n")
        print("Level data saved.")

    # Slot to load the grid data from a file
    @pyqtSlot()
    def loadFromFile(self):
        with open('level_data.txt', 'r') as f:
            for row_idx, line in enumerate(f):
                colors = line.strip().split()
                for col_idx, color in enumerate(colors):
                    self.grid_data[row_idx][col_idx] = color
        print("Level data loaded.")