import json
from pathlib import Path
from datetime import datetime

from src.config import QUESTIONS_FILE, ERRORBOOK_FILE, DATA_DIR
from src.models import Question, QuestionSet


def _ensure_files():
    """初始化：确保数据文件和目录存在"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not QUESTIONS_FILE.exists():
        _save_json(QUESTIONS_FILE, {"sets": []})
    if not ERRORBOOK_FILE.exists():
        _save_json(ERRORBOOK_FILE, {})


def _load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_json(path: Path, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ==================== 题库操作 ====================


def load_all_sets() -> list[QuestionSet]:
    """加载全部练习集"""
    _ensure_files()
    data = _load_json(QUESTIONS_FILE)
    sets = []
    for s in data.get("sets", []):
        qs = QuestionSet(id=s["id"], name=s["name"])
        for q in s.get("questions", []):
            qs.questions.append(Question(
                id=q["id"],
                title=q["title"],
                options=q["options"],
                answer=q["answer"],
                set_id=s["id"],
            ))
        sets.append(qs)
    return sets


def get_set_by_id(set_id: str) -> QuestionSet | None:
    sets = load_all_sets()
    for s in sets:
        if s.id == set_id:
            return s
    return None


def get_question_by_id(question_id: str) -> Question | None:
    sets = load_all_sets()
    for s in sets:
        for q in s.questions:
            if q.id == question_id:
                return q
    return None


def save_all_sets(sets: list[QuestionSet]):
    """保存全部练习集"""
    data = {"sets": []}
    for s in sets:
        entry = {
            "id": s.id,
            "name": s.name,
            "questions": [
                {
                    "id": q.id,
                    "title": q.title,
                    "options": q.options,
                    "answer": q.answer,
                }
                for q in s.questions
            ],
        }
        data["sets"].append(entry)
    _save_json(QUESTIONS_FILE, data)


def add_question_set(set_id: str, name: str):
    """新增练习集"""
    sets = load_all_sets()
    if any(s.id == set_id for s in sets):
        raise ValueError(f"练习集 {set_id} 已存在")
    sets.append(QuestionSet(id=set_id, name=name))
    save_all_sets(sets)


def add_question_to_set(set_id: str, title: str, options: list[str], answer: int):
    """向指定练习集添加题目"""
    sets = load_all_sets()
    for s in sets:
        if s.id == set_id:
            idx = len(s.questions) + 1
            qid = f"{set_id}_q{idx:03d}"
            s.questions.append(Question(
                id=qid, title=title, options=options,
                answer=answer, set_id=set_id,
            ))
            save_all_sets(sets)
            return qid
    raise ValueError(f"练习集 {set_id} 不存在")


def remove_question_set(set_id: str):
    """删除练习集"""
    sets = load_all_sets()
    sets = [s for s in sets if s.id != set_id]
    save_all_sets(sets)


# ==================== 错题本操作 ====================


def load_errorbook() -> dict:
    """加载错题本，返回 {question_id: {wrong_count, last_wrong}}"""
    _ensure_files()
    return _load_json(ERRORBOOK_FILE)


def save_errorbook(data: dict):
    _save_json(ERRORBOOK_FILE, data)


def record_error(question_id: str):
    """记录一次错误"""
    data = load_errorbook()
    if question_id in data:
        data[question_id]["wrong_count"] += 1
    else:
        data[question_id] = {"wrong_count": 1}
    data[question_id]["last_wrong"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_errorbook(data)


def clear_error(question_id: str):
    """清除某题的错误记录"""
    data = load_errorbook()
    data.pop(question_id, None)
    save_errorbook(data)


def clear_all_errors():
    """清空错题本"""
    save_errorbook({})
