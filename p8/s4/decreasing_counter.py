# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value >= 1:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original_value

    # Write the rest of the methods here!

# This exercise has multiple parts. You can submit the parts separately. Each part is worth one exercise point.

# The exercise template contains a partially completed class DecreasingCounter:
    
# The class can now be used as shown below, and should produce the following printout after completing the first part of the exercise:

# counter = DecreasingCounter(10)
# counter.print_value()
# counter.decrease()
# counter.print_value()
# counter.decrease()
# counter.print_value()

# value: 10
# value: 9
# value: 8

# Decreasing the value of the counter
# Please complete the method decrease defined in the template, so that it decreases the value stored in the counter by one. See the example above for expected behaviour.

# The counter must not have a negative value
# Please add functionality to your decrease method, so that the value of the counter will never reach negative values. If the value of the counter is 0, it will not be further decreased.

# counter = DecreasingCounter(2)
# counter.print_value()
# counter.decrease()
# counter.print_value()
# counter.decrease()
# counter.print_value()
# counter.decrease()
# counter.print_value()

# value: 2
# value: 1
# value: 0
# value: 0

# Setting the value to zero
# Please add a method set_to_zero which sets the value of the counter to 0:

# counter = DecreasingCounter(100)
# counter.print_value()
# counter.set_to_zero()
# counter.print_value()

# value: 100
# value: 0

# Resetting the counter
# Please add a method reset_original_value() which resets the counter to its initial state:

# counter = DecreasingCounter(55)
# counter.decrease()
# counter.decrease()
# counter.decrease()
# counter.decrease()
# counter.print_value()
# counter.reset_original_value()
# counter.print_value()

# value: 51
# value: 55

