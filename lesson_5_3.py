# Exercise #1
#
# Create a function that asks the user to enter 3 numbers and then prints on the screen their summary and average.
#
# Hints!
#
# Create the empty list first
# Use for-loop to add 3 numbers from the user's input to the list.
# Create a separate function print_sum_avg with a list parameter.
# This function calculates and prints the summary and the average of numbers from the list parameter.
# Call the function print_sum_avg inside the first function to print out the result.

# Exercise #2
#
# Create another function for calculating summary and average and printing it to the screen,
# but it would accept *args instead of a list. Test how this function works by calling it with a list of numbers.

# Exercise #3
#
# Answer the question: What option did you like more: using list or *args? Please, justify.
#
# Exercise #4
#
# Create any program of your choice that will take the user's input and will perform any action with it
# (for example greeting program, program that calculates the factorial of the number,
# program that prints the word from the back and etc.)


# Exercise #1

number_of_numbers = 3


def input_user_list(list_size):
    user_input = [-1] * list_size  # initializing the list
    # filling the list
    for i in range(len(user_input)):
        user_input[i] = int(input("Please enter number (" + str(i+1) + " of " + str(list_size) + "): "))
    return user_input


def print_sum_avg_list(user_input):
    user_input_sum = sum(user_input)
    print("Sum of the list (list): " + str(user_input_sum))
    print("Average of the list (list): " + str(user_input_sum/len(user_input)))


# Exercise #3
def print_sum_avg_args(*args):
    user_input_sum = sum(*args)
    print("Sum of the list (args): " + str(user_input_sum))
    print("Average of the list (args): " + str(user_input_sum/len(*args)))


user_list = input_user_list(number_of_numbers)
print()
print_sum_avg_list(user_list)
print()
print_sum_avg_args(user_list)


# Exercise #4
def reverse_word(input_word):
    reversed_word = ""
    for i in range(len(input_word)):
        reversed_word = reversed_word + input_word[-i-1]
    return reversed_word


print()
print("Now let's have some fun!")
name = input("Please enter your name: ")
hourly_rate = input("Please enter your hourly rate: ")

print("So, dear " + name + " or, maybe " + reverse_word(name) + "...")
print("You are earning $" + str(int(hourly_rate) * 40 * 52) + " per year or $" + "{:.6f}".format(int(hourly_rate)/3600)
                          + " per second. Probably, not as much as you expected...")
print("But you could earn $" + str(int(hourly_rate) * 24 * 365) +
      " per year if you just abstain from food and sleep and work 24/7. Think about this!")
