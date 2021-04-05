from creditcard import CreditCard
class Visa(CreditCard):
    
    def __init__(self,customer,bank,account,limit,apr):
        #Calling Parent's constructor
        super().__init__(customer,bank,account,limit)
        self._apr = apr #assigning own #this class attribute
    
    def charge(self,price):
        '''Charge given price to the card, assuming sufficient credit limit
            Return True if charge was processed
            Return False and assess $35 fee if charge is denied
        '''
        success = super().charge(price)
        if not success:
            self._balance += 35
            return success

    def process_month(self):
        '''Assess monthly interest on outstanding balance'''

        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor

    