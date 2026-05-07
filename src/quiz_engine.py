import random

from src.models import Question, QuestionSet


LABELS = ["A", "B", "C", "D"]


def shuffle_options(question: Question) -> tuple[list[str], int, int]:
    """随机打乱选项顺序。

    Returns:
        (shuffled_options, shuffled_correct_index, user_answer_index)
        shuffled_options: 打乱后的选项列表（带 ABCD 前缀）
        shuffled_correct_index: 打乱后正确答案的索引
        第三个返回值同 shuffled_correct_index（答题时用于判断对错）
    """
    indices = list(range(4))
    random.shuffle(indices)
    shuffled = [f"{LABELS[i]}. {question.options[idx]}" for i, idx in enumerate(indices)]
    new_answer = indices.index(question.answer)
    return shuffled, new_answer, new_answer


def distribute(total: int, set_ids: list[str], all_sets: list[QuestionSet]) -> dict[str, int]:
    """将 total 道题均分到各练习集。

    策略：
    1. 每人先分 total // n 道
    2. 余数按集合题量从多到少依次补 1 道
    3. 某集合题量不足时，缺额分配给其他题量充足的集合
    """
    n = len(set_ids)
    available = {}
    for sid in set_ids:
        s = next((x for x in all_sets if x.id == sid), None)
        available[sid] = len(s.questions) if s else 0

    # 每人基础分配
    base = total // n
    allocation = {sid: min(base, available[sid]) for sid in set_ids}

    # 余数分配
    remainder = total - sum(allocation.values())
    if remainder > 0:
        # 按当前可用余量从多到少排序
        pool = [(sid, available[sid] - allocation[sid]) for sid in set_ids]
        pool.sort(key=lambda x: -x[1])
        for sid, _ in pool:
            if remainder <= 0:
                break
            if allocation[sid] < available[sid]:
                allocation[sid] += 1
                remainder -= 1

    # 处理不足：把缺额重新分配
    deficit = {}
    surplus_sids = []
    for sid in set_ids:
        if allocation[sid] < base and allocation[sid] >= available[sid]:
            deficit[sid] = base - allocation[sid]
        elif allocation[sid] < available[sid]:
            surplus_sids.append(sid)

    if deficit and surplus_sids:
        total_deficit = sum(deficit.values())
        # 按剩余题量比例分配缺额
        surplus_pool = []
        for sid in surplus_sids:
            remaining = available[sid] - allocation[sid]
            if remaining > 0:
                surplus_pool.append((sid, remaining))
        if surplus_pool:
            total_surplus = sum(r for _, r in surplus_pool)
            for sid, remaining in surplus_pool:
                extra = min(
                    total_deficit * remaining // total_surplus,
                    remaining,
                    total_deficit,
                )
                allocation[sid] += extra
                total_deficit -= extra

    return allocation


def select_questions(
    set_ids: list[str],
    total: int,
    all_sets: list[QuestionSet],
    shuffle_order: bool = True,
) -> list[Question]:
    """从指定练习集中按均分策略抽题。

    Args:
        set_ids: 用户勾选的练习集 ID 列表
        total: 目标总题数
        all_sets: 全部练习集
        shuffle_order: 是否打乱最终题目顺序

    Returns:
        抽取的题目列表
    """
    total_available = sum(
        len(s.questions) for s in all_sets if s.id in set_ids
    )
    if total_available == 0:
        return []
    total = min(total, total_available)

    allocation = distribute(total, set_ids, all_sets)

    result = []
    for sid in set_ids:
        count = allocation.get(sid, 0)
        if count <= 0:
            continue
        s = next(x for x in all_sets if x.id == sid)
        picked = random.sample(s.questions, min(count, len(s.questions)))
        result.extend(picked)

    if shuffle_order:
        random.shuffle(result)

    return result
