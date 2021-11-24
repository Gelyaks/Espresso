import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.data()

    def data(self):
        self.bd()
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        view = self.tableView
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)


    def bd(self):
        conn = sqlite3.connect('coffee.sqlite')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS coffee(
            ID INT PRIMARY KEY,
            сорт TEXT,
            обжарка TEXT,
            молотый_зерна TEXT,
            вкус TEXT,
            цена TEXT,
            объем TEXT);""")
        conn.commit()

        zap = [(1, 'арабика', 'светлая', 'молотый', 'вкусный', '200 рублей', '500г'),
               (2, 'арабика', 'темная', 'зерна', 'с горчинкой', '300 рублей', '700г'),
               (3, 'робуста', 'средняя', 'молотый', 'ореховый', '400 рублей', '800г'),
               (4, 'либерика', 'высшая', 'зерна', 'горький', '600 рублей', '700г'),
               (5, 'робуста', 'темная', 'молотый', 'лимонный', '500 рублей', '400г'),
               (6, 'арабика', 'средняя', 'зерна', 'молочный', '470 рублей', '800г'),
               (7, 'робуста', 'высшая', 'молотый', 'кислый', '560 рублей', '700г'),
               (8, 'арабика', 'темная', 'молотый', 'ореховый', '250 рублей', '300г'),
               (9, 'либерика', 'темная', 'молотый', 'лимонный с горчинкой', '800 рублей', '1кг'),
               (10, 'робуста', 'светлая', 'зерна', 'орехово-молочный', '350 рублей', '400г'),
               (11, 'арабика', 'средняя', 'молотый', 'горько-сладкий', '550 рублей', '700г'),
               (12, 'робуста', 'высшая', 'зерна', 'кисло-сладкий', '500 рублей', '400г'),
               (13, 'арабика', 'средняя', 'молотый', 'винный', '600 рублей', '400г'),
               (14, 'либерика', 'светлая', 'молотый', 'орехово-горький', '590 рублей', '400г')]
        cur.executemany("INSERT OR IGNORE INTO coffee VALUES(?, ?, ?, ?, ?, ?, ?);", zap)
        conn.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
