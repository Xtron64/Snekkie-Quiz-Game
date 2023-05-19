yes = "yes"


def question1Creation():
    global question1, correct_answer1, potential_answers1, question1Class
    while True:
        print("What is the question you are asking going to be?")
        question1 = input("You: ")
        print("Are you sure?")
        question_confirmation1 = input("You: ")
        if question_confirmation1.lower() != yes.lower():
            continue
        else:
            break
    while True:
        print("What would you like potential answers to be (correct answer included)?")
        potential_answer_a1 = input("Potential answer A: ")
        potential_answer_b1 = input("Potential answer B: ")
        potential_answer_c1 = input("Potential answer C: ")
        print("Which one would you like to be the correct answer?")
        correct_answer1 = input("You: ")
        while correct_answer1.lower != "A".lower() or "B".lower() or "C".lower():
            print("Please reply with the letter, as in A, B or C")
            print("Which one would you like to be the correct answer?")
            correct_answer1 = input("You: ")
            if correct_answer1.lower() != "A".lower() or "B".lower() or "C".lower():
                continue
            else:
                break
        print("Are you sure?")
        potential_answer1_confirmation = input("You: ")
        if potential_answer1_confirmation.lower() != yes.lower():
            continue
        else:
            break
    potential_answers1 = (potential_answer_a1, potential_answer_b1, potential_answer_c1)

    class question1Class:
        var = (
            question1,
            potential_answers1,
            correct_answer1
        )


def question2Creation():
    global question2, potential_answers2, correct_answer2, question2Class
    while True:
        print("What would you like the question to be?")
        question2 = input("You: ")
        print("Are you sure?")
        question2_confirmation = input("You: ")
        if question2_confirmation.lower() != yes.lower():
            continue
        else:
            break
    while True:
        print("What would you like potential answers to be (correct answer included)?")
        potential_answer_a2 = input("Potential answer A: ")
        potential_answer_b2 = input("Potential answer B: ")
        potential_answer_c2 = input("Potential answer C: ")
        print("Which one would you like to be the correct answer?")
        correct_answer2 = input("You: ")
        while correct_answer2.lower != "a" or "b" or "c":
            print("Please reply with the letter, as in A, B or C")
            print("Which one would you like to be the correct answer?")
            correct_answer2 = input("You: ")
            if correct_answer2.lower() != "a" or "b" or "c":
                continue
            else:
                break
        print("Are you sure?")
        potential_answer2_confirmation = input("You: ")
        if potential_answer2_confirmation.lower() != yes.lower():
            continue
        else:
            break
    potential_answers2 = (potential_answer_a2, potential_answer_b2, potential_answer_c2)

    class question2Class:
        var = (
            question2,
            potential_answers2,
            correct_answer2
        )


def question3Creation():
    global question3, potential_answers3, correct_answer3, question3Class
    while True:
        print("What would you like the question to be?")
        question3 = input("You: ")
        print("Are you sure?")
        question3_confirmation = input("You: ")
        if question3_confirmation.lower() != yes.lower():
            continue
        else:
            break
    while True:
        print("What would you like potential answers to be (correct answer included)?")
        potential_answer_a3 = input("Potential answer A: ")
        potential_answer_b3 = input("Potential answer B: ")
        potential_answer_c3 = input("Potential answer C: ")
        print("Which one would you like to be the correct answer?")
        correct_answer3 = input("You: ")
        while correct_answer3.lower != "a" or "b" or "c":
            print("Please reply with the letter, as in A, B or C")
            print("Which one would you like to be the correct answer?")
            correct_answer3 = input("You: ")
            if correct_answer3.lower() != "a" or "b" or "c":
                continue
            else:
                break
        print("Are you sure?")
        potential_answer3_confirmation = input("You: ")
        if potential_answer3_confirmation.lower() != yes.lower():
            continue
        else:
            break
    potential_answers3 = (potential_answer_a3, potential_answer_b3, potential_answer_c3)

    class question3Class:
        var = (
            question3,
            potential_answers3,
            correct_answer3
        )


def main():
    print("Would you like to import flashcards to quickly convert them quizzes?")
    import_flashcards = input("You: ")
    if import_flashcards.lower() == yes.lower():
        pass
    else:
        # Creating the quiz
        question1Creation()
        print("Question 1 created!")
        question2Creation()
        print("Question 2 created!")
        question3Creation()
        print("Question 3 created!")
        # Playing the quiz
        print(question1)
        print(potential_answers1)
        user_answer1 = input("You: ")
        print("Are you sure?")


if __name__ == '__main__':
    main()
