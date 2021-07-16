#----------------------------------------------------------------------------------------------------------------------------
# Imports
import random
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
# User Input
print("""
   ___           __     ___                      ____    _                    
  / _ \___  ____/ /__  / _ \___ ____  ___ ____  / __/___(_)__ ___ ___  _______
 / , _/ _ \/ __/  '_/ / ___/ _ `/ _ \/ -_) __/ _\ \/ __/ (_-<(_-</ _ \/ __(_-<
/_/|_|\___/\__/_/\_\ /_/   \_,_/ .__/\__/_/   /___/\__/_/___/___/\___/_/ /___/
                              /_/                                             
	""")


def play():
	dic = {'r' : 'rock',
			'p' : 'paper',
			's' : 'scissors'}
	while True:
		user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
		computer = random.choice(['r', 'p', 's'])

		if user == 's' or user == 'r' or user == 'p':
			if user == computer:
				print(f'The computer chose {dic[computer]}')
				return "It's a tie!!"

			if is_winner(user, computer):
				print(f'The computer chose {dic[computer]}')
				return "Congratulations!! You won."

			print(f'The computer chose {dic[computer]}')
			return 'Sorry!! You lost.'
		else:
			print('Please choose a valid response')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function

def is_winner(player, oppopnent):
	if (player == 'r' and oppopnent == 's') or (player == 's' and oppopnent == 'p') or (player == 'p' and oppopnent == 'r'):
		return True
#----------------------------------------------------------------------------------------------------------------------------

print(play())
