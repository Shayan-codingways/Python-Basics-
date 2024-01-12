class Train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare

    def status(self):
       print(f"the name is {self.name}")
       print(f"the seats are {self.seats}")

    def fareinfo(self):
        print(f"the fare is ${self.fare}")

    def bookticket(self):
        if self.seats>0:
            print("Ticket booked with seat number {self.seats}")
            self.seats=self.seats-1  # seat 1 gone
        else:
            print("Sorry, no seats remaining")

intracity=Train("Expressway__1222", 2, 455)

intracity.status()
intracity.fareinfo()

print("\n")
intracity.bookticket()
intracity.status()
 
print("\n")
intracity.bookticket()
intracity.status()

intracity.bookticket()
