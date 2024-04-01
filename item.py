import csv

class Item:
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"

        # Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    def name(self):
        """Returns the name of the item."""
        return self._name
        
    @name.setter
    def name(self, value):
        self.__name = value


    def calculate_total_price(self):
        return self.price * self.quantity
        
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        #For i.e : 0.5, 10.0
        if isinstance(num, float):
            #Counts out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    
