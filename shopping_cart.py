class ShoppingCart:
    def __init__(self):
        self._total = 0
        self._items = []
        self._employee_discount = None
        
    @property    
    def total(self):
        return self._total
    @total.setter
    def total(self, new_total):
        new_total = self._total
        return self.total
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, list_of_items):
        self._items = list_of_items
        return self.items
    @property
    def employee_discount(self):
        return self._employee_discount
    @employee_discount.setter
    def employee_discont(self, discount):
        self._employee_discount = discount
        return self.employee_discount
    #Next, we want to define an instance method called add_item that will add an item to our cart. It should take in the name of an item, its price and an optional quantity. The method should increase the shopping cart's total by the appropriate amount and return the new total for the shopping cart.
    
    def add_item(self, item_name, item_price, quantity=1):
        
        if grade_level in self._roster:
            self._roster[grade_level].append(student_name)
        else: 
            self._roster[grade_level] = [student_name]
        self.total += total
    return self.total
  