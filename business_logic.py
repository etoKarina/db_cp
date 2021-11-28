import db_module
import datetime
import calendar
from collections import defaultdict


class Restoraunt:

    def __init__(self):
        self.db = db_module.DbModule('db.db')

    def recieve_product(self, product_id, count, date: datetime.date):
        product_ids = set(self.db.get_all_product_id())
        if product_id in product_ids:
            max_id = self.db.get_storage_max_id()
            self.db.new_storage(max_id + 1, count, calendar.timegm(date.utctimetuple()), product_id)
        else:
            print(f'no such product {product_id}')

    def add_product(self, name, type, price, exp_period):
        max_id = self.db.get_product_max_id()
        self.db.new_product(max_id + 1, name, type, price, exp_period)

    def delete_product(self, id):
        self.db.delete_product(id)

    def remove_stall_products(self, date: datetime.datetime):
        timestamp = calendar.timegm(date.utctimetuple())
        ids_to_remove = self.db.get_exp_product(timestamp)
        self.db.delete_storage(ids_to_remove)

    def add_dish(self, name, price, description, dish_product_ids_counts): # [(1 - redis,3 shutki),(2 - repki,4 - shtuki)]
        # проверяем есть ли ну;ные продукты
        # если есть (a,b,c,n) idff (a,b,c,d) = n # (a,b) idff (a,b,c,d) = ()
        product_ids = set(self.db.get_all_product_id())
        if not set(pair[0] for pair in dish_product_ids_counts).difference(product_ids):
            max_id = self.db.get_dish_max_id()
            self.db.new_dish(max_id + 1, name, price, description)
            for product_id, product_count in dish_product_ids_counts:
                self.db.new_consist(max_id+1, product_id, product_count)
        else:
            print(f'no such products in Product list')
        # если нет - ругаемся в консоль

    def delete_dish(self, id):
        self.db.delete_dish(id)
        self.db.delete_consist(id)

    def order(self, dish_ids):
        product_count = defaultdict(int)
        for dish_id in dish_ids:
            product_ids_counts = self.db.get_consist(dish_id)
            for product_id, count in product_ids_counts:
                product_count[product_id]+=count
        # TODO


    def menu_showtime(self):
        print(self.db.get_all_dish())
