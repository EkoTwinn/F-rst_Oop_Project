class Item:
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the recevied argument
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"
    
        #assignt to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
        #Action to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
        
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return ("Item'{}', {}, {}").format((self.name), (self.price), (self.quantity))

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)