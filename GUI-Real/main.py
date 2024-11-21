import sys
import os
import PyQt6
from PyQt6.QtCore import QUrl, QDir
from PyQt6.QtWidgets import *
from PyQt6.QtQml import *
from backend import Backend

if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    #added to import path
    qml_dir = os.path.join(os.path.dirname(__file__), "../UntitledProject")
    engine.addImportPath(QDir(qml_dir).absolutePath())

    # Create backend and expose to QML
    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    # Load the QML file
    engine.load(QUrl.fromLocalFile("UntitledProject/UntitledProjectContent/App.qml"))
    

    # Check if QML loaded correctly
    if not engine.rootObjects():
        print("failed to load QML file!")
        sys.exit(-1)
    else:
        print("file loaded successfully")

    # Execute application
    sys.exit(app.exec())