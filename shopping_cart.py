class ShoppingCart:
    def __init__(self, emp_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = emp_discount
        
    @property    
    def total(self):
        return self._total
    @total.setter
    def total(self, new_total):
        self._total = new_total
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
    
    def add_item(self, item_name, item_price, quantity=1):
        for item in list(range(quantity)):
            self._items.append({'name': item_name, 'price':item_price})
            self.total += item_price
        return self.total
    
    def mean_item_price(self):
        return (self.total/len(self.items))
    
    def find_median(self, list_of_prices):
        if (len(list_of_prices)%2 == 0):
            index1 = int((len(list_of_prices))/2)
            index2 = mid_one - 1
            median = (list_of_prices[index1] + list_of_prices[index2])/2
            return median
        else:
            index3 = int((len(list_of_prices))/2)  
            return list_of_prices[index3]

    def find_item(self, item, key):
        return item[key]
    
    def median_item_price(self):
        prices = [self.find_item(item, "price") for item in self.items]
        prices.sort()
        return self.find_median(prices)
    
    def apply_discount(self):
        if self.employee_discount:
            discount_amt = self.employee_discount/100
            total_discount = self.total * (1 - discount_amt)
            return total_discount
        else:
            return print("Sorry, there is no discount to apply to your cart :(")
    def item_names(self):
        all_items=[self.find_item(item, "name")for item in self.items]
        return all_items
    def void_last_item(self):
        if self.items:
            void = self.items.pop()
        else: 
            return print( "There are no items in your cart!")
        self.total -= void['price']
        
        
        
        
        
        
