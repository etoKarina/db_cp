import db_module
import business_logic
import datetime

if __name__ == "__main__":
    r = business_logic.Restoraunt()
    db = db_module.DbModule('db.db')

    # r.add_product('Seledka', 'riba', 70, 15)
    # r.add_product('Petryshka', 'speciya', 5, 360)
    # r.add_product('Mayones', 'souse', 50, 200)
    # r.add_product('Svekla', 'ovosh', 20, 15)
    # r.add_product('Eggs', 'yaico', 5, 15)
    # r.add_product('Apple', 'yabloko', 5, 10)
    #
    # r.recieve_product(2,10,datetime.datetime(2020,1,1,0,0))
    # r.recieve_product(4, 30, datetime.datetime(2020, 1, 3, 0, 0))
    # r.recieve_product(5, 18, datetime.datetime(2020, 1, 6, 0, 0))
    # r.recieve_product(4, 7, datetime.datetime(2020, 1, 2,0,0))
    #
    # r.recieve_product(6, 7, datetime.datetime(2021, 11, 25, 0, 0))
    #
    #
    # r.add_dish('перог',1488,'desc',[(6,3)])

    r.recieve_product(6, 3, datetime.datetime(2021, 11, 27, 0, 0))
    r.recieve_product(6, 5, datetime.datetime(2021, 11, 28, 0, 0))

    # r.add_dish('не перог', 1488, 'ass', [(2, 3)])

    # r.remove_product_from_storage(6, 3)
    # print(r.check_dish(2))

    # r.remove_stall_products(datetime.datetime(2020,8,1,0,0))

    # print (db.get_all_product_id())

    # r.delete_product(1)

    # r.add_dish('seledka pod wyboi', 150, 'tak sebe', [(3, 1), (4, 1), (99, 2)])
