#Same as above. For each day the salesman doesn't go to work, subtract Rs200 from the total pay.

base_pay = 10000
exp = int(input("Enter the year of experience: "))
leave_count = int(input("Enter the no of days leave: "))
lop = leave_count * 200
print("Loss of pay is: ",lop)
if(exp >= 1):
   increment = exp * 2000
   print("Increment:",increment)
else:
    print("No Increment")
phone_sold = int(input("Enter the no of phones sold: "))
if(phone_sold >= 10):
    x = phone_sold / 10
    y = 13/100 * x 
    commission = x + y
    print("Commission:",commission)
else:
    print("No Commission")
if(phone_sold >= 10 or exp >= 1 or leave_count >=1):
   total_pay = base_pay * commission + increment - lop
   print("Total amount of salary:",total_pay)
else:
    print("Total amount of salary:",base_pay)