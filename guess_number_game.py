class GuessNumber:
	def __init__(self, number, mn=0, mx=100):
		self.number = number
		self.min = mn
		self.max = mx
		self.guess = 0

	def get_guess(self):
		guess = input(f'guesss a number between {self.min} and {self.max}: ')

		if self.valid_number(guess):
			return int(guess)
		else:
			print('please provide a valid number')
			return get_guess()

	def valid_number(self, str_number):
		try:
			number = int(str_number)
		except:
			return False

		return self.min <= number <= self.max


	def play(self):
		while True:
			self.guess += 1
			guess = self.get_guess()

			if guess < self.number:
				print('guess bigger')
			elif guess > self.number:
				print('guess lower')
			else:
				break
		print(f"you guess it in {self.guess} times")



if __name__ == '__main__':
	game = GuessNumber(50)
	game.play()


