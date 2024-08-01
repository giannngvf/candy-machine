# Candy Machine Application

## Overview

This application simulates a candy machine with a graphical user interface using Tkinter. Users can select and purchase items such as candy, chips, gum, and cookies. The machine maintains a balance and allows users to view the current balance. The application also includes functionality to handle purchases and provide change.

## Features

- **Product Selection**: Users can choose from Candy, Chips, Gum, and Cookies.
- **Purchase Handling**: Users can insert money and receive change if necessary.
- **Balance View**: Users can check the current balance in the cash register.
- **GUI**: A Tkinter-based graphical user interface to interact with the candy machine.

## Classes

### `CashRegister`

Manages the cash on hand in the register.

- **`__init__(self, cashOnHand=500)`**: Initializes with a default balance of 500 cents.
- **`currentBalance(self)`**: Returns the current balance.
- **`acceptAmount(self, AmountIn)`**: Adds the given amount to the balance.

### `Dispenser`

Manages the dispensing of products.

- **`__init__(self, numberOfItems=50, cost=50)`**: Initializes with a number of items and cost per item.
- **`getCount(self)`**: Returns the number of items left.
- **`getProductCost(self)`**: Returns the cost of the product.
- **`makeSale(self)`**: Reduces the number of items by one.

## Functions

- **`sellProduct(product, cRegister)`**: Handles the sale process, including checking if enough money is inserted and updating the cash register and product inventory.
- **`createProductWindow(product, price, title)`**: Creates a window for a specific product with a prompt to insert money.
- **`candyWindow()`**: Opens the window for purchasing candy.
- **`chipsWindow()`**: Opens the window for purchasing chips.
- **`gumWindow()`**: Opens the window for purchasing gum.
- **`cookiesWindow()`**: Opens the window for purchasing cookies.
- **`viewingBalance()`**: Opens a window displaying the current balance.
- **`exitMainWindow()`**: Closes the main application window.
