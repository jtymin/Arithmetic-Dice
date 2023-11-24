import random
print ("Dice Rolling Game")
die_color = ["white", "gray", "black"]
rand_number = random.randint(20,30)

print ("**Try to get a number close to -----" + str(rand_number) + "----- by multiplying or adding 3 numbers you roll from the die! If the number you obtain is greater or less than the target number by 3 or less, you win!** \n \n *Rules* \n - On you first roll, you will roll one standard die, and choose to add or multiply the number you got with very small and very large values. You will be able to choose which final value you want after. \n - If you roll a black die on your third number, you have to add your third number by 1. If you roll a white die, you have to subtract your third number by 1.")
    
def game(game_number):
    global first_number
    global final_number
    unique_die = [2, 7, 12, 17]
    if game_number == "1st Roll":
        print("1st Roll")
        first_dice_roll = random.randint(1, 6)
        for i in range(len(unique_die)):
            user_input = input("You rolled a -" + str(first_dice_roll) + "- and a -" + str (unique_die[i]) + "-! 'Add' or 'Multiply'? ")
            if user_input == "Add" or user_input == "add":
                first_number = first_dice_roll + unique_die[i]
            elif user_input == "Multiply" or user_input == "multiply":
                first_number = first_dice_roll * unique_die[i]
            print ("Your number is currently a -" + str(first_number) + "-.")
        user_input = input("Which final value would you like to choose? ")
        print("You chose: " + str(user_input))
    else:
        global dice_roll
        global die_color
        dice_roll = random.randint(1,6)
        die_color = random.choice(die_color)
        global final_number
        print("2nd Roll")
        print("The third number that you rolled is a -" + str(        dice_roll) + "-.")
        if die_color == "black":
            print("You rolled a black die, so you have to add 1 to the. number you got from the die!")
            dice_roll = dice_roll + 1
            print("Your number is now a -" + str(dice_roll) + "-.")
        elif die_color == "white":
            print("You rolled a white die, so you have to subtract 1 from the number you got from the die!")
            dice_roll = dice_roll - 1
        add_user_input = input("Choose to 'Add' or 'Multiply' this number with the previous one: ") 
        if add_user_input == "Add" or add_user_input == "add":
                final_number = first_number + dice_roll
        elif add_user_input == "Multiply" or add_user_input == "multiply":
            final_number = first_number * dice_roll
        print ("Your final number is a -" + str(final_number) + "-!")
        if int(rand_number) - int(final_number) <= 3 and int(rand_number) - int(final_number) >= -3: 
            print ("Congratulations! You won!")
        else:
            print ("Oh no! You lost!")

    
        
game_number_one = input("Type '1st Roll' to start!: ")
game(game_number_one)
game_number_second = input("Type '2nd Roll' to continue the game!: ")
game(game_number_second)

    


