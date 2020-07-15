# bounce.py
#
# Exercise 1.5


originalValue = 60

print("1 " + str(float(originalValue)))

for i in range(2,11):
	originalValue = originalValue*(3/5)
	print(str(i) + " " + str(round(originalValue, 4)))