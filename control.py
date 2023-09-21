from questions import *
from random import shuffle

class Control:

    def __init__(self):
        # questions
        self.questions = question_data
        self.current_q_index = 0
        shuffle(self.questions)
    
    def instructions(self):
        print("\nInstructions: ")
        print("For each Statement Answer as True or False. Any other answer would skip the question.")
        print("If your answer is correct you can choose to double down for the next question by entering 'Yes'")
        print("If wrong answer during double down, you lose points for the previous round too.")
        print("Good Luck\n")

    def next_question(self):

        self.current_q = self.questions[self.current_q_index] # a dict
        self.current_q_index += 1

        return self.current_q['text']

    def check_answer(self,input_answer):
        answer = self.current_q["answer"].lower()
        reward = False

        if input_answer == answer:
            reward = True

        return reward

    def do_question_remain(self):
        
        return self.current_q_index < len(self.questions)

    def reset(self):
        shuffle(self.questions)
        self.current_q_index = 0
        self.instructions()
