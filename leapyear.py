#Leap year checker
#Oliver Borowski



#init
#functions
def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0):
        if year % 100 == 0:
            print("not a leap year")
        else:
            print("leap year")
#main

leap_year(2024)#True
leap_year(1900)#False
leap_year(1600)#True
