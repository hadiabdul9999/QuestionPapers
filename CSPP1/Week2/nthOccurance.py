#**********************************************************************************************************#
#Level 1: 25 Marks
#Question2:
#	Given a number N and two strings S1 and S2, find the index at which the string S2 occurs in S1 for the
# Nth time. If there is no such index then return -1.
#**********************************************************************************************************#








#*************************************************************************************************************#
#*		DO NOT WRITE/MODIFY CODE BELOW THIS LINE. ANY CHANGES MAY CAUSE YOUR HIDDEN TEST CASES TO FAIL 		*#
#*				YOU MAY USE THE SPACE PROVIDED ABOVE TO WRITE YOUR PROGRAM. ALL THE BEST!					*#
#*************************************************************************************************************#

def test_nthOccurence():
	
		assert(nthOccurence("AAAAAAAAAB","AAB",1))==7
	
		assert(nthOccurence("AAEFA","AA",2))==-1

		assert(nthOccurence("ABRACADABRA","A",5))==10

		print("All the test-cases have passed")

test_nthOccurence()