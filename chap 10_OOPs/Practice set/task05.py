
'''Class formed'''
class Train:
    # class attribute
    Train_name="Shalimar"
    
    # method/function
    def Status(self):
        self.seats = 3
        return self.seats

    def fare(self):
        self.fare = 90
        return self.fare 

    def bookticket(self):
        if self.seats>0:
            print(f"Ticket booked with seat number {self.seats}")
            self.seats=self.seats-1  # seat 1 gone
        else:
            print("Sorry, no seats remaining")
    
    def cancel(self):
        print(f"tcicket cancelled for seat {self.seats+1}")
        self.seats=self.seats+1
     
intercity=Train()

intercity.Status()
intercity.fare()

print(f"{Train.Train_name} has {intercity.seats} with each having a fare of {intercity.fare}")

intercity.bookticket()
intercity.bookticket()
print("the seats remaining are",intercity.seats)
print("\n")
intercity.cancel()
intercity.bookticket()