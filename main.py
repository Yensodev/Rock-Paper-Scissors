import random

options = ["R", "P", "S"]

def run():

    while(True):

        print("\nPick an option:\n")
        print('"R" for rock')
        print('"P" for paper')
        print('"S" for scissors\n')
        
        player_option = input("Your option: ").upper()

        if player_option not in options:
            print("\nError: Invalid option. Try again.")

        else: break

    CPU_option = random.choice(options)

    print(f"\nPlayer {player_option} : CPU {CPU_option}")


    if player_option == CPU_option:
        print("\nIt's a tie!!")
        run()
    
    else: print_winner(player_option, CPU_option)




def print_winner(player, CPU):
    if player == "R" and CPU == "S":
        print("Player wins!!")
    
    elif player == "R" and CPU == "P":
        print("CPU wins!!")

    elif player == "S" and CPU == "R":
        print("CPU wins!!")

    elif player == "S" and CPU == "P":
        print("Player wins!!")

    elif player == "P" and CPU == "R":
        print ("Player wins!!")

    elif player == "P" and CPU == "S":
        print("CPU wins!!")



run()
