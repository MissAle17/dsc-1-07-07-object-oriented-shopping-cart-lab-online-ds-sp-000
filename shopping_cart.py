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
    
    def median_item_price(self):
        prices = [self._items(item, "price") for item in self.items]
        prices.sort()
        return self.find_median(prices)

    def find_median(self, list_of_prices):
        length = len(list_of_prices)
        if (length%2 == 0):
            index1 = int(length/2)
            index2 = mid_one - 1
            median = (list_of_prices[index1] + list_of_prices[index2])/2
            return median
        else:
            index3 = int(length/2)  
            return list_of_prices[index3]
                          
 #  mean_item_price and median_item_price  the mean is the average price per item and to find the median we must do three things:

#First put all numbers in our list in ascending order (smallest to greatest)
#Then check to see if there is an odd number of elements in our list. If so, the middle number is the median
#Finally, if there is an even number of elements in the list, the median will be the average or mean of the two center elements (e.g. given the list [1,2,3,4] the elements 2 and 3 are the two center elements and the median would be (2 + 3)/2 or 2.5).
    
    
    



