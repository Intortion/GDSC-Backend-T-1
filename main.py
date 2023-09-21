from control import Control


class Quiz:

    def __init__(self):

        self.score = 0
        self.mode = "normal"

        # displaying instructions for the first time
        controls.instructions()
    
    def normal_points(self,answer):

        correct = controls.check_answer(answer.lower())
        # normal question
        if correct:
            print("Correct!")
            double = "no"
            self.score += 2
            # if questions remain, asks for double down
            if controls.do_question_remain():
                double = input("Would you like to double down on next question? Enter Yes: ")
            if double.lower() == "yes":
                self.mode = "double"
        else:
            self.score -= 1
            print("Incorrect")

    
    def double_points(self,answer):

        correct = controls.check_answer(answer.lower())
        # for double down case
        if correct:
            self.score += 4
            print("Correct!")
        else:
            self.score -= 3     # cancels prev ques points
            print("Incorrect")
        self.mode = "normal"

    def show_score(self):
        print("Your current score is :", self.score)
        print()
    
    def reset(self):
        self.score = 0
        self.mode = "normal"
        controls.reset()

    def run(self):

        print("S:",controls.next_question())

        # check answer
        answer = input("A: ").lower()
        
        if answer == "true" or answer == 'false':
            if self.mode == "normal":
                self.normal_points(answer)
            elif self.mode == "double":
                self.double_points(answer)
        else:
            self.mode = "normal"
        
        # print score
        self.show_score()

# class objects
controls = Control()
quiz = Quiz()

running = True


# main loop
while running:

    # check if question remain
    if controls.do_question_remain():
        quiz.run()
    else:
        print("Your total score is :",quiz.score)
        i = input("Press Enter to retake quiz or any other answer to quit: ")

        if not i:
            quiz.reset()
        else:
            running = False
            quit()
    
    