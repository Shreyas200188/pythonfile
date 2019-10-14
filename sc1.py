answ = int(input("How many words have you written for your term paper ? "))
if answ >= 1500 :
	print("Great, you've done your homework. Enjoy the beach!")
else :
	print("Sorry, you must stay home and work on your term paper")

bags = int(input("How many bags of leaves did you fill this month? "))
if bags > 10:
	print("Great, you made $",bags*3 + 20)
else :
	print("Great, you made $",bags*3)

gpa = float(input("Enter your gpa : "))
if (gpa >= 3.0  and gpa <= 3.5) :
	print("Great you will get Wii for your good grades")
elif (gpa > 3.5 and gpa <= 3.8) :
	print("Great you will get Kinect for your good grades")
elif (gpa >3.8) :
	print("Great you will get PlayStation3 for your good grades")
else :	
	print("Sorry you won't get a game system")

answ1 = input("Did you bring back you signed permission slip (yes/no)? ")
if answ1 == "yes":
	answ2 = input("Who was the leader of Germany in WWII (last name only)? ")
	if answ2 == "Hitler":
		print("You will get to go the history museum!")
	else :
		print("You will get to go the art museum!")
else :
	print("Sorry, you aren't allowed to go on the field trip.")

sat = int(input("What is your SAT score? "))
gpa = float(input("What is your GPA ? "))
if ( sat >= 1100 and gpa >= 3.0) :
	print("Great, you qualify for the scholarship!")
else :
	print("Sorry, you don't qualify for the scholarship")


sat = int(input("What is your SAT score? "))
gpa = float(input("What is your GPA? "))
if (sat >= 1250 or gpa >= 3.6):
	print("Great, you qualify for the Honours Diploma!")
else :
	print("Sorry, you don't qualify for the Honours Diploma")

name_a = input("Runner @1, what is your name? ")
time_a = float(input("What was your time? "))
name_b = input("Runner @2, what is your name? ")
time_b = float(input("What was your time? "))
name_c = input("Runner @3, what is your name? ")
time_c = float(input("What was your time? "))
if ( time_a > time_b and time_a > time_c) :
	print("The winner of the race was ",name_a," !")
elif( time_b > time_a and time_b > time_c) :
	print("The winner of the race was ",name_b," !")
else :
	print("The winner of the race was ",name_c," !")


name = input("What is the employee's name? ")
payrate = float(input("What is the employee's pay rate ($/hr)? "))
hours = float(input("How many hours did the employee work this week? "))
if hours <= 40:
	print(name," gets paid ",hours*payrate," this week.")
else :
	extrah = hours-40
	print(name," gets paid ",40*payrate + extrah*payrate*1.5," this week.")

word = input("Enter 4 letter word : ")
count = 0
if word[0:2] == "NI":
	print("Yes it contains NI at first position")
	count = count + 1
if word[1:3] =="NI" :
	print("Yes it contains NI at second position")
	count = count + 1
if word[2:4] == "NI" :
	print("Yes it contains NI at third position")
	count = count + 1
print("No. of times NI occurs = ",count)

num = input("3-digit number = ")
first = num[0]
second= num[1]
third = num[2]
answ = num[2]+num[1]+num[0]
print("Reversed = ",answ)

side1 = float(input("First side of triangle= "))
side2 = float(input("Second side of triangle= "))
side3 = float(input("Third side of traingle= "))
if ( side1 + side2 >= side3 and side2 + side3 >= side1 and side3 + side1 >= side2) :
	print("Triangle exists")
else :
	print("Triangle does not exist")


dist = int(input("Enter distance: "))
cost = 0.0
if dist > 0 and dist <= 100 :
	cost = 5.0
elif dist > 100 and dist < 500 :
	cost = 8.0
elif dist > 500 and dist < 1000 :
	cost  = 10.0
elif dist >= 1000 :
	cost = 12.0
else :
	cost = 0
