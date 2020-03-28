import questionEngine

from pylatex import Document, Section, Subsection, Package, Command
from pylatex.utils import italic, NoEscape

from sympy import *
import os


class QuestionDoc(Document):
    def __init__(self):
        super().__init__(documentclass="exam")
        # self.packages.append(Package("amsmath"))
        self.packages.append(Package("amsfonts"))
        self.packages.append(Package("calc"))
        self.preamble.append(Command('title', 'Factorisation Questions'))
        self.preamble.append(Command('author', 'FWF'))
        self.preamble.append(Command('date', NoEscape(r'\today')))
        self.append(NoEscape(r'\maketitle'))

        self.append(NoEscape(r"\begin{questions}"))

    def fill_document(self, questions):
        """Add a section, a subsection and some text to the document."""
        self.append(NoEscape("\\question \n"
                             "Factorise the following equations:"))
        self.append(NoEscape("\\begin{parts}"))
        self.append(NoEscape("\\part Factorise"))
        self.append(NoEscape("\\begin{subparts}"))
        for i in range(1, len(questions) + 1):
            self.append(NoEscape(f"\\subpart \n ${latex(questions[i-1][0])}$"))
            if i % 10 == 0 and i != range(1, len(questions) + 1)[-1]:
                self.append(NoEscape("\\end{subparts}"))
                self.append(NoEscape("\\part Factorise"))
                self.append(NoEscape("\\begin{subparts}"))

        self.append(NoEscape("\\end{subparts}"))
        self.append(NoEscape("\\end{parts}"))
        self.append(NoEscape(r"\end{questions}"))


if __name__ == "__main__":
    factorisation_engine = questionEngine.FactorisationQuestions()
    factorisation_questions = factorisation_engine.gen_question_set(
        int(input("N to gen: ")),
        diff=int(input("Diff: ")))

    file_name = str(input("Output file name: "))

    question_document = QuestionDoc()

    question_document.fill_document(factorisation_questions)
    with open(f"./out/{file_name}_answers.txt", "w") as answer_file:
        for answer in factorisation_questions:
            answer_file.write(f"{pretty(answer[1], use_unicode=False)}\n\n")

    question_document.generate_tex(f"./out/{file_name}")
