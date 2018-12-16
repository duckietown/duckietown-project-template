#!/usr/bin/env python

from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution

class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)
        '''
	add the solution code here.
	'''
	import myalgorithm	
	myclass = myalgorithm.MyClass()
	input_from_evaluator = cis.get_challenge_parameters()
	data = {'data': myclass.run_my_code()+input_from_evaluator['dummy']}
	cis.set_solution_output_dict(data)


if __name__ == '__main__':
    wrap_solution(Solver())
