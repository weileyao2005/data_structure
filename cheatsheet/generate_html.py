import re
import html as html_mod

def parse_rawdata(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    questions = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].rstrip('\n').rstrip('\r')

        # 检测题目开头: 数字-数字 或 分数 数字
        is_question_start = False

        m1 = re.match(r'^(\d+-\d+)', line)
        if m1:
            is_question_start = True
        elif re.match(r'^分数\s+(\d+)', line):
            is_question_start = True

        if not is_question_start:
            i += 1
            continue

        # 找下一个题目开头
        j = i + 1
        while j < n:
            next_line = lines[j].rstrip('\n').rstrip('\r')
            if re.match(r'^(\d+-\d+)', next_line):
                break
            if re.match(r'^分数\s+(\d+)', next_line):
                prev_line = lines[j-1].rstrip('\n').rstrip('\r').strip() if j > 0 else ""
                prev_prev_line = lines[j-2].rstrip('\n').rstrip('\r').strip() if j > 1 else ""
                if prev_line == "" or prev_line in ["评测结果", "得分"] or prev_prev_line == "评测结果":
                    break
                if re.match(r'^\d+\s*分$', prev_line):
                    break
            j += 1

        section = lines[i:j]
        i = j

        q = parse_section(section)
        if q:
            questions.append(q)

    return questions


def parse_section(lines):
    """解析一个题目的所有行"""
    n = len(lines)
    qid = ""
    score = ""
    title = ""
    author = ""
    unit = ""

    # --- 第一遍：扫描头部，找到 作者 和 单位 的位置 ---
    author_idx = -1
    unit_idx = -1
    for idx in range(min(15, n)):  # 头部不会超过15行
        line = lines[idx].strip()
        if re.match(r'^作者\s+', line):
            author_idx = idx
        if re.match(r'^单位\s+', line):
            unit_idx = idx
        if author_idx >= 0 and unit_idx >= 0:
            break

    if unit_idx < 0:
        unit_idx = author_idx + 1 if author_idx >= 0 else 2
    if author_idx < 0:
        author_idx = unit_idx - 1 if unit_idx > 0 else 1

    # --- 解析头部行 (0 到 author_idx-1) ---
    for idx in range(0, author_idx):
        line = lines[idx].strip()
        if not line:
            continue

        m_num = re.match(r'^(\d+-\d+)\s*(.*)', line)
        m_score = re.match(r'^分数\s+(\d+)', line)

        if m_num:
            qid = m_num.group(1)
            rest = m_num.group(2).strip()
            if rest and not title:
                title = rest
        elif m_score:
            score = m_score.group(1)
        elif not title and line:
            # 不是题号，不是分数 => 就是标题
            title = line

    # --- 解析作者/单位 ---
    if author_idx < n:
        m_a = re.match(r'^作者\s+(.+)', lines[author_idx].strip())
        if m_a:
            author = m_a.group(1)
    if unit_idx < n:
        m_u = re.match(r'^单位\s+(.+)', lines[unit_idx].strip())
        if m_u:
            unit = m_u.group(1)

    # --- 解析描述和答案代码 ---
    desc_start = unit_idx + 1
    answer_start = -1
    answer_end = -1

    for idx in range(desc_start, n):
        line = lines[idx].strip()
        if line == '/* === 答案代码块 === */':
            answer_start = idx + 1
        elif answer_start > 0 and answer_end < 0:
            if line in ['评测结果', '测试数据'] or re.match(r'^\d+-\d+', line):
                answer_end = idx
                break

    if answer_start > 0 and answer_end < 0:
        answer_end = n

    # 提取描述
    desc_lines = []
    desc_end = answer_start - 1 if answer_start > 0 else n
    for idx in range(desc_start, desc_end):
        if idx < n:
            desc_lines.append(lines[idx].rstrip('\n').rstrip('\r'))

    # 提取答案
    answer_lines = []
    if answer_start > 0:
        for idx in range(answer_start, answer_end):
            if idx < n:
                answer_lines.append(lines[idx].rstrip('\n').rstrip('\r'))

    # 清理描述首尾空行
    while desc_lines and not desc_lines[0].strip():
        desc_lines.pop(0)
    while desc_lines and not desc_lines[-1].strip():
        desc_lines.pop()

    if not title:
        title = "未命名题目"

    return {
        'qid': qid,
        'title': title,
        'score': score,
        'author': author,
        'unit': unit,
        'desc': '\n'.join(desc_lines),
        'answer': '\n'.join(answer_lines),
    }


def generate_html(questions, output_path):
    def esc(text):
        return html_mod.escape(text)

    css = """
    @page { size: A4; margin: 2mm; }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: "Microsoft YaHei", "SimHei", "Consolas", "Courier New", monospace;
      font-size: 5pt;
      line-height: 1.1;
      column-count: 5;
      column-gap: 4px;
      padding: 1px;
      color: #111;
      background: #fff;
      overflow-wrap: break-word;
    }
    h1 {
      font-size: 8pt;
      text-align: center;
      column-span: all;
      margin: 0 0 2px 0;
      padding-bottom: 1px;
      border-bottom: 1px solid #333;
    }
    .card {
      margin-bottom: 2px;
      padding-bottom: 1px;
      border-bottom: 1px dotted #ddd;
    }
    .card h2 {
      font-size: 6pt;
      font-weight: 700;
      color: #000;
      margin-bottom: 0;
    }
    .meta {
      font-size: 4pt;
      color: #999;
      margin-bottom: 0;
    }
    .desc {
      font-size: 6pt;
      color: #333;
      white-space: pre-wrap;
      word-break: break-all;
      margin-bottom: 1px;
    }
    .answer {
      font-size: 5.5pt;
      color: #c00;
      white-space: pre-wrap;
      word-break: break-all;
    }
    """

    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="zh">',
        '<head>',
        '<meta charset="UTF-8">',
        '<style>',
        css,
        '</style>',
        '</head>',
        '<body>',
        '<h1>Data Structure Cheat Sheet</h1>',
    ]

    for q in questions:
        title_full = q['title']
        if q['qid']:
            title_full = q['qid'] + ' ' + title_full

        meta_parts = []
        if q['score']:
            meta_parts.append(f'分数 {q["score"]}')
        if q['author']:
            meta_parts.append(f'作者 {q["author"]}')
        if q['unit']:
            meta_parts.append(f'单位 {q["unit"]}')

        html_parts.append('<div class="card">')
        html_parts.append(f'<h2>{esc(title_full)}</h2>')

        if meta_parts:
            meta_str = ' | '.join(meta_parts)
            html_parts.append(f'<div class="meta">{esc(meta_str)}</div>')

        if q['desc']:
            html_parts.append(f'<div class="desc">{esc(q["desc"])}</div>')

        if q['answer']:
            html_parts.append(f'<div class="answer">{esc(q["answer"])}</div>')

        html_parts.append('</div>')

    html_parts.append('</body>')
    html_parts.append('</html>')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print(f"Generated {output_path} with {len(questions)} questions.")


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    questions = parse_rawdata('rawdata.md')
    for i, q in enumerate(questions):
        print(f"[{i+1}] qid={q['qid']} | title={q['title']} | score={q['score']} | author={q['author']} | unit={q['unit']} | desc_len={len(q['desc'])} | answer_len={len(q['answer'])}")
    generate_html(questions, 'cheatsheet.html')
