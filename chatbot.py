def greet(bot_name, birth_year):
    message1 = "Hello! My name is {}.".format(bot_name)
    message2 = "I was created in {}.".format(birth_year)
    print(message1)
    print(message2)


def remind_name():
    print("Please, remind me your name.")
    name = input("> ")
    
    # Changed logic: store message first, then print
    response = "What a great name you have, {}!".format(name)
    print(response)


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input("Remainder by 3: "))
    rem5 = int(input("Remainder by 5: "))
    rem7 = int(input("Remainder by 7: "))

    # Changed logic: step-by-step calculation
    part1 = rem3 * 70
    part2 = rem5 * 21
    part3 = rem7 * 15

    total = part1 + part2 + part3
    age = total % 105

    print("Your age is {}; that's a good time to start programming!".format(age))


def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input("Enter a number: "))

    # Changed logic: using for loop instead of while
    for i in range(num + 1):
        print("{} !".format(i))


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use functions in Python?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into small subprograms.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    correct = False

    # Changed logic: using flag instead of break directly
    while not correct:
        answer = int(input("Enter your choice (1-4): "))
        if answer == 2:
            correct = True
            print("Completed, have a nice day!")
        else:
            print("Please, try again.")


def end():
    print("Congratulations, have a nice day!")
    print("---------------------------------")
    print("Chatbot Session Ended.")


if __name__ == "__main__":
    greet("ChattyBot", "2025")
    remind_name()
    guess_age()
    count()
    test()
    end()
