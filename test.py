import questionEngine

import json
from datetime import datetime

if __name__ == "__main__":
    possible_question_generators = {
        "factorisation": questionEngine.FactorisationQuestions
    }

    def get_choice():
        return input(f"Select which questions to generate of the following:\n\n"
                     f"{possible_question_generators.keys()}.\n\nChoice: ")

    def menu_loop(tries=0):
        if tries > 1:
            exit(0)
        tries += 1
        try:
            return possible_question_generators[get_choice()]
        except KeyError:
            return menu_loop(tries=tries)

    question_engine = menu_loop()()

    answers_questions = question_engine.gen_question_set(int(input("How many questions to "
                                                                   "generate: ")))

    answers = [answers_questions[i][0] for i in range(len(answers_questions))]
    questions = [answers_questions[i][1] for i in range(len(answers_questions))]

    dt_now_formatted = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    with open(f"./out/{dt_now_formatted}.json", "w") as json_obj:
        json.dump(answers_questions, json_obj, indent=4)
        print(f"Your questions have been output to: ./out/{dt_now_formatted}.json")
