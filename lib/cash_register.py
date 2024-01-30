#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price, quantity)

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Formatting the total as an integer if it is a whole number
            if self.total.is_integer():
                formatted_total = int(self.total)
            else:
                formatted_total = f"{self.total:.2f}"
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    
    def void_last_transaction(self):
        if self.last_transaction:
            title, price, quantity = self.last_transaction
            self.total -= price * quantity
            for _ in range(quantity):
                self.items.remove(title)
        self.last_transaction = None




