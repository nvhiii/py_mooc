# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
             self.balance -= amount
             return True
        return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        regular = 2.50
        self.funds += regular
        
        if payment < regular:
            return payment
        else:
            change = payment - regular
            self.lunches += 1
            return change
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        special = 4.30
        # Increase the value of the funds at the terminal by the price of the lunch,
        self.funds += special
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        if payment < special:
            return payment
        else:
            change = payment - special
            self.specials += 1
            return change

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        regular = 2.50
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if card.balance >= regular:
            card.subtract_from_balance(regular)
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        special = 4.30
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if card.balance >= special:
            card.subtract_from_balance(special)
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)

# In the previous part there was an exercise where you implemented the class LunchCard. The card had separate methods for eating a regular and a special lunch, along with a method for depositing money on the card.

# The LunchCard class, as you were asked to implement it, has some problems, however. The card itself had knowledge of the prices of the different lunch options, and knew to subtract the right amount of money from the balance based on these. But imagine the prices changed, or there were new items introduced to the system, but several cards were already registered in the system. This would mean all existing cards would need to be replaced by versions with knowledge of the new prices.

# A better solution would be to make the cards "stupid", ignorant of the prices of different products. The purpose of the card would be to simply keep track of the available balance. All more complicated features should be contained within another class: the payment terminal.

# A simpler LunchCard
# Let's first implement a simpler version of the LunchCard class. The card should contain functionality only for finding out the current balance, depositing money on the card, and subtracting from the balance. Please fill in the subtract_from_balance(amount) method in the exercise template according to the instructions in the comments:

# The payment terminal and dealing with cash payments
# In the student cafeteria it is possible to pay with either cash or a LunchCard. A payment terminal is used to handle both cash and card transactions. Let's start with the cash transactions.

# Here we have a skeleton implementation for a PaymentTerminal class. Please implement the methods as described in the comments:
     
# Dealing with card transactions
# Now let's implement card transactions. We will need methods which take a LunchCard as an argument, and reduce the balance on the card by the price of the lunch. Below you will find the outlines of these functions. Please fill in the methods as described in the comments:

# when paying with a LunchCard the cash funds available at the terminal do not change. However, the lunches are still sold whenever there is the required balance available, so remember to increase the number of lunches sold appropriately.

# You may use the following code to test your class:
     
# Depositing money on the card
# Finally, let's add a method which lets you deposit money on the card. The card owner pays this by cash, so the deposited sum is added to the funds available at the terminal. Here is an outline for the method:

