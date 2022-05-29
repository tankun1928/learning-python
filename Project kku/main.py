import calculate
import rps

def main():
    while True:
        print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝


""")
        user_cmd = input('What game do you want to play? [CALC/RPS] or [EXIT]: ')
        if user_cmd.lower() == "rps":
            rps.main()
        elif user_cmd.lower() == "calc":
            print()
            print()
            calculate.main()
        elif user_cmd.lower() == 'exit':
            print('Bye bye')
            exit(0)
       

if __name__ == '__main__':
    main()
# while True:
#     user_play_more = input("Wanna Restart?[yes/no]: ")
#     if user_play_more.lower() == "yes":
#         main()
#     elif user_play_more.lower() == "no":
#         break