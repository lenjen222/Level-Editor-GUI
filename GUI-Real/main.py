import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from backend import Backend

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

# Create an instance of the Backend class
backend = Backend()

# Expose the backend object to QML
engine.rootContext().setContextProperty('backend', backend)

# Load the QML file
engine.load('ui.qml')

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = LevelEditor()
    editor.show()
    sys.exit(app.exec_())