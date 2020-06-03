import random

rps_list = ['ROCK', 'PAPER', 'SCISSORS']

stats_count = {'player': 0, 'computer': 0, 'ties': 0}

who_can_defeat_who = [('ROCK', 'SCISSORS'),
                      ('SCISSORS', 'PAPER'),
                      ('PAPER', 'ROCK')]


def main_menu():
    while True:

        option = input(
            "                    Welcome To The Rock Paper Scissors Game                      "
            "\n-------------------------------------------------------------------------------"
            "\n                                  OPTIONS                                      "
            "\n-------------------------------------------------------------------------------"
            "\n[1] - Rock Paper Scissors                                                      "
            "\n[2] - Exit                                                                     "
            "\n-------------------------------------------------------------------------------"
            "\n Please select an option (1 or 2): ")

        if option == '1':
            play(option)
        elif option == '2':
            print("Good Bye")
            exit()
        else:
            input("Invalid option. Try again... Please press ENTER to continue")


def play(option):
    if option == '1':
        print("\n Welcome to Rock, Paper, Scissors game!")
        print("\n You can choose between Rock, Paper or Scissors."
              "\n The first one that scores 3 points WINS the game! ")

    elif option == '2':
        print("Good Bye")
        exit()

    while True:

        rps_input = input("\n Type either Rock, Paper or Scissors: "
                          "\n Please Type The First Letter In Uppercase")

        rps_input = rps_input.upper()

        cpu_list = random.choice(rps_list)

        match = rps_input, cpu_list

        print(f"\n The computer choose:  {cpu_list} ")

        print(f"\n You choose:  {rps_input} ")

        if rps_input == cpu_list:
            stats_count['ties'] += 1
            print("\n No one won its a tie")
            print("\n-------  STATS  -------"
                  "\n YOU  | COMPUTER | DRAW"
                  "\n  {player}        {computer}        {ties}"
                  "\n-----------------------".format(**stats_count))

        elif match in who_can_defeat_who:
            stats_count['player'] += 1
            print("\nResult: The power of {} beats {}! You won that round!".format(rps_input, cpu_list))

            print("\n-------  STATS  -------"
                  "\n YOU  | COMPUTER | DRAW"
                  "\n  {player}        {computer}        {ties}"
                  "\n-----------------------".format(**stats_count))

        else:
            stats_count['computer'] += 1

            print("\nResult: The power of {} beats {}! You lost that round!".format(cpu_list, rps_input))

            print("\n-------  STATS  -------"
                  "\n YOU  | COMPUTER | DRAW"
                  "\n  {player}        {computer}        {ties}"
                  "\n-----------------------".format(**stats_count))

        if stats_count['player'] == 3:
            print("\n You won and the COMPUTER lost")
            exit()

        elif stats_count['computer'] == 3:
            print("\n The computer won and YOU lost")
            exit()


main_menu()
