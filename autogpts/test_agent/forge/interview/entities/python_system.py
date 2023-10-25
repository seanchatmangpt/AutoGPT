from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any

from ..value_objects.interview_question import InterviewQuestion
from ..value_objects.skill_metric import SkillMetric
from ..value_objects.system_attributes import SystemAttributes


class PythonSystem:
    """
    An Entity representing a Python-based system. It has a unique identity and can be evaluated, scaled, or modified.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    def evaluate_system(self, attributes: SystemAttributes) -> List[InterviewQuestion]:
        """
        Evaluates the Python system based on given attributes.
        :param attributes: SystemAttributes object containing architecture type and dependencies
        :return: List of InterviewQuestion objects
        """
        architecture_type = attributes.architecture_type
        dependencies = attributes.dependencies
        skill_metrics = []
        for dependency in dependencies:
            skill_name = dependency.split('.')[0]
            rating = int(dependency.split('.')[1])
            skill_metric = SkillMetric(skill_name=skill_name, rating=rating)
            skill_metrics.append(skill_metric)
        interview_questions = []
        for skill_metric in skill_metrics:
            skill_name = skill_metric.skill_name
            difficulty = skill_metric.rating
            domain = architecture_type
            interview_question = InterviewQuestion(title=skill_name,
                                                   difficulty=difficulty, domain=domain)
            interview_questions.append(interview_question)
        return interview_questions