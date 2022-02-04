class Robot():
  def __init__(self, name, CardNmuber, pin, order, quantity, bill) :
      self.name = name
      self.Cardnumber = CardNmuber
      self.pin = pin
      self.order = order
      self.quantity = quantity
      self.bill = bill
  def introduce_Name(self):
    price = 50
    menu = "Black Coffe, Espresso, Latte, Cappucino"
    print("Hello, Welcome to Harjot's Cafe")
    self.name = input("What is your name :")
    self.order = input("Hey " + self.name + ", What would you like to have? Here is what we are serving \n" + menu + ": ")
    self.quantity = input("How many " + self.order + " do you want to have :")
    self.bill = price * int(self.quantity)
    self.Cardnumber = input("Ok, Your total is : " + str(self.bill) + " Rs \nPlease Enter Your CardNumber : ")
    self.pin = input("Enter Your Pin : ")
    if(int(self.quantity) < 5):
      print("Thank you " + self.name + ", Your will be ready in a minute")
    else:
      print("Thank you " + self.name + ", Your order will be ready in 10-15 minutes")
r1 = Robot("Harjot", "1223", "233", "23edf", "123", "123")
print(r1.introduce_Name())
