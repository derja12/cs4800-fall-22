# from unit_tests import *
import trace
import sys
import shutil
import os


def setup():
    tempdir = os.path.join(os.getcwd(), "/temp_default")
    try:
        shutil.rmtree(tempdir)
    except Exception:
        pass
    os.mkdir(tempdir)

    fails_file = open(os.path.join(tempdir, "failures.txt"),'w')
    fails_file.close()
    

# tracer = trace.Trace(
#     ignoredirs=[sys.prefix, sys.exec_prefix],
#     trace=0,
#     count=1
# )
# tracer.run("main('TestMergeSort.test_1_expected_use')")
# r = tracer.results()
# r.write_results(show_missing=True, coverdir="./coverage")


def main():
    setup()

if __name__ == "__main__":
    main()