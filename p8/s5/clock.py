# Please define a new class named Clock which expands on the capabilities of your Stopwatch class. It should work as follows:

# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)

# clock.set(12, 5)
# print(clock)

# 23:59:55
# 23:59:56
# 23:59:57
# 23:59:58
# 23:59:59
# 00:00:00
# 00:00:01
# 12:05:00

# As you can see above, the constructor should take initial values for the hours, minutes and seconds as arguments, and set these appropriately. The tick method adds one second to the clock. The set method sets new values for the hours and the minutes, and sets the seconds to zero.
    
class Clock:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.seconds <= 59:
            self.seconds += 1
            if self.seconds == 60:
                if self.minutes <= 59:
                    self.minutes += 1
                    if self.minutes == 60:
                        if self.hours <= 23:
                            self.hours += 1
                            if self.hours == 24:
                                self.hours = 0
                        self.minutes = 0
                self.seconds = 0

    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        # check hours
        output = ""
        if self.hours < 10:
            output += f"0{self.hours}:"
        else:
            output += f"{self.hours}:"

        # check minutes
        if self.minutes < 10:
            output += f"0{self.minutes}:"
        else:
            output += f"{self.minutes}:"

        # check seconds
        if self.seconds < 10:
            output += f"0{self.seconds}"
        else:
            output += f"{self.seconds}"

        return output