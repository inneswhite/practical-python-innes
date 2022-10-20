bill_thickness = 0.11 * 0.01
sears_height = 442
num_bills = 1
day = 1
currentBillHeight = 0.11 * 0.01

while currentBillHeight <= sears_height:
    currentBillHeight = num_bills * bill_thickness
    day += 1
    num_bills = num_bills * 2
print('The total number of bill requires is ', num_bills)
print(' in a total number of ', day, 'days')
#this is a comment



