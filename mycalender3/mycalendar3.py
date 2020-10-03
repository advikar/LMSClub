#This is my school calendar code that I wrote using a function
def printCalendar():
	lmsclub3 = '''Day     Time            Subject
                Monday  9:10-10:15 AM   Math
                        10:35-11:40 AM  Science
                        11:40-12:10 AM  Wheel
                Tuesday 9:10-10:15 AM   P.F.
                        10:35-11:40 AM  S.S.
                        11:40-12:10 AM  L.A.'''

#printing lmsclub3 inside function in uppercase letters	
	print (lmsclub3.upper()) 

#Checking if code has "Monday"
	if "Monday" in lmsclub3:
		print("Monday is present")

	else:
   		print("Monday is not present")

#Calling function to print my calendar code
printCalendar()
