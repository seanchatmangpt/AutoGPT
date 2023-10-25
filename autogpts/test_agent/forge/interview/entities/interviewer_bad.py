from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any
from ..value_objects.interview_question import InterviewQuestion
from ..value_objects.skill_metric import SkillMetric
from ..value_objects.system_attributes import SystemAttributes


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
        skill_metrics = self.get_skill_metrics(question.domain)
        system_attributes = self.get_system_attributes(question.domain)
        difficulty_level = self.calculate_difficulty_level(question.difficulty, skill_metrics, system_attributes)
        self.print_question(question.title)
        answer = self.get_answer()
        self.evaluate_answer(answer, difficulty_level)
        self.provide_feedback(answer, difficulty_level)
        self.update_skill_metrics(answer, skill_metrics)
        self.update_system_attributes(answer, system_attributes)
        self.save_skill_metrics(skill_metrics)
        self.save_system_attributes(system_attributes)
        return answer

    def get_skill_metrics(self, domain: str) -> List[SkillMetric]:
        """
        Retrieves the skill metrics for the given domain.
        """
        skill_metrics = self.database.get_skill_metrics(domain)
        self.validate_skill_metrics(skill_metrics)
        return skill_metrics

    def get_system_attributes(self, domain: str) -> SystemAttributes:
        """
        Retrieves the system attributes for the given domain.
        """
        system_attributes = self.database.get_system_attributes(domain)
        self.validate_system_attributes(system_attributes)
        return system_attributes

    def calculate_difficulty_level(self, difficulty: str, skill_metrics: List[SkillMetric], system_attributes: SystemAttributes) -> int:
        """
        Calculates the difficulty level of the question based on the given difficulty, skill metrics, and system attributes.
        """
        difficulty_level = self.calculate_difficulty_level_from_difficulty(difficulty)
        difficulty_level = self.adjust_difficulty_level_from_skill_metrics(difficulty_level, skill_metrics)
        difficulty_level = self.adjust_difficulty_level_from_system_attributes(difficulty_level, system_attributes)
        return difficulty_level

    def calculate_difficulty_level_from_difficulty(self, difficulty: str) -> int:
        """
        Calculates the difficulty level based on the given difficulty.
        """
        difficulty_level_map = {'easy': 1, 'medium': 2, 'hard': 3}
        return difficulty_level_map[difficulty]

    def adjust_difficulty_level_from_skill_metrics(self, difficulty_level: int, skill_metrics: List[SkillMetric]) -> int:
        """
        Adjusts the difficulty level based on the given skill metrics.
        """
        average_rating = self.calculate_average_rating(skill_metrics)
        if average_rating >= 4:
            difficulty_level -= 1
        elif average_rating <= 2:
            difficulty_level += 1
        return difficulty_level

    def adjust_difficulty_level_from_system_attributes(self, difficulty_level: int, system_attributes: SystemAttributes) -> int:
        """
        Adjusts the difficulty level based on the given system attributes.
        """
        if system_attributes.architecture_type == 'microservices':
            difficulty_level += 1
        elif system_attributes.architecture_type == 'monolithic':
            difficulty_level -= 1
        if len(system_attributes.dependencies) > 5:
            difficulty_level += 1
        return difficulty_level

    def calculate_average_rating(self, skill_metrics: List[SkillMetric]) -> float:
        """
        Calculates the average rating of the given skill metrics.
        """
        sum_of_ratings = 0
        for skill_metric in skill_metrics:
            sum_of_ratings += skill_metric.rating
        average_rating = sum_of_ratings / len(skill_metrics)
        return average_rating

    def print_question(self, question_title: str):
        """
        Prints the given question title.
        """
        print(question_title)

    def get_answer(self) -> str:
        """
        Gets the answer from the candidate.
        """
        answer = input()
        self.validate_answer(answer)
        return answer

    def validate_answer(self, answer: str):
        """
        Validates the given answer.
        """
        icontract.ensure(lambda: answer != '', error=ValueError('Answer cannot be empty.'))

    def evaluate_answer(self, answer: str, difficulty_level: int):
        """
        Evaluates the given answer based on the given difficulty level.
        """
        if difficulty_level == 1:
            print('Correct!')
        elif difficulty_level == 2:
            print('Almost there!')
        elif difficulty_level == 3:
            print('Incorrect!')

    def provide_feedback(self, answer: str, difficulty_level: int):
        """
        Provides feedback to the candidate based on the given answer and difficulty level.
        """
        if difficulty_level == 1:
            print('Great job!')
        elif difficulty_level == 2:
            print("You're getting there!")
        elif difficulty_level == 3:
            print('Better luck next time!')

    def update_skill_metrics(self, answer: str, skill_metrics: List[SkillMetric]):
        """
        Updates the given skill metrics based on the given answer.
        """
        for skill_metric in skill_metrics:
            if skill_metric.skill_name == answer:
                skill_metric.rating += 1

    def update_system_attributes(self, answer: str, system_attributes: SystemAttributes):
        """
        Updates the given system attributes based on the given answer.
        """
        if answer == 'Yes':
            system_attributes.dependencies.append('New dependency')

    def save_skill_metrics(self, skill_metrics: List[SkillMetric]):
        """
        Saves the given skill metrics to the database.
        """
        self.database.save_skill_metrics(skill_metrics)

    def save_system_attributes(self, system_attributes: SystemAttributes):
        """
        Saves the given system attributes to the database.
        """
        self.database.save_system_attributes(system_attributes)

    def validate_skill_metrics(self, skill_metrics: List[SkillMetric]):
        """
        Validates the given skill metrics.
        """
        icontract.ensure(lambda: len(skill_metrics) > 0, error=ValueError('Skill metrics cannot be empty.'))

    def validate_system_attributes(self, system_attributes: SystemAttributes):
        """
        Validates the given system attributes.
        """
        icontract.ensure(lambda: system_attributes.architecture_type in ['microservices', 'monolithic'], error=ValueError('Invalid architecture type.'))
        icontract.ensure(lambda: len(system_attributes.dependencies) >= 0, error=ValueError('Dependencies cannot be empty.'))