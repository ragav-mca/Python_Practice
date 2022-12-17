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
    commission = 13/100 * 10 
    print("Commission:",commission)
else:
    print("No Commission")
if(phone_sold >= 10 and exp >= 1 and leave_count >=1):
   total_pay = base_pay * commission + increment - lop
   print("Total amount of salary:",total_pay)
else:
    print("Total amount of salary:",base_pay)

Output:
Enter the year of experience: 1
Enter the no of days leave: 2
Loss of pay is:  400
Increment: 2000
Enter the no of phones sold: 30
Commission: 1.3
Total amount of salary: 14600.0
