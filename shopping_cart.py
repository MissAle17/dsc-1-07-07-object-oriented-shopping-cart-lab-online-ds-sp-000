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
    
#           if self.employee_discount:
 #           discount = self.employee_discount/100
##            return disc_total Now, let's define an instance method called apply_discount that applies a discount if one is provided and returns the discounted total. For example, if we initialize a new shopping cart with a discount of 20% then our total should be discounted in the amount of 20%. So, if our total were $100, after the discount we only would owe $80.

#If our shopping cart does not have an employee discount, then it should return a string saying: "Sorry, there is no discount to apply to your cart :("