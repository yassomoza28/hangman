import random

with open('/storage/emulated/0/scripts/words.txt', 'r') as f :
	words = f.readlines()
	
word = random.choice(words)[:-1:]

allowed_errors = 6
guesses = []
done = False

while not done :
	for letter in word :
		if letter in guesses :
			print(letter,end = ' ')
		else :
			print('_',end = ' ')
	print(' ')
	
	guess = input('next guess ')
	guesses.append(guess)
	if guess not in word :
		allowed_errors-=1
		if allowed_errors  == 0 :
			break
		
	done = True
	for letter in word :
		if letter not in guesses :
			done = False
			
if done :
	print('you won it was ',(word))
else :
	print('game over the word was ',(word))