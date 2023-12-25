###################################################################################
# Required Python Packages
###################################################################################
import random

###################################################################################
# Function Name : main
# Description : main function where execution gets start
# Author : Akash Atul Kank
# Date : 29/11/2023
###################################################################################
def main():
    print("Winning Rules of the game ROCK PAPER SCISSORS are : \n"
          + "Rock vs Paper -> Paper Wins \n"
          + "Rock vs Scissor -> Rock Wins \n"
          + "Paper vs Scissor -> Scissor Wins \n")
    
    while True:
        print("Enter Your Choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor \n")

        # Input from User
        try:
            choice = int(input("Enter your Choice : "))

        except Exception as zobj:
            print("Exception occures as : ",zobj)
            return


        while choice > 3 or choice < 1:
            print("Invalid Input \n")

            try:
                choice = int(input("Enter a Valid Choice Plaese : "))
            
            except Exception as zobj:
                print("Exception Occures as : ",zobj)

        if choice == 1:
            choice_name = "Rock"
        elif choice == 2:
            choice_name = "Paper"
        else:
            choice_name = "Scissor"

        #elif choice == 3:
            #choice_name == "Scissor"

        print("User Choice is \n",choice_name)
        print("Now it's Computers Turn......")

        comp_choice = random.randint(1,3)

        while comp_choice == choice:
            comp_choice = random.randint(1,3)

        if comp_choice == 1:
            comp_choice_name = "rocK"
        elif comp_choice == 2:
            comp_choice_name = "papeR"
        else:
            comp_choice_name = "scissoR"

        print("Computer Choicen is : \n",comp_choice_name)
        print(choice_name, "VS" ,comp_choice_name)

        if(choice == comp_choice):
            print("It's Draw",end="")
            Result = "DRAW"

        # Condition for Paper Winning
        if(choice == 1 and comp_choice == 2):
            print("Paper Wins => ",end="")
            Result = "papeR"
        elif(choice==2 and comp_choice==1):
            print("Paper Wins => ",end="")
            Result = "Paper"

        # Condition for Rock Winning
        if(choice == 1 and comp_choice == 3):
            print("Rock Wins => ",end="")
            Result = "Rock"
        elif(choice == 3 and comp_choice == 1):
            print("Rock Wins => ",end="")
            Result = "rocK"

        # Condition for Scissor Winning
        if(choice == 2 and comp_choice == 3):
            print("Scissor Wins => ",end="")
            Result = "scissoR"
        elif(choice == 3 and comp_choice == 2):
            print("Scissor Wins")
            Result == "Rock"

        if Result == "DRAW":
            print("------ It's a Tie ------")
        elif Result == choice_name:
            print("<----- User Wins ----->")
        else:
            print("----- Computer Wins -----")

        print("Do You Want to Play Again ? (Y/N)")

        ans = input().lower

        if ans == 'n':
            break

    print("Thanks for Playing")


if __name__=="__main__":
    main()