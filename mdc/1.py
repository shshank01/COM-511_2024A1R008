# Write a class 'Train' which has the methods to book a ticket, get status (no of seats) and 
# get fare info of train running under indian railway 
class Train:
    def __init__(self,seats,fare):
        self.seats=seats
        self.fare=fare
    def book_ticket(self):
        if self.seats>0:
            self.seats-=1
            print("Ticket booked successfully")
        else:
            print("No seats available")
    def fare_info(self):
        print("Fare of the train is: ",self.fare)
    def no_of_seats(self):
        print("Remaining seats: ", self.seats)
train1=Train(10,150)
train1.book_ticket()
train1.fare_info()
train1.no_of_seats()