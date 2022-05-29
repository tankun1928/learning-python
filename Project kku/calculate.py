import time
import random
import webbrowser

username = ''
answer = 0
score = 0
FILE_NAME = 'calc_leaderboard.txt'

def get_random_expression(num): # @TODO implement if there's available time
	pass
# current_time = time.time()

# final_time = time.time()
# interval = final_time - current_time

# print(current_time)

# def countdown(time_down):
# 	while time_down:
# 		mins, secs = divmod(time_down, 60)
# 		format_time = '{:02d}:{:02d}'.format(mins, secs)
# 		print(format_time, end='\r')
# 		time.sleep(1)
# 		time_down -= 1
MAX_TIMES = 5

def setting_game():
	global username
	while True:
		username = input("Username: ")
		print("Hello " + username)
		score = 0 # @TODO need to implement
		print("\nAre You Ready")
		player_answer = input("Yes or No: ")
		if player_answer.lower() == "yes":
			break
		elif player_answer.lower() == "no":
			print("-------------------")
		else :
			print("I Told You \"Yes OR No\"👊👊👊")

def play():
	while True:
		num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		num1 = random.choice(num_list)
		num2 = random.choice(num_list)
		op_list = ["+", "-", "*", "/"]
		op1 = random.choice(op_list)
		print("You Have 5 sec to answer")
		print(num1, op1, num2)
		if op1 == "+":
			result = num1 + num2
		elif op1 == "-":
			result = num1 - num2
		elif op1 == "*":
			result = num1 * num2
		elif op1 == "/":
			result = num1 / num2 # @TODO fix ZeroDivisionError
		else:
			print("-Wrong Operation-")
		result = round(result, 2)
		current_time = time.time()
		answer = float(input("Answer: "))
		final_time = time.time()
		interval = final_time - current_time
		if answer == result and interval < MAX_TIMES:
			print("--You Won This Round🥳🥳🥳--")
			update_score(answer, result)
		elif interval > MAX_TIMES and answer == result:
			print("Time Exceeded")
			update_score(answer, result)
			write_score()
			print('YOU ARE LOSE!')
			print('THIS IS YOUR PUNISHMENT!!!')
			time.sleep(2)
			print('...')
			time.sleep(2)
			print('.....')
			webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
			break
		elif answer != result and interval < MAX_TIMES:
			print("Wrong Answer🤞🤞")
			update_score(answer, result)
			write_score()
			print('YOU ARE LOSE!')
			print('THIS IS YOUR PUNISHMENT!!!')
			time.sleep(2)
			print('...')
			time.sleep(2)
			print('.....')
			webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
			break
		elif answer != result and interval > MAX_TIMES:
			print("Wrong Answer🤞🤞 And Time Exceeded")
			update_score(answer, result)
			write_score()
			print('YOU ARE LOSE!')
			print('THIS IS YOUR PUNISHMENT!!!')
			time.sleep(2)
			print('...')
			time.sleep(2)
			print('.....')
			webbrowser.open('https://www.youtube.com/watch?v=DWtpNPZ4tb4')
			break
		print()
		print("Time In This Round ", int(interval), "Secs")
		print()

def count_to_ready():
	print("----Approximate answer to 2 decimal places.----")
	print(3)
	time.sleep(1)
	print(2)
	time.sleep(1)
	print(1)

def read_score():
	print('────── •✧✧• ─────-Your Score-───── •✧✧• ──────')
	print(f'{username:>12}{score:>25}')

def update_score(player_ans, result):
	global score
	if player_ans == result:
		score += 1
	print(f"Your score is {score}")

def write_score():
	with open(FILE_NAME, 'a') as file:
		file.write(f'{username} {score}\n')

def update_sorted_score():
	temp_dict = {}
	with open(FILE_NAME, 'r') as file:
		for line in file.readlines():
			line = line.strip()
			key, value = line.split()
			temp_dict[key] = int(value)

	sorted_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1], reverse=True))
	with open(FILE_NAME, 'w') as file:
		for key in sorted_dict:
			file.write(f'{key} {sorted_dict[key]}\n')

	print_dict(sorted_dict)

def print_dict(arg_dict):
	for key in arg_dict:
		print(f'{key:>12}{arg_dict[key]:>25}')


def main():
	global score
	print("""░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝  ██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗""")

	print()
	print()
	setting_game()
	count_to_ready()
	play()
	print("-----------------------------------------")
	while True:
		cmd_score = input('Do you want to see score? [yes/no]: ')
		if cmd_score.lower() == 'yes':
			read_score()
		play_choice = input("Wanna Play More? [yes/no]: ")
		if play_choice.lower() == "yes":
			score = 0
			setting_game()
			count_to_ready()
			play()
			print("-----------------------------------------")
		elif play_choice.lower() == "no":
			print('Bye bye!!!👋👋')
			print()
			print('------------------------------------------------')
			print('────── •✧✧• ─────-scoreboard-───── •✧✧• ──────')
			update_sorted_score()
			break


if __name__ == '__main__':
	main()




