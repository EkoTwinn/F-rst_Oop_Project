from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call the super fuction to have accses all attributes/ methods
        super().__init__(
            name, price, quantity
        )
        
        #run validations to the recevied argument
        assert broken_phones >= 0, f"quantity {broken_phones} is not greater than 0"
    
        
        #assignt to self object
        self.broken_phones = broken_phones