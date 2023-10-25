from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any
from .candidate import Candidate


class Interview:
    """
    An Entity representing a single interview instance. It has a unique identity and associated properties like interview type, date, and candidates.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    def evaluate_candidate(self, candidate: Candidate, metrics: List[
            SkillMetric]):
        """
        Evaluates the candidate based on given metrics.
        :param candidate: Candidate object to be evaluated
        :param metrics: List of SkillMetric objects to be used for evaluation
        :return: Percentage score of the candidate's evaluation
        """
        candidate_skills = candidate.skills
        candidate_system_attributes = candidate.system_attributes
        candidate_interview_questions = candidate.interview_questions
        candidate_metrics = candidate.metrics
        candidate_architecture_type = (candidate_system_attributes.
                                       architecture_type)
        candidate_dependencies = candidate_system_attributes.dependencies
        candidate_skill_names = [skill.skill_name for skill in
                                 candidate_metrics]
        candidate_skill_ratings = [skill.rating for skill in candidate_metrics]
        candidate_interview_question_titles = [question.title for question in
                                               candidate_interview_questions]
        candidate_interview_question_difficulties = [question.difficulty for
                                                     question in candidate_interview_questions]
        candidate_interview_question_domains = [question.domain for
                                                question in candidate_interview_questions]
        candidate_total_skill_rating = sum(candidate_skill_ratings)
        candidate_total_interview_question_difficulty = sum(
            candidate_interview_question_difficulties)
        candidate_total_interview_question_domain = sum(
            candidate_interview_question_domains)
        candidate_total_interview_question_score = (
            candidate_total_interview_question_difficulty +
            candidate_total_interview_question_domain)
        candidate_total_score = (candidate_total_skill_rating +
                                 candidate_total_interview_question_score)
        candidate_total_score_percentage = candidate_total_score / 100 * 100
        candidate_total_score_percentage = round(
            candidate_total_score_percentage, 2)
        candidate_total_score_percentage = str(candidate_total_score_percentage
                                               ) + '%'
        return candidate_total_score_percentage