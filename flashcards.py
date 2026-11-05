# We need to use the random function to display a random question within a directory.

# Another function will prompt the user if they want to see the answer. 
#The answer will be the second key value 

flashcards = [
    {"question" : "What color is the Sun?", "answer" : "Yellow"},
    {"question" : "What color is the Sky?", "answer" : "Blue"},
    {"question" : "What color is the grass", "answer" : "Green"},

]
'''
Task:Tell user goodbye
Input: none
Side Effect: Print goodby message
Return: none
'''
def quit_app():
    print("Thanks for Studying!")

'''
Task: Selects random question in flash card list
Input: Flashcards list
Side Effect: None
Return: Flash card from list
'''

def get_random_question(cards):
    random_card = random.choice(cards)
    print (random_card)
'''
Task: Display Question
Input: Question Card
Side Effect: Print the question next to terminal
Return: none
'''

def show_question():
    question = card["question"]
    print("Question:", question)


'''
Task: Display Question
Input: Question Card
Side Effect: Print the question nest to terminal
Return: none
'''

def show_answer(card):
    answer = card["answer"]
    print("Answer:", answer)


'''
Task: Reveal Answer
Input:
Side Effect: Print Answer
Return:
'''


def main():
    while True:
        chose_card = get_random_question(flashcards)
        show_question(chosen_card)
        user_choice = input("Enter Q to quit, type anything else to continue.")
        if user_choice == "Q":
            quit_app()
            break
        else: 
            show_answer(chose_card)

main()
