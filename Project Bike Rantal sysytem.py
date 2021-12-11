#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("enter the positive value or greater than zero:-")
        elif q>self.stock:
            print("enter the value (less than stock):-")
        else:
            self.stock=self.stock-q
            print("total price:",q*100)
            print("total Bikes:",self.stock)
while True:
    obj=Bikeshop(100)
    us=int(input('''
    1.Display Stocks
    2.Rent a bike
    3.Exit
    '''))
    if us==1:
        obj.displayBike()
    elif us==2:
        n=int(input("enter the quantity:-"))
        obj.rentForBike(n)
    else:
        break
            
    


# In[ ]:




