#**********************************************************************************************************#
#Level 2: 50 Marks
#Question3:
#	A student has solved some random sudoku puzzles and wants you to check whether his answers are correct or
#	not. Write a function that takes a 9x9 sudoku as an input and checks whether it is correct or not.
#	The sudoku is said to be correct when it satisfies four rules:
#		Rule 1: All the rows should have unique numbers in them.
#		Rule 2: All the columns should have unique numbers in them.
#		Rule 3: All the blocks should have unique numbers.
#		Rule 4: No box should be empty.
#	Refer image "sudoku.png" to understand what row, column and box are.
#**********************************************************************************************************#








#*************************************************************************************************************#
#*		DO NOT WRITE/MODIFY CODE BELOW THIS LINE. ANY CHANGES MAY CAUSE YOUR HIDDEN TEST CASES TO FAIL 		*#
#*				YOU MAY USE THE SPACE PROVIDED ABOVE TO WRITE YOUR PROGRAM. ALL THE BEST!					*#
#*************************************************************************************************************#

def test_sudoku():
	
		assert(sudoku([[2,9,5,7,4,3,8,6,1],[4,3,1,8,6,5,9,2,7],[8,7,6,1,9,2,5,4,3],[3,8,7,4,5,9,2,1,6],[6,1,2,3,8,7,4,9,5],[5,4,9,2,1,6,7,3,8],[7,6,3,5,3,4,1,8,9],[9,2,8,6,7,1,3,5,4],[1,5,4,9,3,8,6,7,2]]))=="Correct"
		
		assert(sudoku([[1,2,3,7,8,9,4,5,6],[4,5,6,1,2,3,7,8,9],[7,8,9,4,5,6,1,2,3],[2,3,1,8,9,7,5,6,4],[5,6,4,2,3,1,8,9,7],[8,9,7,5,6,4,2,3,1],[3,1,2,9,7,8,6,4,5],[7,4,5,3,1,2,9,7,8],[9,7,8,6,4,5,3,1,2]]))=="There is a mistake in the puzzle"

		assert(sudoku([[2,9,5,7,4,3,8,6,1],[4,3,1,8,6,5,9,2,7],[8,7,6,1,9,2,5,4,3],[3,8,7,4,5,9,2,1,6],[6,1,2,3,8,7,4,9,5],[5,4,9,2,1,6,7,3,8],[7,6,3,5,3,4,1,8,9],[0,2,8,6,7,1,3,5,4],[1,5,4,9,3,8,6,7,2]]))=="Illegal values found in the puzzle"
		
		print("All the test-cases have passed")

test_sudoku()