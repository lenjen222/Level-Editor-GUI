import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QUrl
from backend import Backend

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create the QML application engine
    engine = QQmlApplicationEngine()

    # Create an instance of the Backend class and expose it to QML
    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    # Load the real QML file
    engine.load(QUrl.fromLocalFile('C:/Users/Len/Documents/GitHub/Level-Editor-GUI/MainEntry.qml'))

    # Check if the QML file loaded successfully
    if not engine.rootObjects():
        sys.exit(-1)

    # Execute the application
    sys.exit(app.exec())