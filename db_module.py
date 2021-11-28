import sqlite3


class DbModule:

    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_all_products(self):
        """ Получаем все продукты из перечня """
        with self.connection:
            return self.cursor.execute('SELECT * FROM Product').fetchall()

    def new_product(self, id, name, type, price, exp_period):
        """Пополнение перечня ингредиентов """
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO Product (idProduct, pName, pType, pPrice, pExpPeriod)"
                f" VALUES ({id},'{name}','{type}',{price},{exp_period});")

    def delete_product(self, id):
        """Удаление ингридиента """
        with self.connection:
            self.cursor.execute(
                f"DELETE FROM Product  WHERE idProduct={id};")

    def new_storage(self, id, count, date, id_product):
        """Поставки на склад """
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO Storage ( idStorage, sCount, sDate, idProd)"
                f" VALUES ({id},{count},{date},{id_product});")

    def delete_storage(self, ids: list):
        """Удаление продуктов со склада """
        with self.connection:
            self.cursor.execute(
                f"DELETE FROM Storage  WHERE idStorage in ({','.join(str(id) for id in ids)});")

    def get_all_storage(self):
        """ Получаем перечень всего на складе """
        with self.connection:
            return self.cursor.execute('SELECT * FROM Storage').fetchall()

    def new_dish(self, id, name, price, description):
        """Поставки на склад """
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO Dish ( idDish, dName, dPrice, dDescription)"
                f" VALUES ({id},'{name}',{price},'{description}');")

    def delete_dish(self, id):
        """Удаление блюда """
        with self.connection:
            self.cursor.execute(
                f"DELETE FROM Dish  WHERE idDish={id};")

    def get_all_dish(self):
        """ Получаем перечень всех блюд """
        with self.connection:
            return self.cursor.execute('SELECT * FROM Dish').fetchall()

    def new_consist(self, dish, product, count):
        """добавление рецепта """
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO Consists ( idDish, idProduct, cCount)"
                f" VALUES ({dish},{product},{count});")

    def delete_consist(self, id):
        """Удаление рецепта """
        with self.connection:
            self.cursor.execute(
                f"DELETE FROM Consists  WHERE idDish={id};")

    def get_consist(self, id):
        """ Получаем  рецептa """
        with self.connection:
            return self.cursor.execute(f'SELECT idProduct, cCount FROM Consists WHERE idDish={id}').fetchall()

    def get_storage_max_id(self):
        """ Получение максимльного id склада"""
        with self.connection:
            result = self.cursor.execute('SELECT max(idStorage) FROM Storage').fetchall()  # list[tuple]
            return result[0][0] if result[0][0] is not None else 0

    def get_product_max_id(self):
        """ Получение максимльного id продукта"""
        with self.connection:
            result = self.cursor.execute('SELECT max(idProduct) FROM Product').fetchall()  # list[tuple]
            return result[0][0] if result[0][0] is not None else 0

    def get_dish_max_id(self):
        """ Получение максимльного id блюда"""
        with self.connection:
            result = self.cursor.execute('SELECT max(idDish) FROM Dish').fetchall()  # list[tuple]
            return result[0][0] if result[0][0] is not None else 0

    def get_all_product_id(self):
        """ Получение всех id """
        with self.connection:
            result = self.cursor.execute('SELECT idProduct FROM Product').fetchall()  # list[tuple]
            return [row[0] for row in result]  # [[1],[2],[3]]

    def get_exp_product(self, timestamp):
        """ Получение всех id """
        with self.connection:
            result = self.cursor.execute(f"""
select idStorage 
  from Storage s
left join Product p 
  on s.idProd=p.idProduct
where s.sDate + p.pExpPeriod*24*60*60 < {timestamp}
            """).fetchall()  # list[tuple]
            return [row[0] for row in result]  # [[1],[2],[3]]
