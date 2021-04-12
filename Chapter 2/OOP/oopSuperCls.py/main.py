from creditcard import CreditCard
from visacard import Visa
def main():
    #Creating an object of CreditCard
    first_customer = CreditCard('Abdullah Jonaed','Chase Bank','47896512345',5000)
    print(first_customer.get_limit())
    # Creating an object of Visa
    visaCustomer = Visa('AJ', 'Capital One', '587964123', 500, 24)
    visaCustomer.charge(500)
    print(visaCustomer.get_balance())
    print(visaCustomer.get_limit())
    print(visaCustomer.charge(100))
    visaCustomer.process_month()
    print(visaCustomer.get_balance())

if __name__ == "__main__":
    main()
