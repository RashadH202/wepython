print("Welcome to tip calculator!")
bill = float(input("what was the total bill? $"))

#check
print(type(bill))

tip = int(input("How much tip would like to give? 10, 12, 15? just a number please!"))

people = int(input("how many people to split the bill?"))

bill_with_tip = bill * (1 + tip / 100 )
print(bill_with_tip)


bill_per_person = bill_with_tip / people

final_amount = round(bill_per_person, 2)
final_amount = "{:2f}".format(bill_per_person)

print(f"each person should pay: ${final_amount}")
