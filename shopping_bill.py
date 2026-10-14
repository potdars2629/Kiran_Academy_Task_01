
# Kiran Academy - Task 01
# Shopping Bill - GST First, Discount After

def calculateElectronicsGST(a, b):
    total = a + b
    return total + (total * 18 / 100)


def calculateFashionGST(c, d):
    total = c + d
    return total + (total * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100

    return total - discount


# Main Program
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_bill = calculateDiscountedBill(a, b, c, d, e)

print("----- SHOPPING BILL -----")
print(f"Total after GST = Rs.{total:.2f}")
print(f"Discount = Rs.{discount:.2f}")
print(f"Final payable amount = Rs.{final_bill:.2f}")
