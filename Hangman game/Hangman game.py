import sys
import os
import random

sys.path.append(os.path.abspath('game_files'))
from words_hangmangame import words

hangman_art = {0: ('   ', 
	               '   ', 
	               '   '),
               1: (' o ', 
	               '   ', 
	               '   '), 
               2: (' o ', 
	               ' | ', 
	               '   '), 
               3: (' o ', 
	               '/| ', 
	               '   '),
               4: (' o ', 
	               '/|\\', 
	               '   '),
               5: (' o ', 
	               '/|\\', 
	               '/  '),
               6: (' o ', 
	               '/|\\', 
	               '/ \\')}

def show_word(displayed_word):
	print('Mystery word: ' + ' '.join(displayed_word).upper())
	while True:
		guess = input('Enter your guess (1 letter): ').lower()
		if len(guess) != 1 or not guess.isalpha():
			print('Invalid guess. Has to be 1 letter!')
			continue
		if guess in displayed_word:
			print(f'\'{guess}\' is already guessed!')
			continue		
		return guess
		break

def guess_check(guess, answer, displayed_word):
	if guess in answer:
		for i in range(len(answer)):
			if answer[i] == guess:
				displayed_word[i] = guess
		print('CORRECT! <3')
		return 0
	else:
		print('INCORRECT! :(')
		return 1

def hangman_display(num_mistakes):
	for art in hangman_art[num_mistakes]:
		print(' ' + art)


def main():
	num_mistakes = 0
	answer = random.choice(words)
	displayed_word = ['_'] * len(answer)

	print('< Welcome to Python Hangman! >')
	print()

	while True:
		guess = show_word(displayed_word)
		num_mistakes += guess_check(guess, answer, displayed_word)
		print()
		print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
		hangman_display(num_mistakes)
		print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
		print()

		if '_' not in displayed_word:
			print('YOU WON!')
			break
		if num_mistakes == 6:
			print('YOU LOST!')
			break

	print(f'Word: {answer.upper()}')
	print(f'Number of mistakes: {num_mistakes}')
	print('Thanks for playing Python Hangman!')


if __name__ == '__main__':
	main()