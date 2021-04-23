import unittest
import logging

import test_line, test_point, test_compliment, test_random, test_rect

logging.getLogger().setLevel(logging.INFO)

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_rect))
suite.addTests(loader.loadTestsFromModule(test_random))
suite.addTests(loader.loadTestsFromModule(test_point))
suite.addTests(loader.loadTestsFromModule(test_line))
suite.addTests(loader.loadTestsFromModule(test_compliment))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
