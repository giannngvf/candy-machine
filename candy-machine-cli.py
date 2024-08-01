# CANDY MACHINE COMMAND LINE INTERFACE VERSION
class CashRegister:
    def __init__(self, cashOnHand=500):
        self.cashOnHand = cashOnHand

    def currentBalance(self):
        return self.cashOnHand

    def acceptAmount(self, AmountIn: int):
        self.cashOnHand += AmountIn


class Dispenser:
    def __init__(self, numberOfItems=50, cost=50):
        self.numberOfItems = numberOfItems
        self.cost = cost

    def getCount(self):
        return self.numberOfItems

    def getProductCost(self):
        return self.cost

    def makeSale(self):
        self.numberOfItems -= 1


class CandyMachine:

    @staticmethod
    def Program():
        cashRegister = CashRegister()
        candy = Dispenser()
        chips = Dispenser(30, 65)
        gum = Dispenser(20, 55)
        cookies = Dispenser(25, 85)

        while True:
            try:
                CandyMachine.showSelection()
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    CandyMachine.sellProduct(candy, cashRegister)
                    buyAgain = input("Do you want to buy again? Y/N: ")
                    if buyAgain.lower() == 'y':
                        pass
                    elif buyAgain.lower() == 'n':
                        break
                    else:
                        print("Invalid input!")
                elif choice == 2:
                    CandyMachine.sellProduct(chips, cashRegister)
                    buyAgain = input("Do you want to buy again? Y/N: ")
                    if buyAgain.lower() == 'y':
                        pass
                    elif buyAgain.lower() == 'n':
                        break
                    else:
                        print("Invalid input!")
                elif choice == 3:
                    CandyMachine.sellProduct(gum, cashRegister)
                    buyAgain = input("Do you want to buy again? Y/N: ")
                    if buyAgain.lower() == 'y':
                        pass
                    elif buyAgain.lower() == 'n':
                        break
                    else:
                        print("Invalid input!")
                elif choice == 4:
                    CandyMachine.sellProduct(cookies, cashRegister)
                    buyAgain = input("Do you want to buy again? Y/N: ")
                    if buyAgain.lower() == 'y':
                        pass
                    elif buyAgain.lower() == 'n':
                        break
                    else:
                        print("Invalid input!")
                elif choice == 0:
                    print(f"The current balance is {cashRegister.currentBalance()}.")
                elif choice == 9:
                    print("Thank you for visiting our candy machine! Have a nice day!")
                    break
                else:
                    print("Invalid input!")
            except ValueError:
                print("Invalid input!")

    @staticmethod
    def sellProduct(product, cRegister):
        if product.getCount() > 0:
            price = product.getProductCost()
            centsRequired = price
            centsInserted = 0
            while centsRequired > 0:
                print("Please insert", centsRequired, "cents: ")
                centsInserted = centsInserted + int(input())
                centsRequired = price - centsInserted
            cRegister.acceptAmount(price)
            product.makeSale()
            change = abs(centsRequired)
            if change > 0:
                print(
                    f"Thank you for buying our product! Enjoy and have a nice day! Here's your {change} cents change.")
            else:
                print("Thank you for buying our product! Enjoy and have a nice day!")
        else:
            print("Sorry this item is sold out.")

    @staticmethod
    def showSelection():
        print("****Welcome to Sweet's Candy Shop****")
        print("To select an item enter"
              "\n 1 for Candy\n 2 for Chips\n 3 for Gum\n 4 for Cookies"
              "\n 0 to View Balance\n 9 to Exit")


CandyMachine.Program()