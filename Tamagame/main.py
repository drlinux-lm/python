import os
from rng import rng
from engine import engine
from printer import printer

## Start with cleaned up console
os.system("clear")

def main():
    win = loss = 0
    bet = None
    
    while True:
        tamago = rng(1, 9)
        
        print(f"Tamagotchi:\t{tamago}")

        try:
            while True:
                bet = input("Greater 'g', Less 'l' or Quit 'x': ")
                if bet.lower() not in ["g", "l", "x"]:
                    print("Invalid key. Please try again.")
                else:
                    break
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting gracefully.")
            break

        if bet.lower() == "x":
            print("Quiting game")
            break

        if engine(tamago, bet):
            win += 1
        else:
            loss += 1
        accuracy = round(win / (win + loss) * 100, 1)
        print(f"\nWins: {win}, Losses: {loss}, Accuracy: {accuracy}%")

        try:
            input("\nPress return to continue...")
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting gracefully.")
            break
        os.system("clear")

if __name__ == '__main__':
    main()