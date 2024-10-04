
# Roommate Payment Calculator

## Overview

This program calculates how much one roommate owes to the other when they go shopping. The program works by comparing a receipt (the "check") and a list of products requested by the roommate. It then calculates:

1. The total amount spent on the shopping.
2. The amount the non-shopping roommate owes, based on their requested items.
3. A list of requested items that were not found on the receipt.

## Files

- `check.txt`: Contains the list of products and their prices from the shopping trip. The format is `product,price`.
- `product_list.txt`: Contains the list of products requested by the roommate. The format is `product,quantity`.

## Program Output

- The total amount spent on the shopping.
- The amount the non-shopping roommate owes.
- A list of items requested but not found on the receipt, along with the quantity.

## Example

### Input Files:

**check.txt**:

```
Milk,1.59
Milk,1.59
Egg,1.99
Milk,1.59
Egg,1.99
Bread,2.20
Tomatos,5.60
Soap,2.99
Soap,2.99
Beer,1.29
Beer,1.29
Beer,1.29
Beer,1.29
Beer,1.29
Bananas,3.50
Mozzarella,1.80
Rum,12.59
Oil,6.99
Oil,6.99
Rice,2.50
Mozzarella,1.80
Flour,0.80
Flour,0.80
Water,2.40
Water,2.40
Water,2.40
Water,2.40
Chewing gum,1.20
Razors,4.99
```

**product_list.txt**:

```
Beer,2
Bread,1
Oil,3
Rum,2
Milk,2
Tomatos,1
Mozzarella,4
Water,1
AAA Battery,2
```

### Program Output:

```
Total spent: 82.54 euro
Money from roommate: 46.13 euro
Items not purchased:
      1 Oil
      1 Rum
      2 Mozzarella
      2 AAA Battery
```

## Usage

1. Prepare `check.txt` and `product_list.txt` files with the correct formats.
2. Run the program.
3. View the results in the console, including the total amount spent, amount owed by the roommate, and any items that were not found.

## Contact

If you have any questions or feedback, feel free to contact me via [LinkedIn](your-linkedin-profile) or email at your-email@example.com.
