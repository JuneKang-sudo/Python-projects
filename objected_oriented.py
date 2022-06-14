'''
Objected oriented programming hw

For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

'''

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return (f'Account owner: {self.owner}\nAccount balance: ${self.balance}')
    def deposit(self, deposit):
        if deposit: self.balance = deposit + self.balance
        print (f'This is your deposit: ${deposit}')
        print('Deposit Accepted')
        print (f'This is your new balance: ${self.balance}')


    def withdraw (self, withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw
            return (f'Withdrawal Accepted \nThis is your new balance: ${self.balance}')
        else:
            return ('Funds Unavailable!')


'''
Test
'''
acct1 = Account('Jose', 50)
print (acct1)
#print (acct1.owner)
#print(acct1.balance)
acct1.deposit(50)
acct1.deposit(80)
print(acct1.balance)
print(acct1.withdraw(130))
print(acct1.withdraw(130))


'''
Fill in the Line class methods to accept coordinates as a pair of tuples and
return the slope and distance of the line.
'''
import math
class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance (self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        dis = math.sqrt(((x2-x1)**2)+(y2-y1)**2)
        return dis
    def slope (self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print (li.slope())

'''
Fill in the class
'''

class cylinder:
    def __init__(self, height =1, radius =1):
        self.height = height
        self.radius = radius
    def volume (self):
        return math.pi * (self.radius **2)*self.height
    def surface_area (self):
        return 2*math.pi*self.radius*self.height +2* math.pi * (self.radius **2)

c = cylinder (2,3)
#print (c.volume())
#print (c.surface_area())
