import time 
import random

def reaction_time_test():
    print("Reaction Time Tester")
    print("Instructions: Press Enter as quickly as you can after seeing 'Go!'.")

    while True:
        input("Press 'Enter' to begin!")

        #Random wait time between 4 and 9 seconds
        wait_time = random.uniform(4, 9)
        time.sleep(wait_time)

        print("Go!")
        start_time = time.time()
        input()
        end_time = time.time()

        reaction_time = end_time - start_time
        print(f"Reaction Time: {reaction_time:.3f} seconds")

        #Ask if the user wants to try again
        try_again = input("Would you like to try again? (Yes / No): ")
        if try_again.lower() != 'Yes':
            break

if __name__ == "__main__":
    reaction_time_test()
