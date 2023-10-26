from collections import namedtuple
from typing import List
import subprocess
import time
import psutil

Report = namedtuple('Report', ['name', 'code_complexity', 'code_coverage',
                               'performance'])

def generate_reports() -> List[Report]:
    """Generate reports for code complexity, code coverage, and performance."""
    reports = []

    # Generate code complexity report
    code_complexity = subprocess.check_output(['radon', 'cc', '-s', '-a', 'code'])
    reports.append(Report('Code Complexity Report', code_complexity, None, None))

    # Generate code coverage report
    code_coverage = subprocess.check_output(['coverage', 'report'])
    reports.append(Report('Code Coverage Report', None, code_coverage, None))

    # Generate performance report
    performance = timeit.timeit('main()', setup='from __main__ import main', number=100)
    reports.append(Report('Performance Report', None, None, performance))

    return reports

def debug_tools() -> None:
    """Run debugging tools and generate relevant metrics and reports."""
    subprocess.run('pyflame -s 30 -r -o perf.txt python main.py', shell=True)
    subprocess.run('py-spy record -o calls.svg python main.py', shell=True)
    subprocess.run('python -m memory_profiler main.py', shell=True)

def code_review() -> None:
    """Perform code review and provide feedback on code quality."""
    subprocess.run('black main.py', shell=True)
    subprocess.run('flake8 main.py', shell=True)
    subprocess.run('mypy main.py', shell=True)

def integrate_version_control() -> None:
    """Integrate with version control systems such as Git."""
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "Added new feature"', shell=True)
    subprocess.run('git push origin master', shell=True)

def create_account(username: str, password: str) -> None:
    """Create user account with given username and password."""
    subprocess.run(f'python create_account.py {username} {password}', shell=True)

def login(username: str, password: str) -> None:
    """Log in with given username and password."""
    subprocess.run(f'python login.py {username} {password}', shell=True)

# Main function
def main() -> None:
    """Main function that runs all the features and scenarios."""
    reports = generate_reports()
    for report in reports:
        print(f'Report Name: {report.name}\nReport Contents: {report}\n')

    debug_tools()
    code_review()
    integrate_version_control()
    create_account('John Doe', 'password123')
    login('John Doe', 'password123')

    # Print system performance metrics
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    print(f'CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%')

# Run main function
if __name__ == '__main__':
    main()