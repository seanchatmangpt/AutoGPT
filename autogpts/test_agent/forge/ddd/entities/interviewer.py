from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any
from ..value_objects.interview_question import InterviewQuestion


class Interviewer:
    """
    An Entity representing the interviewer who conducts the interview. Has a unique identity and can evaluate candidates.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    def ask_question(self, question: InterviewQuestion):
        """
    Asks the specified question during an interview.
    """
        if question is None:
            raise ValueError('Question cannot be None')
        if question.title is None or question.title == '':
            raise ValueError('Question title cannot be None or empty')
        if question.difficulty is None or question.difficulty == '':
            raise ValueError('Question difficulty cannot be None or empty')
        if question.domain is None or question.domain == '':
            raise ValueError('Question domain cannot be None or empty')
        if question.domain not in ['Python', 'Java', 'C++', 'C#',
                                   'JavaScript', 'PHP', 'Ruby', 'Go', 'Swift', 'Kotlin']:
            raise ValueError(
                'Question domain must be one of the following: Python, Java, C++, C#, JavaScript, PHP, Ruby, Go, Swift, Kotlin'
            )
        if question.difficulty not in ['Easy', 'Medium', 'Hard']:
            raise ValueError(
                'Question difficulty must be one of the following: Easy, Medium, Hard'
            )
        if question.title not in [
            'What is the difference between a list and a tuple?',
            'What is the difference between a set and a frozenset?',
            'What is the difference between a dictionary and a defaultdict?',
            'What is the difference between a list and a deque?',
            'What is the difference between a list and a linked list?',
            'What is the difference between a list and a array?',
            'What is the difference between a list and a stack?',
            'What is the difference between a list and a queue?',
            'What is the difference between a list and a heap?',
                'What is the difference between a list and a graph?']:
            raise ValueError(
                'Question title must be one of the following: What is the difference between a list and a tuple?, What is the difference between a set and a frozenset?, What is the difference between a dictionary and a defaultdict?, What is the difference between a list and a deque?, What is the difference between a list and a linked list?, What is the difference between a list and a array?, What is the difference between a list and a stack?, What is the difference between a list and a queue?, What is the difference between a list and a heap?, What is the difference between a list and a graph?'
            )
        print('Asking question: ' + question.title)
        print('Difficulty: ' + question.difficulty)
        print('Domain: ' + question.domain)
        return
