import random

from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from ..views import user_bin
from django.db import connection
from django.db.utils import ProgrammingError


class CheckoutView(UnicornView):
    bin = []
    grand_total = ''
    customer_name = ""
    customer_address = ""
    customer_phone = ""
    customer_email = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grand_total = kwargs['grand_total']
        self.user_bin = user_bin
        self.bin = self.user_bin.parts

    def _execute_query(self, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            response = cursor.fetchall()
            print(response)
            return response
        except ProgrammingError as e:
            print(f"Error when inserting! {e}. Technically, this is a success!")
            return None

    def _get_id(self, query):
        response = self._execute_query(query)
        if not response:
            return -1
        return response[0][0]

    def save_and_pay(self):
        customer_id_query = (f"SELECT * from customers WHERE customers.recipient_name = "
                             f"'{self.customer_name}' AND customers.recipient_address = "
                             f"'{self.customer_address}' AND customers.phone = "
                             f"'{self.customer_phone}' AND customers.email = "
                             f"'{self.customer_email}' ;")
        customer_id = self._get_id(customer_id_query)
        if customer_id == -1:
            print("Didn't find a customer for the first time! Adding!")
            self._execute_query((f"INSERT INTO customers (recipient_name, recipient_address, phone, email) "
                                 f"VALUES('{self.customer_name}','{self.customer_address}',"
                                 f"'{self.customer_phone}','{self.customer_email}');"))
            customer_id = self._get_id(customer_id_query)

        if customer_id == -1:
            print("Shitfuck :D Couldn't insert a customer apparently!")
            return
        while True:
            order_number = random.randint(0, 1000000)
            order_number = f"{order_number:06}"
            order_id_query = f"SELECT * FROM orders where order_number = '{order_number}'"
            print(order_number)
            order = self._execute_query(order_id_query)
            if not order:
                self._execute_query((f"INSERT INTO orders (customer_id, order_number) "
                                     f"VALUES({customer_id},'{order_number}');"))
            order_id = self._get_id(order_id_query)
            if order_id == -1:
                print("Och... Failed to insert order!")
                return
            break
        for part in self.user_bin.parts:
            self._execute_query((f"INSERT INTO ordered_parts (order_id, part_id, quantity) "
                                 f"VALUES({order_id},{part['part_id']},{part['quantity']});"))
        return redirect('payment', grand_total=self.grand_total)
