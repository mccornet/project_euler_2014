""" Euler 96 - Su Doku

The 6K text file, sudoku.txt, contains fifty different 
Su Doku puzzles ranging in difficulty, but all with unique 
solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit 
numbers found in the top left corner of each solution grid; 
for example, 483 is the 3-digit number found in the 
top left corner of the solution grid above.
"""

class Soduko:
	""" Sudoku Class """
	puzzle = [0]*(82) # 9 rows * 9 cols +1 index offset

	def load(self, input_array):
		""" Copy data into internal storage 
			Len of data should be 81! """
		self.puzzle[1:] = input_array

	def print(self): 
		print(self.puzzle[1:10])
		print(self.puzzle[10:19])
		print(self.puzzle[19:28])
		print(self.puzzle[28:37])
		print(self.puzzle[37:46])
		print(self.puzzle[46:55])
		print(self.puzzle[55:64])
		print(self.puzzle[64:73])
		print(self.puzzle[73:82])

	def solve(self):
		""" Solves soduko recursivly """
		# 1. Find next empy square:
		empty_sq = self.next_empty_square()

		# 2. Done when no more empty square found
		if empty_sq == 0: return True 

		# 3. Try all possible values
		for value in range(1,10):
			# 3.1 Fill in value
			self.puzzle[empty_sq] = value

			# 3.2 Check if value possible and solves in recursion
			if self.valid(empty_sq): # not invalid
				# try recursion
				if self.solve() : return True

		# 4. If it did not work, empty square and return
		self.puzzle[empty_sq] = 0
		return False

	def sum_pe_96(self):
		""" returns the sum of the first three squares """
		return self.puzzle[1]*100 + self.puzzle[2]*10 + self.puzzle[3]

	def valid(self, square):
		""" Checks if puzzle can be valid for the given square"""

		# calculate row
		# NB: rows 0,1,2, ..., 8
		row = (square-1)//9 
		row_start = 1 + 9*row
		row_end   = 10 + 9*row # one extra for range behaviour
		
		# test row
		row_values = [0] * 10
		for sq in range(row_start,row_end,1):
			test_value = self.puzzle[sq]
			if row_values[test_value] != 0: 
				return False
			else: row_values[test_value] = test_value

		# calculate column
		# NB: cols 0,1,2, ..., 8
		col = square - 9*row - 1
		col_start = 1 + col
		col_end= 74 + col # one extra for range behaviour

		# test column
		col_values = [0] * 10
		for sq in range(col_start,col_end,9):
			test_value = self.puzzle[sq]
			if col_values[test_value] != 0:
				return False
			else: col_values[test_value] = test_value

		# calculate and test panel
		offset = (col//3)*3 + (row//3)*27
		pan_values = [0] * 10
		for i in range(1,4):
			for j in range(0,3):
				sq = i + j*9 + offset
				test_value = self.puzzle[sq]
				if pan_values[test_value] != 0:
					return False
				else: pan_values[test_value] = test_value

		# we found no invalid values
		return True

	def next_empty_square(self):
		""" Returns index of the first empty square """
		# 1. Try to find empty square
		for square in range(1, 82): # length puzzle data + 1
			if self.puzzle[square] == 0: return square

		# 2. No empty square found
		return 0

# 1: Read sodukos
sudokus = []

# sudoku file into idividual lines
lines = [line.rstrip('\n') for line in open("sudoku.txt")]

# filter sudokus
start = 0
while start < len(lines):
	sudokus.append([int(char) for char in ''.join(lines[start+1:start+10])])
	start+=10

# 2: Solve sudokus and add count
mySudoku = Soduko()
total_count = 0
nr = 1
for sudoku in sudokus:
	print("Solving: {}".format(nr))
	mySudoku.load(sudoku)
	mySudoku.solve()
	total_count += mySudoku.sum_pe_96()
	nr += 1

#3 print total count
print(total_count)

