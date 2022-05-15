class FizzBuzz:
    def convert(self, number):
        if number % 3 == 0:
            return "Fizz"
        else:
            return number
        
    def say(self, number):
        print(self.convert(number))

