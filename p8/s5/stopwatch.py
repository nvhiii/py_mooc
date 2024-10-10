# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

# The exercise template contains the following skeleton for the Stopwatch class:
    
# Please add to the class definition so that it works as follows:

# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()

# 00:00
# 00:01
# 00:02
# ... many more lines printed out
# 00:59
# 01:00
# 01:01
# ... many, many more lines printed out
# 59:58
# 59:59
# 00:00
# 00:01

# So, the method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. Your class definition should also contain a __str__ method, which returns a string representation of the state of the stopwatch, as shown in the example above.

# Hint: it might make it easier to test the tick method if you temporarily set the initial values of the seconds and minutes to some value closer to 59 in the constructor. If you do change the initial values, remember to change them back before submitting.

    def tick(self):
        # ticks 1 second
        if self.seconds <= 59:
            self.seconds += 1
            if self.seconds == 60:
                if self.minutes <= 59:
                    self.minutes += 1
                    if self.minutes == 60:
                        self.minutes = 0
                self.seconds = 0

    def __str__(self):
        if self.minutes < 10 and self.seconds < 10:
            return f"0{self.minutes}:0{self.seconds}"
        elif self.minutes < 10 and self.seconds > 10:
            return f"0{self.minutes}:{self.seconds}"
        elif self.minutes > 10 and self.seconds < 10:
            return f"{self.minutes}:0{self.seconds}"
        else:
            return f"{self.minutes}:{self.seconds}"
