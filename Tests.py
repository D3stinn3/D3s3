import pandas as pd


print('Hello World')

def counter():

    count = 0
    check = input('please input words to check: ')

    for letter in check:
        if (letter == 'D'):
            count += 1
            print(str(count) + " number of D's in the input")


counter()


def List_Type():

    list1 = ['Biology', 'History', 'Science', 'Physics']

    while True:
        if list1[1] == 'History':
            print(str(list1[1]) + ' is the real deal!')
        else:
            print(str('this is false!'))
        break
        

List_Type()


def Thanks():

    example = [1, 2, 3]

    for number in example:
        if (number >= max(example)) and (number not in example):
            print(number)
        else:
            print(number)
        break

    i = 0

    while i <= 3:

        i += 1

        the_number = example[:-1]

        example.append(the_number)

        print(the_number[:-1])


Thanks()

def The_Tuple():

    my_tuple = ('Destinne 1', 'Ann', 'Elijah')

    try:
        
        iter(my_tuple)

        print(f'{my_tuple} is iterable') # the tuple instance is iterable
        
        return True   
    
    except TypeError as TP:
        
        print(f'{TP} is the error occurred')

        return False


The_Tuple()


    
def fibonacci(num):

    fibo = [0, 1]

    i = 2

    while i <= num:

       next_fibo = fibo[i - 1] + fibo[i - 2]

       fibo.append(next_fibo)

       i += 1
    
    return fibo

print(fibonacci(9))


def fibonacci_1(num):

    f1 = f2 = 1

    print(f1, f2, end='')

    i = 2

    while i >= num:

        f1, f2 = f1, f1+f2

        print(f2, end='')

        i += 1

    print()



fibonacci_1(9)


def fibonacci_2():

    first_number = int(input('please input the first number: '))
    second_number = int(input('please input the second number: '))

    reps = int(input('please input number of reps in the fibonacci sequence: '))

    the_fibo_listing = [first_number, second_number]

    for i in range(reps):

        fibo = the_fibo_listing[-1] + the_fibo_listing[-2]

        the_fibo_listing.append(fibo)

    print(the_fibo_listing)


fibonacci_2()


class Train: # starts by describing the maximum payload of the train

    def __init__(self, weight_capacity):
        self.weight_capacity = weight_capacity

class Trip:

    def __init__(self, train):

        self.train = self.train_validation(train)

    def train_validation(self, train):

        self.train = train
        return self.train

    def __call__(self, passenger):

            self.trip = passenger
            self.train.weight_capacity -= self.trip.load_weight
            return self.train.weight_capacity

class Passenger:

    def __init__(self, load_weight):
        
        self.load_weight = load_weight

    def attend_trip(self, trip):

        self.trip = trip

# begins by describong the weight of the train

train = Train(34286)

# goes to the passanger instance pay load in the train

passenger_instance = Passenger(66)

section_scan = Trip.train_validation(Trip, train=20)

print(section_scan)


# object inheritance for the trip instances

trip = Trip(train)

print(trip(passenger_instance))


def merging(): #merging two or more lists using the pandas library!

    foo = {'mean': 10, 'median': 20, 'result': 30}
    bar = {'mean': 30, 'median': 20, 'result': 10}

    merger = pd.DataFrame({'foo': foo, 'bar': bar}).T.rename_axis('set')

    print(merger)


merging()


def json_and_python():

    jsn_file = {'fields': [
    {'name': 2, 'type': 'Int32'},
    {'name': 12, 'type': 'string'},
    {'name': 9, 'type': 'datetimeoffset'}
    ],
    'type': 'struct'}

    # the architecture of the json_file dict is:

    if jsn_file.setdefault('type', None) == 'struct':

        print("the key 'type' has a value 'struct'")

    else:

        print("the key 'type' does not have a value 'struct'")

     
    replacements = {'Int32': 'Integer', 'datetimeoffset': 'datetime'}

    for i, data in enumerate(jsn_file['fields']):

        if data['type'] in replacements.keys():

            jsn_file['fields'][i]['type'] = replacements[data['type']]

    print(jsn_file)


json_and_python()


def cat_listing():

    catNames = []

    while True:

        print('Weka Jina Ya Paka kwa mara ya ' + str(len(catNames)) + ' ama andika "Sina" kama hamna paka!')
        name = input()

        if name == 'Sina':
            break

        catNames += [name]

        print(catNames[0:])
    
    print('these are the cat names: ')

    for name in catNames:
        
        print(''+ str(name))

        if name not in catNames:

            print('please input the cat name to search: ')
            name = input()
            print('I do not have a cat named ' + str(name))
    
        else:

            print('I do have a cat named ' + str(name))


cat_listing()


def supply_chain():

    supplies = ['chilli', 'salt', 'garlic']

    for i in range(len(supplies)):

        if supplies[i] == 'garlic':
            
            print(str(i))
        
        elif supplies[i] == 'salt':

            print(str(i))
        
        elif supplies[i] == 'chilli':

            print(str(i))

        print('index ' + str(i) + ' represents ' + str(supplies[i]))
    
    supplies.sort()

    print(supplies)


supply_chain()


def password_verification():

    usernames = {'Destinne': 'Destinne123', 'Wachana': 'Wachana1996', 'Trinity': 'Baby123'}

    name = input('Please enter your username: ')

    if name in usernames:

        password = usernames.get(name) # the get method returns the name!
        pword = input('please input password for verification: ') 

        if password == pword:

            print('Access Granted!')

        else:

            print('Access Denied!')
    else:

        print('User is not an Administrator!')


password_verification()


def Adding_Entries():

    previous_entries = ['Ruwedah', 'Eleanor', 'Patricia', 'Nadia', 'Naomi', 'Maria']
    current_entries = ['Ru']

    for name in previous_entries:

        if name not in previous_entries and name in current_entries:

            previous_entries.append(name)

        else:

            print('No existing names to be appended')
    
    name = input('Please enter name to append: ')
    print('Welcome to the organization ' + str(name))

    current_entries.append(name)

    print('At the moment ' + str(len(current_entries)) + ' members have recently joined the organization')
    all_entries = current_entries + previous_entries

    all_entries.sort()

    print(all_entries)

Adding_Entries()

def Adding_Entries1(): # one can gain access to dict items using the setdefault prompt

    exp_dict = {}

    exp_dict.setdefault('Joke', 'I got jokes!')

    if 'Joke' in exp_dict.keys(): # one can also gain access to the key-value combo using the get method

        exp_dict1 = exp_dict.get('Joke', 0)

        print(exp_dict1)

        print(exp_dict)

    else:

        print(exp_dict)
    
    if 'Zero Jokes' not in exp_dict.keys():

        exp_dict.setdefault('Zero Jokes', 'Now I got another joke!')

        print(exp_dict)
    
    else:

        print(exp_dict)


Adding_Entries1()








    
