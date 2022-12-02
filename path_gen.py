from unit_tests import *
import trace
import sys
import shutil
import os


def main():
    setup()
    run_tests()

def setup():
    tempdir = os.path.join(os.getcwd(), "temp_default")
    try:
        shutil.rmtree(tempdir)
    except Exception:
        pass
    os.mkdir(tempdir)

    fails_file = open(os.path.join(tempdir, "failures.txt"),'w')
    fails_file.close()
    
def run_tests():
    tracer = trace.Trace(
        ignoredirs=[sys.prefix, sys.exec_prefix],
        trace=0,
        count=1
    )
    tracer.run("main_testing('TestMergeSort.test_1_expected_use', 'temp_default/failures.txt')")
    r = tracer.results()
    r.write_results(show_missing=True, coverdir="./temp_default/test_TestMergeSort.test_1_expected_use")

if __name__ == "__main__":
    main()