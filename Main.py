from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QMessageBox
import Quran

# TODO add the font in data

font_main = QFont("KFGQPC HAFS Uthmanic Script", 20)
font_second = QFont("Calibri", 14)
font_third = QFont("Calibri", 14)
color1 = 'lightgray'
color2 = 'white'

gui_sura_list = []
sld_last_value = 0
selected_sura_list = []
selected_sura_name = 'الفاتحة'
selected_sura_number = 1

besmAlah = ' بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ '



class Aya(QtWidgets.QListWidgetItem):
    def __init__(self, text, number, colorInt, align):
        super().__init__()
        self.text = text
        self.number = number
        self.inSura = selected_sura_name
        self.set_text(text, number)
        self.set_color(colorInt)
        self.setTextAlignment(align)

    def set_color(self, colorInt):
        if colorInt == 1:
            self.setBackground(QColor(color1))
        elif colorInt == 0:
            self.setBackground(QColor(color2))

    def set_text(self, text, number):
        if text == besmAlah:
            self.setText(self.text)
        else:
            self.setText(self.text + f' ({number})')


class QuranApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # UI DESIGN
        self.resize(800, 600)
        self.setWindowTitle('Quran App')
        self.root = QtWidgets.QWidget(self)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.root)
        self.horizontalLayoutTop = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBottom = QtWidgets.QHBoxLayout()

        self.btnSettings = QtWidgets.QPushButton(self.root)
        self.btnSettings.setText('|||')
        self.btnSettings.setFont(font_second)
        self.horizontalLayoutTop.addWidget(self.btnSettings)

        self.sld = QtWidgets.QSlider(Qt.Horizontal, self.root)
        self.sld.setValue(20)
        self.sld.setRange(15, 40)
        self.horizontalLayoutTop.addWidget(self.sld)

        self.btnExit = QtWidgets.QPushButton(self.root)
        self.btnExit.setText('خروج')
        self.btnExit.setFont(font_second)
        self.horizontalLayoutTop.addWidget(self.btnExit)  # ADDING

        self.verticalLayout.addLayout(self.horizontalLayoutTop)  # END OF TOP LAYOUT

        self.listWidget = QtWidgets.QListWidget(self.root)
        # self.listWidget.setSpacing(5)
        self.listWidget.setWordWrap(True)
        self.listWidget.setFont(font_main)

        self.verticalLayout.addWidget(self.listWidget)  # END OF CENTER LAYOUT

        self.btnNext = QtWidgets.QPushButton(self.root)
        self.btnNext.setText('السورة التالية')
        self.btnNext.setFont(font_second)
        self.horizontalLayoutBottom.addWidget(self.btnNext)  # ADDING

        self.cb = QtWidgets.QComboBox()
        self.cb.setFont(font_third)
        self.cb.addItems(Quran.suras_names)
        self.cb.removeItem(0)
        self.cb.setCurrentIndex(0)
        self.horizontalLayoutBottom.addWidget(self.cb)  # ADDING

        self.btnPrev = QtWidgets.QPushButton(self.root)
        self.btnPrev.setText('السورة السابقة')
        self.btnPrev.setFont(font_second)
        self.horizontalLayoutBottom.addWidget(self.btnPrev)  # ADDING

        self.verticalLayout.addLayout(self.horizontalLayoutBottom)  # END OF BOTTOM LAYOUT

        self.setCentralWidget(self.root)  # ADDING Everything

        # BINDING EVENTS
        self.btnNext.clicked.connect(self.next_sura)
        self.btnPrev.clicked.connect(self.prev_sura)
        self.btnExit.clicked.connect(exit_app)
        self.cb.currentTextChanged.connect(self.sura_update)
        self.sld.valueChanged.connect(self.update_slider)
        self.listWidget.itemClicked.connect(aya_clicked)

    # FUNCTIONS
    def show_sura(self):
        global selected_sura_list
        gui_sura_list.clear()
        self.listWidget.clear()
        self.listWidget.scrollToTop()
        self.addBesmAlah(self.cb.currentText())
        z = 1
        for i in selected_sura_list:
            x = selected_sura_list.index(i) % 2
            self.addAya(i, x, z)
            z += 1

    def sura_changed(self):
        global selected_sura_list, selected_sura_number, selected_sura_name
        print('sura changed')
        selected_sura_name = self.cb.currentText()
        selected_sura_list = Quran.get_sura(selected_sura_name)
        selected_sura_number = Quran.get_sura_number(selected_sura_name)

    def addAya(self, item, colorInt=1, ayatCounter=0):
        lbl = Aya(item, ayatCounter, colorInt, QtCore.Qt.AlignRight)
        gui_sura_list.append(lbl)
        self.listWidget.addItem(lbl)

    def addBesmAlah(self, sura):
        if sura != 'التوبة' and sura != 'الفاتحة':
            lbl = Aya(besmAlah, 0, 1, QtCore.Qt.AlignCenter)
            gui_sura_list.append(lbl)
            self.listWidget.addItem(lbl)

    def sura_update(self):
        self.sura_changed()
        self.show_sura()
        self.update_slider()

    def next_sura(self):
        if self.cb.currentIndex() != 113:
            self.cb.setCurrentIndex(self.cb.currentIndex() + 1)
            self.sura_update()
        else:
            self.cb.setCurrentIndex(0)
            self.sura_update()

    def prev_sura(self):
        if self.cb.currentIndex() != 0:
            self.cb.setCurrentIndex(self.cb.currentIndex() - 1)
            self.sura_update()
        else:
            self.cb.setCurrentIndex(113)
            self.sura_update()

    def sura_info(self):
        info = Quran.get_sura_info(self.cb.currentText())
        print(info)

    def update_slider(self):
        global sld_last_value
        sld_last_value = self.sld.value()
        for i in gui_sura_list:
            i.setFont(QFont("KFGQPC HAFS Uthmanic Script", sld_last_value))



window:QuranApp

# MAIN FUNCTION
def main():
    # STYLE
    app = QtWidgets.QApplication([])
    app.setStyle('WindowsVista')
    palette = QPalette()
    palette.setColor(QPalette.Background, Qt.lightGray)
    app.setPalette(palette)
    app.setStyleSheet("QPushButton { padding: 7px; } QComboBox { padding: 5px; }")

    # APP START
    global window
    window = QuranApp()
    window.sura_update()  # Show first sura

    # APP LOOP
    window.show()  # Show a window
    app.exec_()  # Run the app


def aya_clicked(aya: Aya):
    print(aya.number, aya.inSura)


def exit_app():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Are you sure?")
    msg.setWindowTitle("Exit App")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    i = msg.exec_()
    if i == 1024:
        QCoreApplication.quit()


if __name__ == '__main__':
    main()
