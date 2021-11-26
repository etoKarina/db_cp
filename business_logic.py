import db_module
import datetime
import calendar


class Restoraunt:

    def __init__(self):
        self.db = db_module.DbModule('db.db')

    def recieve_product(self, product_id: object, count: object, date: object) -> object:
        product_ids =set(self.db.get_all_product_id())
        if  product_id in product_ids:
            max_id = self.db.get_storage_max_id()
            self.db.new_storage(max_id + 1, count, calendar.timegm(date.utctimetuple()), product_id)
        else:
            print(f'no such product {product_id}')

    def add_product(self, name, type, price, exp_period):
        max_id = self.db.get_product_max_id()
        self.db.new_product(max_id + 1, name, type, price, exp_period)

    def delete_product(self, id):
        self.db.delete_product(id)


    def remove_stall_products (self, date: datetime.datetime ):
        timestamp = calendar.timegm(date.utctimetuple())
        ids_to_remove=self.db.get_exp_product(timestamp)
        self.db.delete_storage(ids_to_remove)