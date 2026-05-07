"""数据结构刷题工具 — 主入口"""

import questionary
from rich.console import Console

from src.cli import (
    show_main_menu, show_manage_menu,
    select_sets, ask_shuffle, ask_total_questions,
    run_quiz_session, show_result_summary,
)
from src.storage import (
    load_all_sets, add_question_set, add_question_to_set,
    remove_question_set, get_set_by_id,
)
from src.quiz_engine import select_questions
from src.errorbook import show_error_list, get_error_questions_full

console = Console()


def quiz_flow():
    """刷题流程"""
    all_sets = load_all_sets()
    if not all_sets:
        console.print()
        console.print("[yellow]题库为空！请先在「题库管理」中添加练习集和题目。[/yellow]")
        console.print()
        questionary.press_any_key_to_continue().ask()
        return

    # 1. 勾选练习集
    set_ids = select_sets(all_sets)
    if not set_ids:
        return

    # 2. 打乱还是顺序
    shuffle_order = ask_shuffle()

    # 3. 总题数
    available = sum(
        len(s.questions) for s in all_sets if s.id in set_ids
    )
    total = ask_total_questions(available)

    # 4. 抽题
    questions = select_questions(set_ids, total, all_sets, shuffle_order)

    # 5. 开始答题
    results = run_quiz_session(questions)

    # 6. 结果摘要
    show_result_summary(results, planned_total=total)


def errorbook_flow():
    """错题本流程"""
    while True:
        result = show_error_list()
        if result == "retry":
            questions = get_error_questions_full()
            if not questions:
                console.print("[yellow]没有可重练的错题。[/yellow]")
                questionary.press_any_key_to_continue().ask()
                continue
            shuffle_order = ask_shuffle()
            if shuffle_order:
                import random
                random.shuffle(questions)
            results = run_quiz_session(questions)
            show_result_summary(results, planned_total=len(questions))
        else:
            break


def manage_flow():
    """题库管理流程"""
    while True:
        action = show_manage_menu()
        if action is None or action == "back":
            break
        elif action == "list":
            _list_sets()
        elif action == "add_set":
            _add_set()
        elif action == "add_question":
            _add_question()
        elif action == "remove_set":
            _remove_set()


def _list_sets():
    console.clear()
    sets = load_all_sets()
    if not sets:
        console.print("[yellow]题库为空。[/yellow]")
    else:
        for s in sets:
            console.print(f"  [{s.id}] [bold]{s.name}[/bold] — {len(s.questions)} 题")
    console.print()
    questionary.press_any_key_to_continue().ask()


def _add_set():
    console.clear()
    sid = questionary.text(
        "练习集 ID（英文，如 ch01）：",
        validate=lambda t: True if t.strip() and " " not in t else "不能为空或含空格",
    ).ask()
    if not sid:
        return
    name = questionary.text("练习集名称（如 第一章 绪论）：").ask()
    if not name:
        return
    try:
        add_question_set(sid.strip(), name.strip())
        console.print(f"[green]练习集 [{sid}] {name} 创建成功。[/green]")
    except ValueError as e:
        console.print(f"[red]{e}[/red]")
    questionary.press_any_key_to_continue().ask()


def _add_question():
    sets = load_all_sets()
    if not sets:
        console.print("[yellow]请先创建练习集。[/yellow]")
        questionary.press_any_key_to_continue().ask()
        return

    console.clear()
    sid = questionary.select(
        "选择目标练习集：",
        choices=[
            questionary.Choice(f"{s.name} ({len(s.questions)}题)", value=s.id)
            for s in sets
        ],
    ).ask()
    if not sid:
        return

    console.print()
    title = questionary.text("题目内容：").ask()
    if not title:
        return

    options = []
    labels = ["A", "B", "C", "D"]
    console.print()
    for label in labels:
        opt = questionary.text(f"选项 {label}：").ask()
        if opt is None:
            return
        options.append(opt.strip())

    answer = questionary.select(
        "正确答案：",
        choices=[
            questionary.Choice(f"{labels[i]}. {options[i]}", value=i)
            for i in range(4)
        ],
    ).ask()
    if answer is None:
        return

    qid = add_question_to_set(sid, title.strip(), options, answer)
    console.print(f"[green]题目 {qid} 添加成功。[/green]")
    questionary.press_any_key_to_continue().ask()


def _remove_set():
    sets = load_all_sets()
    if not sets:
        console.print("[yellow]没有可删除的练习集。[/yellow]")
        questionary.press_any_key_to_continue().ask()
        return

    sid = questionary.select(
        "选择要删除的练习集：",
        choices=[
            questionary.Choice(f"{s.name} ({len(s.questions)}题)", value=s.id)
            for s in sets
        ],
    ).ask()
    if not sid:
        return
    confirm = questionary.confirm(f"确定要删除练习集 [{sid}] 及其中全部题目吗？").ask()
    if confirm:
        remove_question_set(sid)
        console.print("[green]已删除。[/green]")
    questionary.press_any_key_to_continue().ask()


def main():
    while True:
        choice = show_main_menu()
        if choice is None or choice == "exit":
            console.print()
            console.print("[dim]再见！[/dim]")
            break
        elif choice == "quiz":
            quiz_flow()
        elif choice == "errorbook":
            errorbook_flow()
        elif choice == "manage":
            manage_flow()


if __name__ == "__main__":
    main()
