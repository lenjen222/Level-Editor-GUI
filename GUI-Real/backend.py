from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
import json

class Backend(QObject):
    # Signal to notify changes in the selected sprite and grid data
    selectedSpriteChanged = pyqtSignal()
    gridUpdated = pyqtSignal()

    def __init__(self, grid_width=100, grid_height=100):
        super().__init__()
        self.grid_width = grid_width
        self.grid_height = grid_height
        self._selectedSprite = "assets/empty.png"
        self.grid_data = [[self._selectedSprite for _ in range(self.grid_width)] for _ in range(self.grid_height)]

    # Property for the currently selected sprite
    @pyqtProperty(str, notify=selectedSpriteChanged)
    def selectedSprite(self):
        return self._selectedSprite

    @selectedSprite.setter
    def selectedSprite(self, imageSource):
        if self._selectedSprite != imageSource:
            self._selectedSprite = imageSource
            self.selectedSpriteChanged.emit()  # Emit signal to notify change

    # Slot to set the selected sprite
    @pyqtSlot(str)
    def setSelectedSprite(self, imageSource):
        self.selectedSprite = imageSource
        print(f"Selected sprite set to: {imageSource}")

    # Slot to set a sprite on a specific tile
    @pyqtSlot(int)
    def setTileSprite(self, index):
        row = index // self.grid_width
        col = index % self.grid_width
        self.grid_data[row][col] = self._selectedSprite
        self.gridUpdated.emit()  # Emit signal to update UI if needed
        print(f"Tile at index {index} set to sprite {self._selectedSprite}")

    # Slot to retrieve the image source for a specific tile
    @pyqtSlot(int, result=str)
    def getTileImageSource(self, index):
        row = index // self.grid_width
        col = index % self.grid_width
        return self.grid_data[row][col]

    # Clear the level and reset each tile to the default selected sprite
    @pyqtSlot()
    def clearLevel(self):
        self.grid_data = [[self._selectedSprite for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.gridUpdated.emit()
        print("Level cleared.")

    # Save the current grid state to a JSON file
    @pyqtSlot()
    def saveToFile(self):
        with open('level_data.json', 'w') as f:
            json.dump(self.grid_data, f)
        print("Level data saved.")

    # Load the grid state from a JSON file
    @pyqtSlot()
    def loadFromFile(self):
        try:
            with open('level_data.json', 'r') as f:
                self.grid_data = json.load(f)
            self.gridUpdated.emit()  # Emit signal to refresh UI
            print("Level data loaded.")
        except FileNotFoundError:
            print("No saved level data found.")
        except json.JSONDecodeError:
            print("Error decoding level data.")