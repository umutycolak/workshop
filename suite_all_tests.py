import unittest
from testAll import TestHome
from testAll import TestBlog
from concurrencytest import ConcurrentTestSuite, fork_for_tests


def suite():

    suite = unittest.TestSuite()
    # Home Page Test
    suite.addTest(TestHome("test_TC001_py3_python_news_button"))

    # Blog Page Tests
    suite.addTest(TestBlog("test_TC002_verify_url"))
    suite.addTest(TestBlog("test_TC003_verify_PY380RC1_name"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(3))
    runner.run(concurrent_suite)
