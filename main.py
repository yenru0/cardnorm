from PySide2.QtWidgets import QApplication

import sys

from ui.main import Main

__version__ = "0.1"

if __name__ == '__main__':
    app = QApplication(sys.argv)

    runner = Main()
    runner.show()
    

    sys.exit(app.exec_())