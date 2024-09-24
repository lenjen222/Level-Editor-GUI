import QtQuick 6.7
import QtQuick.Controls 6.7

ApplicationWindow {
    visible: true
    width: 1024
    height: 768

    // Use the backend's selectedColor property
    property color selectedColor: backend.selectedColor

    // Palette for color selection
    GridView {
        id: paletteView
        width: parent.width
        height: 100
        cellWidth: 50
        cellHeight: 50
        model: ListModel {
            ListElement { name: "Grey"; colorCode: "grey" }
            ListElement { name: "Red"; colorCode: "red" }
            // Add more colors as needed
        }
        delegate: Rectangle {
            width: 40
            height: 40
            color: colorCode
            border.color: "black"
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // Call the backend method to set the selected color
                    backend.setSelectedColor(colorCode)
                }
            }
        }
    }

    // Map Canvas where the tiles are placed
    GridView {
        id: mapCanvas
        anchors.top: paletteView.bottom
        width: parent.width
        height: parent.height - paletteView.height
        cellWidth: 20
        cellHeight: 20
        model: 100 * 100  // Example grid size, 100x100 tiles
        delegate: Rectangle {
            width: 20
            height: 20
            // Bind the color of the tile to the backend grid data (additional work needed here)
            color: "white" // This will be updated when loading grid data
            border.color: "lightgrey"
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    // Call the backend method to set the tile color
                    backend.setTileColor(index)
                }
            }
        }
    }

   
    Button {
        text: "Save Level"
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        onClicked: {
            backend.saveToFile()
        }
    }

    Button {
        text: "Load Level"
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        onClicked: {
            backend.loadFromFile()
        }
    }
    // pop up dialogue for the clear level button
        Dialog {
        id: clearDialog
        title: "Confirm Clear"
        modal: true
        standardButtons: Dialog.Ok | Dialog.Cancel
        visible: false

        contentItem: Column {
            spacing: 10
            Text {
                text: "Are you sure you want to clear the whole level?"
                wrapMode: Text.WordWrap
            }
        }

        onAccepted: {
            backend.clearLevel()
            // Refresh the GridView
            mapCanvas.model = mapCanvas.model
        }

        onRejected: {
            // No action needed
        }
    }
}