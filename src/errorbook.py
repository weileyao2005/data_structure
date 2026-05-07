import questionary
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table

from src.models import Question
from src.storage import (
    load_errorbook, get_question_by_id,
    clear_error, clear_all_errors,
)

console = Console()


def _get_error_questions() -> list[tuple[str, dict, Question | None]]:
    """获取错题列表，按错误次数降序排列。返回 [(question_id, info, Question|None), ...]"""
    eb = load_errorbook()
    if not eb:
        return []
    sorted_items = sorted(
        eb.items(),
        key=lambda kv: (-kv[1]["wrong_count"], kv[1].get("last_wrong", ""))
    )
    result = []
    for qid, info in sorted_items:
        q = get_question_by_id(qid)
        result.append((qid, info, q))
    return result


def show_error_list():
    """展示错题本"""
    console.clear()
    items = _get_error_questions()

    if not items:
        console.print()
        console.print(Panel("[green]错题本为空，继续保持！[/green]"))
        console.print()
        questionary.press_any_key_to_continue().ask()
        return

    console.print()
    table = Table(title="错题本")
    table.add_column("#", style="dim", width=4)
    table.add_column("题目", max_width=50)
    table.add_column("错误次数", justify="center", width=10)
    table.add_column("最近错误", width=20)

    choices = []
    for idx, (qid, info, q) in enumerate(items, 1):
        title = q.title if q else "(题目已删除)"
        if len(title) > 45:
            title = title[:42] + "..."
        table.add_row(
            str(idx),
            title,
            str(info["wrong_count"]),
            info.get("last_wrong", ""),
        )
        choices.append(questionary.Choice(
            f"[{info['wrong_count']}次] {title[:40]}",
            value=idx - 1,
        ))

    console.print(table)
    console.print()

    # 操作菜单
    action = questionary.select(
        "操作：",
        choices=[
            questionary.Choice("查看/复制错题", value="view"),
            questionary.Choice("重练全部错题", value="retry"),
            questionary.Choice("清除某题记录", value="clear_one"),
            questionary.Choice("清空错题本", value="clear_all"),
            questionary.Choice("返回主菜单", value="back"),
        ],
    ).ask()

    if action == "back" or action is None:
        return
    elif action == "view":
        _view_error_detail(items, choices)
    elif action == "retry":
        return "retry"  # 由 main.py 处理
    elif action == "clear_one":
        _clear_one_error(items, choices)
    elif action == "clear_all":
        _clear_all()


def _view_error_detail(items, choices):
    """查看并复制错题详情"""
    idx = questionary.select(
        "选择要查看的错题：",
        choices=choices,
    ).ask()
    if idx is None:
        return
    qid, info, q = items[idx]
    if q is None:
        console.print("[red]该题目已从题库中删除。[/red]")
        questionary.press_any_key_to_continue().ask()
        return

    console.clear()
    console.print()
    console.print(
        Panel.fit(
            f"[bold]错题 #{idx + 1}[/bold]  错误 [red]{info['wrong_count']}[/red] 次",
            border_style="red",
        )
    )
    console.print()

    # 题目（纯文本输出，方便复制）
    console.print(f"题目：[bold]{escape(q.title)}[/bold]")
    console.print()

    labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(q.options):
        marker = " →" if i == q.answer else "  "
        style = "bold green" if i == q.answer else ""
        console.print(f"  {marker} {labels[i]}. {opt}", style=style)

    console.print()
    console.print("[dim]提示：上方内容可在终端中用鼠标选中复制[/dim]")
    console.print()
    questionary.press_any_key_to_continue().ask()


def _clear_one_error(items, choices):
    """清除某题的错误记录"""
    idx = questionary.select(
        "选择要清除的错题：",
        choices=choices,
    ).ask()
    if idx is None:
        return
    qid, info, q = items[idx]
    clear_error(qid)
    console.print("[green]已清除。[/green]")
    questionary.press_any_key_to_continue().ask()


def _clear_all():
    confirm = questionary.confirm("确定要清空全部错题记录吗？").ask()
    if confirm:
        clear_all_errors()
        console.print("[green]错题本已清空。[/green]")
    questionary.press_any_key_to_continue().ask()


def get_error_question_ids() -> list[str]:
    """获取错题本中的所有题目 ID"""
    return list(load_errorbook().keys())


def get_error_questions_full() -> list[Question]:
    """获取错题对应的完整 Question 对象列表"""
    qids = get_error_question_ids()
    result = []
    for qid in qids:
        q = get_question_by_id(qid)
        if q is not None:
            result.append(q)
    return result
