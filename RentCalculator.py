#This is a Rent calculator where we will calulate our monthly expenses like
#House rent , Electricity bill , food ,water bill,Total bill, Bill per person

person=int(input("Total person in your house: "))
rent=int(input("Enter your House Rent: "))
food=int(input("Enter your bill of food: "))
water=int(input("Enter your bill of water: "))
electricity_spend=int(input("Enter your total electricity spended: "))
charge_per_unit=int(input("Enter your charge per unit: "))
electricity_bill= electricity_spend*charge_per_unit

total=rent+food+water+electricity_bill
per_person=total//person


print("Per person Bill is :" , per_person)