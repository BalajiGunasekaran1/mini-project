#function to calculate the BMI on the height and weight inputs by user.

def bmi(height,mass):
	b_index = mass/(height**2)
	return round(b_index,2)
loop="y"
while(loop=='y' or loop=='Y'):
	
	height = float(input("Enter the height in meters:"))
	mass = float(input("Enter the weight in kg:"))
	b_index = bmi(height,mass)
	print("Your BMI is:","{}".format(b_index))
	if(b_index<18.5):
		print("Underwieght")
	elif(b_index>=18.5 and b_index<=24.9):
		print("Normal Weight")
	elif(b_index>=25.0 and b_index<=29.9):
		print("Over Weight")
	elif(b_index>30.0):
		print("Obesity")
	print("Do you want to continue(y/n): ")
	loop=input()

