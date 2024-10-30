import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QUrl
from backend import Backend

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Instantiate the backend and set it up in the QML context
    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    # Load the QML file
    engine.load(QUrl.fromLocalFile('qml/ui.qml'))

    # Check if the QML loaded correctly
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())