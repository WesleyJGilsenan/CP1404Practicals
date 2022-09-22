"""CP1404: Prac 1 Sales Bonus | Wesley Gilsenan"""

"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

sales = float(input("Enter sales: "))
while sales >= 0:
    if sales < 1000:
        bonus = (sales / 100) * 10
        print(f"User bonus is ${bonus:.2f}")
        sales = float(input("Enter sales: "))
    if sales >= 1000:
        bonus = (sales / 100) * 15
        print(f"User bonus is ${bonus:.2f}")
        sales = float(input("Enter sales: "))
print("error")