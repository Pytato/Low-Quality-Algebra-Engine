from sympy import *


class BaseQuestionEngine:
    def __init__(self):
        self.x, self.y, self.z, self.t = symbols('x y z t')
        self.k, self.m, self.n = symbols('k m n', integer=True)
        self.f, self.g, self.h = symbols('f g h', cls=Function)

    def gen_question(self, **kwargs):
        return None

    def gen_question_set(self, n_to_gen, **kwargs):
        q_set = []
        for _ in range(n_to_gen):
            curr_q = self.gen_question(**kwargs)
            while curr_q in q_set:
                curr_q = self.gen_question(**kwargs)
            q_set.append(curr_q)
        return q_set
