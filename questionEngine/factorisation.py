from questionEngine.base_question_engine import BaseQuestionEngine
import sympy
import random


class FactorisationQuestions(BaseQuestionEngine):
    def __init__(self):
        super().__init__()

    def gen_quad_factorisation_x_only(self, coeff_range=None, follower_range=None, **kwargs):
        if coeff_range is None:
            coeff_range = [-6, 6]
        if follower_range is None:
            follower_range = [-12, 12]
        pre_gen_eq = random.randint(*coeff_range) * \
            (random.randint(*coeff_range) * self.x + random.randint(*follower_range)) * \
            (random.randint(*coeff_range) * self.x + random.randint(*follower_range))

        return pre_gen_eq.expand(), pre_gen_eq

    def gen_question(self, diff=0, **kwargs):
        if diff == 0:
            return self.gen_quad_factorisation_x_only(**kwargs)


if __name__ == "__main__":
    test_fac_engine = FactorisationQuestions()
    print(test_fac_engine.gen_question_set(20, diff=0))
