import unittest

from testAll import TestHome
from testAll import TestBlog
from multiprocessing import Pool


def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)
    # verbosity ne demek, ne işe yarar.


tests = [TestHome("test_TC001_py3_python_news_button"),
         TestBlog("test_TC002_verify_url"),
         TestBlog("test_TC003_verify_PY380RC1_name")]

if __name__ == "__main__":
    with Pool(3) as p:
        p.map(run_test, tests)
    # pool ne işe yarıyor?
