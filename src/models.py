from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Question:
    id: str
    title: str
    options: list[str]  # 不带 ABCD 前缀的选项内容
    answer: int         # 正确答案索引 0-3
    set_id: str = ""    # 所属练习集 ID


@dataclass
class QuestionSet:
    id: str
    name: str
    questions: list[Question] = field(default_factory=list)


@dataclass
class ErrorEntry:
    question_id: str
    wrong_count: int = 0
    last_wrong: str = ""


@dataclass
class QuizResult:
    """单题答题结果"""
    question: Question
    user_choice: int        # 用户选择的选项索引（随机化后的）
    is_correct: bool
    shuffled_options: list[str]  # 本次显示的选项顺序
    shuffled_answer: int         # 本次正确答案在 shuffled_options 中的位置
