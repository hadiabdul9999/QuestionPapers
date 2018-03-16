#**********************************************************************************************************#
#Level 0: 25 Marks
#Question1:
#	Write a function 'Statistics' that takes a list of numbers as an input and calculates the mean, median 
#	and mode.
#**********************************************************************************************************#








#*************************************************************************************************************#
#*		DO NOT WRITE/MODIFY CODE BELOW THIS LINE. ANY CHANGES MAY CAUSE YOUR HIDDEN TEST CASES TO FAIL 		*#
#*				YOU MAY USE THE SPACE PROVIDED ABOVE TO WRITE YOUR PROGRAM. ALL THE BEST!					*#
#*************************************************************************************************************#
def test_statistics():
	
		assert(statistics([1,1,1,1,2,1,1,1,1])) == "mean = 1;median = 1;mode = 1"
		
		assert(statistics([3,3,8,2,4,3,2,1]))=="mean = 3;median = 3;mode = 3"
		
		assert(statistics([2,4,6,8,10,10,8,6,4,2]))=="mean = 6; median = 6; mode = 2,4,6,8,10"

		print("All the test-cases have passed")

test_statistics()
