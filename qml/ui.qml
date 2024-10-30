import QtQuick 6.7
import QtQuick.Controls 6.7

ApplicationWindow {
    visible: true
    width: 1024
    height: 768

    property color selectedColor: backend.selectedSprite

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
                    backend.setSelectedSprite(colorCode)
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
            color: "white" // This will be updated when loading grid data
            border.color: "lightgrey"
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    backend.setTileSprite(index)
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

    Dialog {
        id: clearDialog
        title: "Confirm Clear"
        modal: true
        width: 300  // Set a fixed width to avoid implicitWidth binding loops
        standardButtons: DialogButtonBox.StandardButton.Ok | DialogButtonBox.StandardButton.Cancel
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
            mapCanvas.model = mapCanvas.model
        }

        onRejected: {
            // No action needed
        }
    }
}