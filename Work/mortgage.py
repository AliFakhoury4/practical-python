# mortgage.py
#
# Exercise 1.11

principal = 500000.0
rate = 0.05
total_paid = 0.0
payment = 2684.11
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

updated_payment = payment + extra_payment

while principal > 0:
	if (month >= extra_payment_start_month and month <= extra_payment_end_month):
		if(principal * (1+rate/12) - updated_payment < 0):
			total_paid = total_paid + principal
			principal = 0
		else:
			principal = principal * (1+rate/12) - updated_payment
			total_paid = total_paid + updated_payment
		
		print(str(month) + " " + str(round(total_paid,2)) + " " + str(round(principal, 2)))
	else:
		if(principal * (1+rate/12) - payment < 0):
			total_paid = total_paid + principal
			principal = 0
		else:
			principal = principal * (1+rate/12) - payment
			total_paid = total_paid + payment
		
		print(str(month) + " " + str(round(total_paid,2)) + " " + str(round(principal, 2)))

	month += 1
	
print(month-1)

print('Total paid', round(total_paid, 1))