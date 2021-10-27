import itertools
import time
from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    name: str
    dependencies: List[str]

    def print_name(self):
        print(self.name)


test_list = [
    Task('A', ['B', 'C']),
    Task('B', ['C']),
    Task('C', [])
]

done_tasks = set()

def _run_task(task: Task, all_tasks:List[Task]):
    if task.name in done_tasks:
        return
    for dependency in task.dependencies:
        if dependency not in done_tasks:
            dependency_task = [task for task in all_tasks if task.name == dependency].pop()
            _run_task(dependency_task, all_tasks)
    task.print_name()
    done_tasks.add(task.name)


def run(tasks: List[Task]):
    """
    run([
    Task('A', ['B', 'C']),
    Task('B', ['C']),
    Task('C', [])
    ])
    C
    B
    A
    :param test_list:
    :return:
    """
    for task in tasks:
        _run_task(task, tasks)

run(test_list)

