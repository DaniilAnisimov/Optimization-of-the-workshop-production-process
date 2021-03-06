import sys
from PyQt5.QtWidgets import *
import Catalog, Orders, New_product, Basket, Warehouse, Categories, Tools, Work, Сlient
from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Мастерская')

        self.about_action_program = QAction()
        self.about_action_program.setText("О программе")
        self.about_action_program.triggered.connect(self.about_program_show)
        self.menuBar.addAction(self.about_action_program)

        self.about_action_help = QAction()
        self.about_action_help.setText("Помощь")
        self.about_action_help.triggered.connect(self.help_show)
        self.menuBar.addAction(self.about_action_help)

        self.about_program = AboutProgram()
        self.help = Help()

        self.initUI()

    def initUI(self):
        self.tabWidget.removeTab(0)
        self.tabWidget.removeTab(0)
        self.tabWidget.addTab(Catalog.Catalog(), "Каталог")
        self.tabWidget.addTab(Orders.Orders(), "Заказы")
        self.tabWidget.addTab(New_product.NewProduct(), "Новое изделие")
        self.tabWidget.addTab(Basket.ShoppingCart(), "Корзина")
        self.tabWidget.addTab(Warehouse.Warehouse(), "Склад")
        self.tabWidget.addTab(Categories.Categories(), "Категории")
        self.tabWidget.addTab(Tools.Tools(), "Инструменты ")
        self.tabWidget.addTab(Work.Work(), "Работа")
        self.tabWidget.addTab(Сlient.Client(), "Клиенты")

    def about_program_show(self):
        self.about_program.show()

    def help_show(self):
        self.help.show()


class AboutProgram(QWidget):
    def __init__(self):
        super(AboutProgram, self).__init__()
        self.setWindowTitle("О программе")
        self.setLayout(QVBoxLayout(self))
        self.info = QTextEdit(self)
        self.info.setText("Данная программа создана для оптимизации производственного процесса малой мастерской. \n"
                          "Данная программа подходит к любому небольшому производству, начиная от кондитерских \n"
                          "заканчивая ремонтными мастерскими. Для всех тех кто начинает с закупки сырья, \n"
                          " работая инструментами и вкладывает свой труд.")
        self.layout().addWidget(self.info)


class Help(QWidget):
    def __init__(self):
        super(Help, self).__init__()
        self.setWindowTitle("Помощь")
        self.setLayout(QVBoxLayout(self))
        self.info = QTextEdit(self)
        self.info.setText("1) Каталог\n "
                          "В каталоге вы можете выбрать готовые изделия, узнать его габариты, цену, \n"
                          "а так же посмотреть фото продукта. Для поиска по названию присутствует поисковик, \n"
                          "регистр учитывается!!! \n "
                          "2) Заказы \n"
                          "В этом окне вы можете посмотреть текущие заказы \n"
                          "или завершенные, если выбрать соответствующий раздел. Можно добавлять новые заказы, \n"
                          "завершать, а также пускать их в производство. Мастер выставляет дату сдачи заказа, \n"
                          "когда заказ находится в работе или в ожидании, он горит зелёным, если до даты сдачи \n"
                          "осталось 3 или менее дней заказ загорится жёлтым, если дата сдачи прошла, он \n"
                          "загорится красным. При запуске в производство, материалы заказа автоматически \n"
                          "спишутся со склада, если материалов на складе не хватает они будут автоматически \n"
                          "отабражены в корзине. Инструменты используемые в работе будут амортизированы, \n"
                          "при израсходовании своего ресурса будут добавлены в корзину. \n"
                          "3) Новое изделие \n "
                          "В этом окне мастер создаёт новые изделия, вносит материалы, которые будут затрачены \n"
                          "на него. Так же можно добавить фотографию продукта, установить габариты, указать \n"
                          "работы производимые в отношении этого продукта, и инструменты, которые будут\n"
                          "использованы для работы. Пометка - форматы доступные для фото: png, jpeg.\n"
                          "4) Корзина\n"
                          "В корзине отображаются материалы которые нужно закупить (В верхней таблице),\n"
                          "в нижней указаны инструменты которые израсходовали свой ресурс и нуждаются в \n"
                          "обновлении. Каждую из таблиц можно сохранить в таблицах Excel и в \n"
                          "дальнейшем распечатать. \n"
                          "5) Склад\n "
                          "На складе находятся материалы. Для удобного поиска присутствуют категории и\n"
                          "подстрока для поиска. Если вы хотиите найти, к примеру только материалы \n"
                          "относящиеся только к пиломатериалам, вам нужно просто выбрать соответствующую\n"
                          "категорию. Для поиска по названию присутствует поисковик, регистр учитывается!!!\n"
                          "Вы можете редактировать, добавлять и попалнять материалы.Добавление - создание\n"
                          "нового материала в бд (базе данных), когда как пополнение - добавление к уже\n"
                          "существующим. Пометка - при пополнении материалов, если они присутствуют в\n"
                          "карзине, они спишутся от туда автоматически. \n"
                          "6) Категории\n"
                          "Существуют для более удобного поиска в складе, группируют материалы.\n"
                          "7) Инструменты\n"
                          "В окне можно добавлять, редактировать и заменять на новые инструменты,\n"
                          "в таблице вы можете увидеть информацию о инструменте. Кол-во операций - кол-во\n"
                          "одинаковых операций который может произвести инструмент, к примеру лобзик имеет\n"
                          "кол-во операций = 10000, а единицы измерения = мото часы (в сокращении м.ч), =>\n"
                          "лобзик может выработать 10000 мото часов до израсходования своего ресурса,\n"
                          "после чего он спишется в карзину. Амортизация - стоимость одной операции (В рублях)\n"
                          "Инвентарный номер - номер который вы можете присвоить инструменту для более\n"
                          "лёгкого поиска. Мощность Вт - мощность инструмента, может равняться 0,\n"
                          "если инструмент не электрический. \n"
                          "8) Работа \n"
                          "Здесь можно добавить новые процессы работы. Пометка: расчет стоимости за\n"
                          "произведёную операцию, расчитывается в рублях за единицу измерения.\n"
                          "9) Клиенты\n"
                          "Для того чтобы не потерять свои контакты вы можете заполнить информацию о\n"
                          "каждом клиенте, ФИО, телефон, Email. Добавление клиентов обязательно, т.к\n"
                          "заказы привязываются к клиентам. \n"
                          "P.s: Все вопросы относящиеся к работе программы, идеи для расширения,\n"
                          "или модернизации, критику присылать на почтовый ящик: daniilanisimov2005@yandex.com. ")
        self.layout().addWidget(self.info)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
