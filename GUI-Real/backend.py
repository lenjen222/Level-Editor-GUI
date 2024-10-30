from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
import json

class Backend(QObject):
    # Add a signal to notify changes in the selectedSprite property
    selectedSpriteChanged = pyqtSignal()

    def __init__(self, grid_width=100, grid_height=100):
        super().__init__()
        self.grid_width = grid_width
        self.grid_height = grid_height
        self._selectedSprite = "assets/empty.png"
        self.grid_data = [[self._selectedSprite for _ in range(self.grid_width)] for _ in range(self.grid_height)]

    @pyqtSlot(str)
    def setSelectedSprite(self, imageSource):
        if self._selectedSprite != imageSource:
            self._selectedSprite = imageSource
            self.selectedSpriteChanged.emit()  # Emit the change notification signal
        print(f"Selected sprite set to: {imageSource}")

    @pyqtProperty(str, notify=selectedSpriteChanged)  # Mark this property as NOTIFYable
    def selectedSprite(self):
        return self._selectedSprite

    @pyqtSlot(int)
    def setTileSprite(self, index):
        row = index // self.grid_width
        col = index % self.grid_width
        self.grid_data[row][col] = self._selectedSprite
        print(f"Tile at index {index} set to sprite {self._selectedSprite}")

    @pyqtSlot(int, result=str)
    def getTileImageSource(self, index):
        row = index // self.grid_width
        col = index % self.grid_width
        return self.grid_data[row][col]

    @pyqtSlot()
    def clearLevel(self):
        self.grid_data = [[self._selectedSprite for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        print("Level cleared.")
        self.selectedSpriteChanged.emit()

    @pyqtSlot()
    def saveToFile(self):
        with open('level_data.json', 'w') as f:
            json.dump(self.grid_data, f)
        print("Level data saved.")

    @pyqtSlot()
    def loadFromFile(self):
        try:
            with open('level_data.json', 'r') as f:
                self.grid_data = json.load(f)
            print("Level data loaded.")
            self.selectedSpriteChanged.emit()
        except FileNotFoundError:
            print("No saved level data found.")
        except json.JSONDecodeError:
            print("Error decoding level data.")