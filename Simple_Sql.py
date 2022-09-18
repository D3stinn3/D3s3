"""class initialization"""
import random

class Initialization:

    def __init__(self, numerouno=0, numerodos=0):

        self.numerouno = numerouno
        self.numerodos = numerodos

    def SecondInitialization(self):

        if self.numerouno == 0 and self.numerodos == 0:

            print(f'{self.numerouno} and {self.numerodos} are the initial inputs!')
        
        else:
            print(f'not the initial output expected!')



obj = Initialization()
obj.SecondInitialization()


"""modifying a variable/object within a class"""

class MotorBike:

    condition = 'brand new'
    crisis = False

    def __init__(self, model, color, rpm):

        self.model = model
        self.color = color
        self.rpm = rpm

    def show_bike(self):

        return 'This is a brand new bike\n Model: %s, Color: %s, Rpm: %d' %(self.model, self.color, self.rpm)

    def passive_condition(self):

        self.condition = 'partially used' # this is where we change the argment!

        if self.condition == 'brand new': # checking the variable!

            print('not used yet!')

        elif self.condition == 'partially used':
            print('Used!')
        
        else:
            print('used!')


    def fuel_valve(self):

        try:

            while not self.crisis:

                if self.rpm > 3000:
                    yield 'Valve Shut'

                yield 'Valve Open' # acts as our else statement!

        except (StopIteration, AttributeError) as si:

            yield f'Error generated is: {si}'
    
    def new_iter(self):
        pass

        """the_iter = []

        iterations = iter(the_iter)

        print(iterations.__next__())"""
    
obj2 = MotorBike('Honda', 'Black', 3000)
obj2.passive_condition()
obj2_ = obj2.fuel_valve()

obj2.new_iter()
print(obj2_.__next__()) # the next attribute runs based on an iterator!

def prime_number():
    num = 29
    flag = False

    if num > 1:
        for i in range(2, num):

            if (num % i) == 0:
                flag = True
            break
    
    if flag:
        print(f'{num} is not a prime number')
    else:
        print(f'{num} is a prime number!')

prime_number()

class MultThree:

    def __init__(self, max=0):

        """a class implementing an iterator on the multiples of three"""

        self.max = max

    def __iter__(self):

        self.m = 0 # initializing an intrinsic object in the __iter__ fxn!
        return self
    
    def __next__(self):

        try:
            
            if self.m >= self.max:
                result = 3**self.m

                self.m += 1
                return result

        except StopIteration as si:

            print(f'Error Occured as :  {si}')
        


x_iter = MultThree(6)

for i in x_iter:
    print(i)
    break
x_iter_ = iter(x_iter)
print(next(x_iter_))


def gener():

    print('This is the first iteration')
    x = 5
    print('This is the second iteration')
    x += 5
    print('This is the last iteration')
    x += 5

genr = gener()
genr