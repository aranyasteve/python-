
# 1000 0%
# 2000 5%
# 3000 10%
# 5000 15%
# more then 5000  20%
shopping_amt = int(input("enter shopping amount :"))
if shopping_amt < 0:
    shopping_amt = discount_amt = payable_amt = 0
    print('Shopping amount not valid ! ')
elif shopping_amt < 1000:
    discount_amt = shopping_amt * 0
    payable_amt = shopping_amt - discount_amt
elif shopping_amt < 2000:
    discount_amt = shopping_amt * 0.05
    payable_amt = shopping_amt - discount_amt
elif shopping_amt < 3000:
    discount_amt = shopping_amt * 0.10
    payable_amt = shopping_amt - discount_amt
elif shopping_amt < 5000:
    discount_amt = shopping_amt * 0.15
    payable_amt = shopping_amt - discount_amt
else:
    discount_amt = shopping_amt * 0.20
    payable_amt = shopping_amt - discount_amt

print("***************************************************")
print("The Shopping Amount is  : {}".format(shopping_amt))
print("The Discount Amount is  : {}".format(discount_amt))
print("The Payable  Amount is  : {}".format(payable_amt))
print("***************************************************")