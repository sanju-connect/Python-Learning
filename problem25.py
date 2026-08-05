from random import randint


class Train:

  def __init__(self, TrainNo):
    self.TrainNo = TrainNo

  def Book_Ticket(self, start, end):
    print(f"Ticket is Booked in Train no: {self.TrainNo} from {start} to {end}")

  def Get_Status(self, start, end):
    print(f"Train (Train No: {self.TrainNo}) is Running Successfuly from {start} to {end}")

  def Get_Fare(self, start, end):
    print(f"Ticket Fair Train no: {self.TrainNo} from {start} to {end} is {randint(1, 500)}")

Sanju = Train(12345)
Sanju.Book_Ticket("Siliguri", "Kolkata")
Sanju.Get_Status("Siliguri", "Kolkata")
Sanju.Get_Fare("Siliguri", "Kolkata")