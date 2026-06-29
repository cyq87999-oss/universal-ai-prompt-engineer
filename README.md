# 万能AI短视频生产引擎 (Universal AI Prompt Engineer)

> 全链路 AI 短视频生产流水线 — 从一句话创意到完整短视频的端到端解决方案

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-222222?logo=github-pages)](https://cyq87999-oss.github.io/universal-ai-prompt-engineer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 概述

本技能实现了从一句话创意到完整短视频的**全自动生产流水线**，整合了 4 个专业 Agent 工作流、8 大提示词维度、导演级分镜节奏模板，以及 FFmpeg/剪映 API 两条剪辑路径。

### 端到端生产流程

```
用户输入主题
    ↓
Phase 1: 剧本撰写 (script_writing Agent)
    ↓
Phase 2: 导演级提示词工程 (6 大公式体系)
    ↓
Phase 3: AI 图像生成 (batch_image_gen Agent)
    ↓
Phase 4: AI 视频片段生成 (batch_video_gen Agent)
    ↓
Phase 5: 视频剪辑合成 (video_edit Agent / FFmpeg / 剪映 API)
    ↓
Phase 6: 导出与发布
```

## 核心能力

| 阶段 | 产出 | 技术方案 |
|------|------|----------|
| **剧本** | 分场景剧本 + 分镜头表 | script_writing Agent (豆包大模型) |
| **提示词** | 6 公式体系 + 自定义词库组合 | 8 大维度 + 20 章分类数据 |
| **图像** | 每场景一张高质量图片 | batch_image_gen Agent (即梦 Seedream) |
| **视频片段** | 每场景一段连续视频 | batch_video_gen Agent (即梦 Seedance) |
| **剪辑合成** | 完整短视频 | video_edit Agent / FFmpeg / 剪映 API |

## 文件结构

```
universal-ai-prompt-engineer/
├── SKILL.md                 # 主控文档 v3.0 Directors Edition
├── references/              # 16 个参考数据文件
│   ├── agents-workflow.md         # 4 节点 Agent 工作流
│   ├── director-prompt-template.md # 导演级提示词模板
│   ├── prompt-data-complete.md    # 20 章完整数据体系
│   ├── scene_background.md        # ①场景背景
│   ├── art_style.md               # ②风格艺术
│   ├── camera_language.md         # ③镜头语言
│   ├── shot_description.md        # ④镜头描述
│   ├── character_costume.md       # ⑤人物服装
│   ├── color_lighting.md          # ⑥色调光效
│   ├── culture_environment.md     # ⑦文化与环境
│   ├── details_decoration.md      # ⑧细节装饰
│   ├── ai-prompt-formula.md       # AI 提示词构建方法论
│   ├── prompt-universal-formula.md # 万能公式技能手册
│   ├── formula-ai-prompt.md       # AI 提示词万能公式
│   ├── prompt_templates.md        # 5 套提示词模板
│   └── workflow/                  # 短视频工作流定义
├── scripts/                 # SD 模型脚本
│   ├── sd_model.py          # SD 完整推理管线
│   ├── lora_train.py        # LoRA 微调训练
│   └── dpo_train.py         # DPO 偏好优化
└── assets/
    └── prompt_templates.md  # 可复制的模板文档
```

## 6 大提示词公式体系

| 级别 | 公式名称 | 适用场景 |
|------|---------|----------|
| 基础 | 7 大元素公式 | 快速出词 |
| 标准 | 视频/图像双公式 | 通用生成 |
| 进阶 | 8 大维度组合公式 | 精细控制 |
| 高级 | 6 模块万能公式 | 专业创作 |
| 导演级 | S-A-C-S-C 五步法 | 精确参数化控制 |
| 参考 | 20 章完整数据体系 | 自定义词库组合 |

## 安装使用

本技能为 CodeBuddy 技能包。安装方式：

```bash
# 1. 下载技能包
wget https://github.com/cyq87999-oss/universal-ai-prompt-engineer/releases/latest/download/universal-ai-prompt-engineer.zip

# 2. 解压到 CodeBuddy skills 目录
unzip universal-ai-prompt-engineer.zip -d ~/.codebuddy/skills/

# 3. 在 CodeBuddy 中触发
# 输入 "帮我做个短视频" 或 "/video" 即可激活
```

## 触发方式

在 CodeBuddy 对话中输入以下任一内容即可激活：

- "帮我做个短视频" / "AI 短视频"
- "帮我写提示词" / "生成 prompt" / "即梦提示词"
- "分镜脚本" / "Storyboard"
- "FFmpeg 剪辑" / "剪映 API"
- "/video" / "/prompt" / "/jimeng" / "/storyboard"

## 参考与致谢

- 工作流定义：Coze Workflow 强化版短视频工作流 + AGENTS.md 4 节点定义
- 提示词体系：AI提示词构建方法论 + 万能公式技能手册 + 20 章完整数据
- 导演级模板：即梦视频导演级提示词模板
- 视频剪辑：FFmpeg 8.1.1 + 剪映创作者工具 API
- 模型配置：Stable Diffusion Model Config (LoRA + DPO)

## License

MIT
