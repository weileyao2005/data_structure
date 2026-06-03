# 项目概述

本项目有两个用途：

1. **数据结构刷题工具** — 终端交互式选择题练习系统，用于辅助 PTA 题库刷题和错题复习
2. **电磁场与电磁波 / 数字信号处理 课程复习** — 课本内容解析 + 课程笔记 + 答疑整理

---

## 目录结构

```
.
├── main.py                  # 数据结构刷题 CLI 入口
├── quiz_app.py              # 数据结构刷题 GUI 版（tkinter + 图片显示）
├── quiz.html                # 数据结构刷题 HTML 版（自包含暗色主题页面）
├── serve_quiz.py            # 启动本地 HTTP 服务器打开 quiz.html
├── generate_quiz_html.py    # 从 data/questions.json 生成 quiz.html
├── 刷题工具.bat             # 一键启动（CLI / GUI 二选一）
├── 刷题_HTML版.bat          # 一键启动 HTML 版
├── errorbook.json           # 错题本数据（运行时读写）
├── requirements.txt         # Python 依赖
│
├── src/                     # 刷题工具源码
│   ├── cli.py               # 终端交互界面（questionary + rich）
│   ├── storage.py           # 题库 JSON 读写
│   ├── quiz_engine.py       # 抽题、打乱、选项随机化逻辑
│   ├── errorbook.py         # 错题本管理
│   ├── models.py            # 数据模型
│   └── config.py            # 配置
│
├── data/                    # 题库数据
│   └── questions.json       # 所有题目（按练习集组织）
│
├── cheatsheet/              # 数据结构速查表
│   ├── cheatsheet.html      # 速查表页面
│   ├── generate_html.py     # 生成脚本
│   └── rawdata.md           # 原始数据
│
├── textbook/                # 课本内容（PDF 转 Markdown）
│   ├── 电磁场与电磁波(第5版)/
│   │   ├── 第1章 矢量分析/   # 按节拆分：1.1 ~ 1.9
│   │   ├── 第2章 电磁场的基本规律/
│   │   ├── ... (共8章)
│   │   └── *.pdf            # 对应原始 PDF
│   └── 数字信号处理(第3版)学习指导/
│       ├── 第1章 ... .md    # 按章组织（含习题解答）
│       ├── ... (共9章 + 附录 + 参考文献)
│       └── *.pdf            # 对应原始 PDF
│
├── lecture_notes/           # 课程笔记（含答疑、推导展开）
│   ├── 2026-05-27_第1章_矢量分析_1.2-1.3/
│   │   └── 课程笔记.md       # 坐标系 + 方向导数与梯度
│   ├── 2026-05-31_第1章_矢量分析_1.4-1.5/
│   │   └── 课程笔记.md       # 通量/散度 + 环流/旋度
│   └── 2026-05-31_第1章_矢量分析_1.6-1.9/
│       └── 课程笔记.md       # 无旋场/无散场 + 格林定理 + 亥姆霍兹定理
│
├── tools/                   # 构建/解析/可视化工具（一次性或偶尔使用）
│   ├── build_answers.py     # 从 parsed_questions.json 生成最终题库
│   ├── build_final.py       # 验证答案后生成最终 questions.json
│   ├── parse_temp.py        # 从 temp.md 提取题目为 parsed_questions.json
│   ├── add_ch07.py          # 添加第7章（图）题目到题库
│   ├── em_viz.py            # 电磁场散度/旋度交互式可视化
│   ├── parsed_questions.json  # 中间数据
│   ├── ch07_questions.json   # 中间数据
│   └── raw_questions.txt     # 原始题目文本
│
├── _temp/                   # 临时文件（待清理）
│   ├── temp.docx / temp.md  # 工作文档
│   ├── media/               # 从 docx 提取的图片
│   └── ...
│
├── xAI_Application/         # xAI 求职材料（与本项目无关）
└── .claude/                 # Claude Code 配置
```

---

## 刷题工具使用方法

```bash
# 终端版
python main.py

# GUI 版（支持图片显示）
python quiz_app.py

# HTML 版
python serve_quiz.py
# 或双击 刷题_HTML版.bat
```

## 课本与笔记

- 课本 PDF 已通过 Firecrawl parse 转换为 Markdown，存放在 `textbook/` 下
- 课程笔记是对课本关键知识点的讲解展开，包含详细的分步推导、答疑和直观类比
- 笔记编号与课本节号对应（如 1.3.1, 1.3.2），方便对照阅读
