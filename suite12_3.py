import unittest
from test12_3 import RunnerTest
from test12_3 import TournamentTest



RT_Test = unittest.TestSuite()
RT_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
RT_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RT_Test)

