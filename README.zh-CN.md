# Codex Co-Mathematician

> [English](README.md) | 中文

一个轻量级、由 Codex 驱动的数学研究工作区模式。

本项目受 Google DeepMind
[AI co-mathematician 论文](https://arxiv.org/abs/2605.06651)中公开设计原则启发，
但**不是**对其系统的复现。本项目将这些思想改写为一个 Codex-native、基于文件系统的
轻量工作流。

本仓库**不是**新的多 agent 平台。Codex 本身就是 driver；仓库文件系统
就是 shared artifact store；Codex subagents 扮演 workstream coordinator、
specialist 和 reviewer；harness 只负责 schema、状态、gating、报告骨架和验证脚本。

## 包含什么

- `AGENTS.md`：本工作区的硬规则。
- `.agents/skills/codex-co-mathematician/`：Codex Skill 和可复用模板。
- `.codex/`：窄角色 custom agents，包括 proof、computation、review、citation checking 和 synthesis。
- `harness/co_math/`：用于 workspace 状态和 gates 的小型 Python harness。
- `workspace/`：新项目的空 scaffold。

## 不包含什么

- 不包含已解决的研究项目。
- 不包含下载的论文库。
- 不包含外部仓库快照。
- 不包含 Web app 或 agent runtime。
- 不包含 proprietary prompts 或私有系统内容。

## 安装

支持 Python 3.9+。

```bash
python3 -m pip install -e .
co-math --help
```

不安装也可以运行：

```bash
PYTHONPATH=. python3 -m harness.co_math.cli --help
```

## 使用 Skill

让 Codex 使用 `codex-co-mathematician` Skill。流程是：

```text
onboarding -> research question formalization -> goal approval -> workstreams -> reviewer loop -> final working paper
```

核心规则很简单：用户明确 approve goal 之前，不得启动 workstream；workstream report
未通过独立 reviewer 审查之前，不得标记 complete。

## 开始一个新项目

初始化 workspace：

```bash
co-math init --workspace workspace
```

onboarding 阶段，Codex 应更新：

```text
workspace/project/PROJECT.md
workspace/project/GOALS.yaml
workspace/project/PROJECT_STATUS.md
workspace/project/messages.jsonl
```

draft goal 不可执行。只有当 goal 状态恰好是下面这样，才能启动 workstream：

```yaml
status: approved
```

检查 goal approval：

```bash
co-math check-gate --workspace workspace --gate goal_approval --goal-id G1
```

为 approved goal 创建 workstream：

```bash
co-math new-workstream \
  --workspace workspace \
  --goal-id G1 \
  --title "Literature baseline review" \
  --kind literature
```

允许的 workstream kind 是 `proof`、`computation`、`literature` 和 `review`。

## Harness 命令

```bash
co-math init --workspace workspace
co-math append-message --workspace workspace --sender project_coordinator --recipient user --type status --content "..."
co-math new-workstream --workspace workspace --goal-id G1 --title "..." --kind proof
co-math check-gate --workspace workspace --gate goal_approval --goal-id G1
co-math check-gate --workspace workspace --gate workstream_completion --workstream-id WS-G1-001-example
co-math render-final --workspace workspace
```

## 测试

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest harness/tests -q
```

## 许可证

MIT。见 `LICENSE`。
