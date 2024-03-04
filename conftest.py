import pytest
from collections import defaultdict

pytest_plugins = ["pytester"]

# for counting passed + failed tests, per student/basename
ac_data = defaultdict(lambda: [0,0])

def pytest_html_report_title(report):
    report.title = "pytest grader"

def pytest_html_results_table_header(cells):
    # add new column for student/basename
    cells.insert(2, "<th>Student/Basename</th>")
    # remove links column
    cells.pop()

def pytest_html_results_table_row(report, cells):
    basename = ""
    if report.when == "call":
        # add new column for base of filename
        basename = report.ac_basename
        # count the number of passed tests
        stats = ac_data[basename]
        if report.passed: stats[0] += 1 # passed tests
        if report.failed: stats[1] += 1 # failed tests
        basename = "(%d/%d) %s" % (stats[0],stats[0]+stats[1],basename)

    cells.insert(2, f"<td>{basename}</td>")
    # remove links column
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.ac_basename = item.cls.basename
