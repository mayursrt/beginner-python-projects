#----------------------------------------------------------------------------------------------------------------------------
# Imports
from words import words
import random
import string
from hangman_visual import lives_visual_dict
#----------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------
# Body

def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()

def hangman():
	word = get_valid_word(words)
	word_letters = set(word)
	used_letters = set()
	alphabet = set(string.ascii_uppercase)

	lives = 7


	while len(word_letters) > 0 and lives > 0:
		print(f'You have {lives} lives left. You have used these letters: ', ' '.join(used_letters))

		word_list = [letter if letter in used_letters else '_' for letter in word]
		print(lives_visual_dict[lives])
		print('Current Word: ', ' '.join(word_list))

		user_letter = str(input('Enter an Alphabet: ').upper())
		
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			
			else:
				lives -= 1
				print('Letter is not in the word.')


		elif user_letter in used_letters:
			print('You\'ve already used this letter. Please try another one.')

		else:
			print('Invalid Character. Please try again.')
	if lives == 0:
		print(lives_visual_dict[lives])
		print(f'Sorry, you lost!! You have 0 lives remaining. The word was {word}')
	else:
		print(f'Congratulations you guessed the word correctly. The word is {word}')

hangman()

#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input

#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function

#----------------------------------------------------------------------------------------------------------------------------






############################################################################################################################# 
#############################################################################################################################
