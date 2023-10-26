import timeit
import cProfile
import io
import pstats
from memory_profiler import memory_usage
from typing import Dict, List, Tuple, Any, Optional
from pathlib import Path
from dataclasses import dataclass
from functools import wraps
from contextlib import contextmanager
from itertools import chain
from collections import Counter
from collections.abc import Callable
from functools import partial, reduce
from operator import attrgetter

def logged(func: Callable) -> Callable:
    @wraps(func)
    def with_logging(*args, **kwargs):
        start = timeit.default_timer()
        print(f'Running {func.__name__} with args: {args} kwargs: {kwargs}')
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f'Finished {func.__name__} in {end - start} seconds')
        return result
    return with_logging

@dataclass
class TestResult:
    name: str
    result: str
    error: Optional[str] = None

def run_tests(tests: List[TestResult]) -> None:
    for test in tests:
        if test.error:
            print(f'{test.name}: {test.error}')
        else:
            print(f'{test.name}: {test.result}')

def generate_report(tests: List[TestResult]) -> Dict[str, int]:
    return {
        'total_tests': len(tests),
        'passed_tests': sum(1 for test in tests if not test.error),
        'failed_tests': sum(1 for test in tests if test.error)
    }

@contextmanager
def profiling() -> Tuple[io.StringIO, pstats.Stats]:
    profiler = cProfile.Profile()
    profiler.enable()
    output = io.StringIO()
    yield output, profiler
    profiler.disable()
    stats = pstats.Stats(profiler, stream=output)
    stats.sort_stats('cumulative')
    stats.print_stats()
    print(output.getvalue())

def measure_memory_usage(func: Callable) -> Callable:
    @wraps(func)
    def with_memory_usage(*args, **kwargs):
        mem_usage, result = memory_usage((func, args, kwargs), interval=0.2, retval=True)
        print(f'Memory usage: {max(mem_usage) - min(mem_usage)}')
        return result
    return with_memory_usage

@dataclass
class ExecutionReport:
    name: str
    execution_time: float
    memory_usage: int

def generate_execution_report(func: Callable, *args, **kwargs) -> ExecutionReport:
    with profiling() as (output, profiler):
        with measure_memory_usage(func) as result:
            func(*args, **kwargs)
        execution_time = profiler.total_tt
        memory_usage = max(profiler.getstats(), key=attrgetter('tottime')).memusage[2]
        return ExecutionReport(func.__name__, execution_time, memory_usage)

def get_coverage(func: Callable) -> Callable:
    @wraps(func)
    def with_coverage(*args, **kwargs):
        result = func(*args, **kwargs)
        lines = result.split('\n')
        return Counter(lines)
    return with_coverage

def get_code_complexity(func: Callable) -> int:
    return len(inspect.getsourcelines(func)[0])

def export_report(report: Dict[str, Any], export_format: str) -> None:
    path = Path(f'report.{export_format}')
    with open(path, 'w') as file:
        file.write(str(report))

def main() -> None:
    # Tests
    tests = [
        TestResult('Test 1', 'Passed'),
        TestResult('Test 2', 'Passed'),
        TestResult('Test 3', 'Failed', 'Error message'),
        TestResult('Test 4', 'Passed')
    ]
    run_tests(tests)
    # Debugging
    @logged
    def add(x: int, y: int) -> int:
        return x + y
    add(1, 2)
    # Code suggestions
    # N/A
    # Metrics
    metrics = {
        'code_complexity': get_code_complexity(add),
        'test_coverage': get_coverage(add),
        'lines_of_code': len(inspect.getsourcelines(add)[0])
    }
    # Reports
    execution_report = generate_execution_report(add, 1, 2)
    code_complexity_report = metrics['code_complexity']
    test_coverage_report = metrics['test_coverage']
    lines_of_code_report = metrics['lines_of_code']
    # Export
    export_report(execution_report, 'json')
    export_report(code_complexity_report, 'csv')
    export_report(test_coverage_report, 'txt')
    export_report(lines_of_code_report, 'md')

if __name__ == '__main__':
    main()