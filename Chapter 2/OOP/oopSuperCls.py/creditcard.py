class CreditCard:
    def __init__(self,customer,bank,account,limit):
        ''' Create Credit Card instance
        The initail balance is 0
        Customer    : the name of the customer
        Bank        : the name of the Bank
        account     : the account identifier
        limit       : credit limit
        '''
        self._customer = customer
        self._bank     = bank
        self._account  = account
        self._limit    = limit
        self._balance  = 0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def charge(self,price):
        '''Charge given price to the card, assuming sufficient credit limit
        Return True if charge was processed, False if charge was denied.'''
        if price+self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    #Making payment towards balance
    def make_payment(self,amount):
        #Subtract amount from balance, this also setting the object's balance newly
        self._balance -= amount
    
