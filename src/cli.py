import questionary
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src.models import Question, QuestionSet, QuizResult
from src.quiz_engine import shuffle_options
from src.storage import record_error, load_errorbook, get_question_by_id

console = Console()


def _style_choice(choice):
    """questionary select 样式：选中项高亮"""
    return choice


def show_main_menu() -> str:
    console.clear()
    console.print()
    console.print(
        Panel.fit(
            "[bold cyan]数据结构刷题工具[/bold cyan]",
            border_style="cyan",
        )
    )
    console.print()
    choice = questionary.select(
        "请选择操作：",
        choices=[
            questionary.Choice("1. 开始刷题", value="quiz"),
            questionary.Choice("2. 错题本", value="errorbook"),
            questionary.Choice("3. 题库管理", value="manage"),
            questionary.Choice("4. 退出", value="exit"),
        ],
    ).ask()
    return choice


# ==================== 题库管理子菜单 ====================


def show_manage_menu() -> str | None:
    console.clear()
    console.print()
    console.print("[bold yellow]题库管理[/bold yellow]")
    console.print()
    choice = questionary.select(
        "请选择操作：",
        choices=[
            questionary.Choice("1. 查看练习集列表", value="list"),
            questionary.Choice("2. 新增练习集", value="add_set"),
            questionary.Choice("3. 添加题目", value="add_question"),
            questionary.Choice("4. 删除练习集", value="remove_set"),
            questionary.Choice("5. 返回主菜单", value="back"),
        ],
    ).ask()
    return choice


# ==================== 刷题设置 ====================


def select_sets(all_sets: list[QuestionSet]) -> list[str]:
    """勾选练习集，返回选中的 set_id 列表"""
    console.clear()
    console.print()
    console.print("[bold]选择练习集[/bold] (空格勾选/取消, 回车确认)")
    console.print()

    choices = []
    for s in all_sets:
        label = f"{s.name}  ({len(s.questions)} 题)"
        choices.append(questionary.Choice(label, value=s.id, checked=False))

    if not choices:
        console.print("[yellow]题库中没有练习集，请先在题库管理中创建。[/yellow]")
        questionary.press_any_key_to_continue().ask()
        return []

    selected = questionary.checkbox(
        "勾选要练习的练习集：",
        choices=choices,
    ).ask()

    if selected is None:
        return []
    return list(selected)


def ask_shuffle() -> bool:
    console.print()
    answer = questionary.select(
        "题目顺序：",
        choices=[
            questionary.Choice("打乱顺序（推荐）", value=True),
            questionary.Choice("保持原序", value=False),
        ],
    ).ask()
    return answer if answer is not None else True


def ask_total_questions(max_available: int) -> int:
    console.print()
    result = questionary.text(
        f"总共要练几道题？（可用 {max_available} 道）",
        default=str(max_available),
        validate=lambda text: (
            True if text.isdigit() and 1 <= int(text) <= max_available
            else f"请输入 1 - {max_available} 之间的数字"
        ),
    ).ask()
    return int(result) if result else max_available


# ==================== 答题循环 ====================


def run_quiz_session(questions: list[Question]) -> list[QuizResult]:
    """逐题作答，返回答题结果列表。Ctrl+C 可随时退出。"""
    results: list[QuizResult] = []
    total = len(questions)

    if total == 0:
        console.print("[yellow]没有可用的题目。[/yellow]")
        questionary.press_any_key_to_continue().ask()
        return results

    i = 0
    while i < total:
        q = questions[i]
        console.clear()

        # 题头
        set_label = q.set_id
        console.print(f"[dim]第 {i + 1}/{total} 题  [{set_label}][/dim]")
        console.print()

        # 题目文字（escape 防止 rich 误解析 [1] 等字符为标记）
        console.print(f"  [bold]{escape(q.title)}[/bold]")
        console.print()

        # 打乱选项
        shuffled, correct_idx, _ = shuffle_options(q)

        # 让用户选择
        try:
            user_answer = questionary.select(
                "请选择答案（Ctrl+C 退出本次刷题）：",
                choices=[
                    questionary.Choice(opt, value=idx)
                    for idx, opt in enumerate(shuffled)
                ],
            ).ask()
        except KeyboardInterrupt:
            user_answer = None

        if user_answer is None:  # 用户按了 Ctrl+C
            console.print()
            try:
                confirm = questionary.confirm("确定要退出本次刷题吗？已答题目会保留。").ask()
            except KeyboardInterrupt:
                confirm = True
            if confirm or confirm is None:
                break
            else:
                continue  # 回到当前题目重新作答

        is_correct = user_answer == correct_idx

        # 即时反馈
        console.print()
        if is_correct:
            console.print(f"  [bold green]正确！[/bold green]")
        else:
            correct_label = shuffled[correct_idx]
            user_label = shuffled[user_answer]
            console.print(f"  [bold red]错误！[/bold red]")
            console.print(f"  你的答案: [red]{user_label}[/red]")
            console.print(f"  正确答案: [green]{correct_label}[/green]")
            record_error(q.id)

        results.append(QuizResult(
            question=q,
            user_choice=user_answer,
            is_correct=is_correct,
            shuffled_options=shuffled,
            shuffled_answer=correct_idx,
        ))

        i += 1

        # 等待继续
        if i < total:
            console.print()
            try:
                questionary.press_any_key_to_continue(message="按任意键继续（Ctrl+C 退出）...").ask()
            except KeyboardInterrupt:
                console.print()
                break

    return results


def show_result_summary(results: list[QuizResult], planned_total: int = 0):
    """展示本轮答题统计"""
    console.clear()
    if not results:
        console.print("[yellow]没有答题记录。[/yellow]")
        questionary.press_any_key_to_continue().ask()
        return

    total = len(results)
    correct = sum(1 for r in results if r.is_correct)
    wrong = total - correct
    accuracy = correct / total * 100 if total > 0 else 0

    console.print()
    status = ""
    if planned_total and total < planned_total:
        status = f" [dim](中途退出，已完成 {total}/{planned_total})[/dim]"
    console.print(Panel.fit(f"[bold]答题结果[/bold]{status}", border_style="cyan"))
    console.print()

    table = Table(title=f"共 {total} 题")
    table.add_column("", style="dim")
    table.add_column("数量")
    table.add_column("占比")

    table.add_row("[green]✓ 正确[/green]", str(correct), f"{accuracy:.1f}%")
    table.add_row("[red]✗ 错误[/red]", str(wrong), f"{100 - accuracy:.1f}%")

    console.print(table)

    if accuracy == 100:
        console.print()
        console.print("  [bold green]🎉 全部正确！[/bold green]")

    console.print()
    questionary.press_any_key_to_continue().ask()
