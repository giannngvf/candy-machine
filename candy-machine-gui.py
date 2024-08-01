from tkinter import *
from tkinter import messagebox

window = Tk()


class CashRegister:
    def __init__(self, cashOnHand=500):
        self.cashOnHand = cashOnHand

    def currentBalance(self):
        return self.cashOnHand

    def acceptAmount(self, AmountIn):
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


cashRegister = CashRegister()
candy = Dispenser()
chips = Dispenser(40, 80)
gum = Dispenser(60, 55)
cookies = Dispenser(15, 100)


def sellProduct(product, cRegister):
    try:
        centsInserted = int(centsInsert.get())
        centsInsert.delete(0, 'end')
        if product.getCount() > 0:
            price = product.getProductCost()
            centsRequired = price - centsInserted

            if centsRequired > 0:
                messagebox.showinfo("Amount Needed", f"Please insert {centsRequired} more cents.")
            else:
                change = centsInserted - price
                if change == 0:
                    messagebox.showinfo("Buy Successful", "Thank you for buying our product!")
                else:
                    messagebox.showinfo("Buy Successful", f"Thank you for buying our product! Your change is {change} cents.")
                cRegister.acceptAmount(price)
                product.makeSale()
        else:
            messagebox.showinfo("Sold Out", "Item is sold out.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input!")


def candyWindow():
    global centsInsert
    candyWin = Toplevel(window)
    candyWin.geometry('360x150')
    candyWin.title('Candy')
    candyWin.config(background='#F694C1')

    candyLabel = Label(candyWin, text='Please insert 50 cents for the candy:', font=('Helvetica', 10, 'bold'), fg='black', bg='sky blue', bd=5, relief=RAISED)
    candyLabel.place(x=60, y=15)
    centsInsert = Entry(candyWin, font=('Helvetica', 10, 'bold'), bg='light gray', relief=SUNKEN, bd=5, justify=CENTER)
    centsInsert.place(x=110, y=50)
    ok = Button(candyWin, text='OK', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=20, relief=RAISED, command=lambda: sellProduct(candy, cashRegister))
    ok.place(x=110, y=90)
    cancel = Button(candyWin, text='CANCEL', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=5, relief=RAISED, command=candyWin.destroy)
    cancel.place(x=190, y=90)


def chipsWindow():
    global centsInsert
    chipsWin = Toplevel(window)
    chipsWin.geometry('360x150')
    chipsWin.title('Chips')
    chipsWin.config(bg='#F694C1')

    chipsLabel = Label(chipsWin, text='Please insert 80 cents for the chips:', font=('Helvetica', 10, 'bold'), fg='black', bg='sky blue', bd=5, relief=RAISED)
    chipsLabel.place(x=60, y=15)
    centsInsert = Entry(chipsWin, font=('Helvetica', 10, 'bold'), bg='light gray', relief=SUNKEN, bd=5, justify=CENTER)
    centsInsert.place(x=110, y=50)
    ok = Button(chipsWin, text='OK', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=20, relief=RAISED, command=lambda: sellProduct(chips, cashRegister))
    ok.place(x=110, y=90)
    cancel = Button(chipsWin, text='CANCEL', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=5, relief=RAISED, command=chipsWin.destroy)
    cancel.place(x=190, y=90)


def gumWindow():
    global centsInsert
    gumWin = Toplevel(window)
    gumWin.geometry('360x150')
    gumWin.title('Gum')
    gumWin.config(bg='#F694C1')

    gumLabel = Label(gumWin, text='Please insert 55 cents for the gum:', font=('Helvetica', 10, 'bold'), fg='black', bg='sky blue', bd=5, relief=RAISED)
    gumLabel.place(x=60, y=15)
    centsInsert = Entry(gumWin, font=('Helvetica', 10, 'bold'), bg='light gray', relief=SUNKEN, bd=5, justify=CENTER)
    centsInsert.place(x=110, y=50)
    ok = Button(gumWin, text='OK', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=20, relief=RAISED, command=lambda: sellProduct(gum, cashRegister))
    ok.place(x=110, y=90)
    cancel = Button(gumWin, text='CANCEL', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=5, relief=RAISED, command=gumWin.destroy)
    cancel.place(x=190, y=90)


def cookiesWindow():
    global centsInsert
    cookiesWin = Toplevel(window)
    cookiesWin.geometry('360x150')
    cookiesWin.title('Cookies')
    cookiesWin.config(bg='#F694C1')

    cookiesLabel = Label(cookiesWin, text='Please insert 100 cents for the cookies:', font=('Helvetica', 10, 'bold'), fg='black', bg='sky blue', bd=5, relief=RAISED)
    cookiesLabel.place(x=60, y=15)
    centsInsert = Entry(cookiesWin, font=('Helvetica', 10, 'bold'), bg='light gray', relief=SUNKEN, bd=5, justify=CENTER)
    centsInsert.place(x=110, y=50)
    ok = Button(cookiesWin, text='OK', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=20, relief=RAISED, command=lambda: sellProduct(cookies, cashRegister))
    ok.place(x=110, y=90)
    cancel = Button(cookiesWin, text='CANCEL', bg='sky blue', font=('Helvetica', 9, 'bold'), bd=5, padx=5, relief=RAISED, command=cookiesWin.destroy)
    cancel.place(x=190, y=90)


def viewingBalance():
    balance = cashRegister.currentBalance()
    balanceWin = Toplevel(window)
    balanceWin.geometry('360x150')
    balanceWin.title('Balance')
    balanceWin.config(bg='#F694C1')

    balanceInfo = Label(balanceWin, text='Balance:', font=('Helvetica', 12, 'bold'), bg='sky blue', fg='black', bd=5, relief=RAISED)
    balanceInfo.place(x=145, y=15)
    currentBalance = Label(balanceWin, text=balance, padx=100, font=('Helvetica', 12, 'bold'), bg='light gray', fg='black', bd=5, relief=SUNKEN)
    currentBalance.place(x=66, y=50)
    exitWindow = Button(balanceWin, text='EXIT', font=('Helvetica', 12, 'bold'), bg='sky blue', relief=RAISED, bd=5, command=balanceWin.destroy)
    exitWindow.place(x=155, y=85)


def exitMainWindow():
    window.destroy()


window.geometry('420x380')
window.title('Candy Machine')
window.config(bg='#F694C1')

welcomeText = Label(window, text="WELCOME TO SWEET'S CANDY SHOP", font=('Helvetica', 12, 'bold'), fg='black', bg='pink', relief=RAISED, bd=5, padx=5, pady=5)
welcomeText.place(x=55, y=20)

selectionText = Label(window, text='To make a selection, click on the product below:', font=('Helvetica', 10, 'bold'), fg='black', bg='pink', relief=RAISED, bd=4)
selectionText.place(x=57, y=70)

candyButton = Button(window, text='CANDY', font=('Helvetica', 12, 'bold'), padx=99, bg='sky blue', bd=5, relief=RAISED, command=candyWindow)
candyButton.place(x=80, y=110)

chipsButton = Button(window, text='CHIPS', font=('Helvetica', 12, 'bold'), padx=103, bg='sky blue', bd=5, relief=RAISED, command=chipsWindow)
chipsButton.place(x=80, y=153)

gumButton = Button(window, text='GUM', font=('Helvetica', 12, 'bold'), padx=109, bg='sky blue', bd=5, relief=RAISED, command=gumWindow)
gumButton.place(x=80, y=196)

cookiesButton = Button(window, text='COOKIES', font=('Helvetica', 12, 'bold'), padx=91, bg='sky blue', bd=5, relief=RAISED, command=cookiesWindow)
cookiesButton.place(x=80, y=239)

balanceButton = Button(window, text='BALANCE', font=('Helvetica', 12, 'bold'), padx=88, bg='sky blue', bd=5, relief=RAISED, command=viewingBalance)
balanceButton.place(x=80, y=282)

exitButton = Button(window, text='EXIT', font=('Helvetica', 12, 'bold'), padx=109, bg='sky blue', bd=5, relief=RAISED, command=exitMainWindow)
exitButton.place(x=80, y=325)

window.mainloop()