import sys
import re

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtWidgets import QApplication, QPlainTextEdit

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)

        self.highlighting_rules = []

        # правило для выделения строк, содержащих две буквы "z" ровно с тремя символами между ними
        pattern = QRegExp("z.{3}z")
        format = QTextCharFormat()
        format.setForeground(QColor("red"))
        format.setFontWeight(QFont.Bold)
        self.highlighting_rules.append((pattern, format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)


class MainWindow(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.highlighter = Highlighter(self.document())

        # задаем шрифт
        font = QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)

        # 4 символа - макс
        self.setTabStopWidth(4 * self.fontMetrics().width(' '))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
