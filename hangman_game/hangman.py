#----------------------------------------------------------------------------------------------------------------------------
# Imports
from words import words
import random
#----------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------
# Body

def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()


random_phrase = get_valid_word(words)
print(random_phrase)
print(random.choice(words))
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input

#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function

#----------------------------------------------------------------------------------------------------------------------------






############################################################################################################################# 
#############################################################################################################################
