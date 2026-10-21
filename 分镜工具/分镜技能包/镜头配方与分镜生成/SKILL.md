---
name: shot-recipe-card
description: 镜头配方与分镜生成一体化技能（Shot-Recipe-Card 三合一），对标 video-shotcraft。技能1配方库：157个电影级镜头配方卡片、211套风格、157组预览元数据、Ink Press 36.2s模板；技能2分镜推理：接收用户需求自动编排标准化分镜JSON（支持模板骨架/自动编排/节拍对齐）；技能3 Remotion工程生成：分镜JSON一键生成完整可运行的 Remotion TSX 工程。当用户要做产品宣传片/给截图找电影化镜头运动/编排分镜/生成Remotion视频工程时使用，一条流水线从需求直达可渲染代码。
---

# Shot-Recipe-Card 镜头配方与分镜生成（三合一）

对标 video-shotcraft 的完整视频创作流水线：**配方检索 → 分镜编排 → Remotion 工程生成**。

## 三层架构

| 层 | 模块 | 输入 | 输出 |
|----|------|------|------|
| 技能1 配方库 | `scripts/library.py` `ShotRecipeLibrary` | 查询条件 | 镜头配方卡片/风格/模板 |
| 技能2 分镜推理 | `scripts/shot_agent.py` `ShotAgentReasoner` | 用户需求+时长+素材 | 标准化分镜 JSON |
| 技能3 工程生成 | `scripts/remotion_generator.py` `RemotionCodeGenerator` | 分镜 JSON | Remotion TSX 工程 |

## 资产总览

- **157 张镜头配方卡片**（`scripts/recipes/*.json`），10 大分类：camera / transitions / ui-entrance / typography / interaction / rhythm / opening / data / 3d-scene / outro
- **211 套风格配置**（`scripts/styles/style_manifest.json`）：inkpress-dark、midnight、modern-light、sage、coral、iris、deep-ocean、obsidian-violet、vintage-kraft 等
- **157 组运动预览元数据**（`scripts/motion_previews/preview_manifest.json`）
- **Ink Press 36.2s 成品模板**（`scripts/templates/inkpress_promo_36.2s.json`）：36.2s / 30fps / 1920×1080

## 执行流程

### 第 1 步：理解需求
从用户输入提取：素材（截图/图片）、总时长、想要的类别（开场/转场/数据展示等）、是否用模板、节拍点。

### 第 2 步：检索配方（技能1）
```python
import sys; sys.path.insert(0, "<技能根>/scripts")
from library import ShotRecipeLibrary
lib = ShotRecipeLibrary(auto_populate=False)   # 从本地资产加载
lib.searchShots(tags=["transitions"])          # 按标签筛选
lib.getShotById("whip-pan")                    # 完整配方卡
lib.listAllStyles()                            # 全部风格
lib.getTemplate("inkpress_promo_36.2s")        # 成品模板
```
六个标准接口：`listAllShots / searchShots / getShotById / getMotionPreview / getTemplate / listAllStyles`。

### 第 3 步：编排分镜（技能2）
```python
from shot_agent import ShotAgentReasoner
agent = ShotAgentReasoner(lib)
sb = agent.build_storyboard(
    user_prompt="产品演示短片",        # 需求文案
    total_duration=36.2,              # 总时长（秒）
    asset_list=["./assets/s1.png"],   # 素材路径（可选）
    beat_points=[0, 2.4, 5.0],        # 音频节拍点（可选，自动对齐镜头起点）
    template_id="inkpress_promo_36.2s",  # 模板模式（可选）
    style_id="inkpress-dark"          # 风格（可选）
)
```
两种编排模式：**模板模式**（template_id 存在时按 Ink Press 骨架填充）、**自动模式**（按素材类型筛选配方，循环填满总时长）。

### 第 4 步：生成 Remotion 工程（技能3）
```python
from remotion_generator import RemotionCodeGenerator
gen = RemotionCodeGenerator(lib)
out_dir = gen.generate(sb, output_dir="<输出目录>")
```
产出：`VideoMain.tsx`（含组件引用、时长帧数、素材、参数）、`remotion.config.ts`、`package.json`。用户 `npm install && npm run dev` 即可在 Remotion Studio 预览，`npm run render` 出片。

### 第 5 步：交付
向用户说明：分镜表（shotId/时长/素材/参数）、选用的风格建议、工程目录路径、渲染命令。渲染所需 shotRecipes.tsx 组件按 remotionComponent 名对应实现。

## 典型问答

- 「给产品截图做个 36 秒宣传片」→ 技能1 取 Ink Press 模板 → 技能2 模板编排 → 技能3 出工程
- 「8 秒数据增长展示」→ 技能2 自动编排（digit-roll-counter 等配方）→ 技能3 出工程
- 「有哪些转场镜头」→ 技能1 `searchShots(tags=["transitions"])` 输出 5 张配方卡（含时长/素材要求/避坑）

## 边界与注意

- 技能产出 Remotion 工程**代码骨架**；`shotRecipes.tsx` 组件库（各 remotionComponent 的具体实现）需按配方卡 `implementationNotes` 补充或从 video-shotcraft 官方 demo 移植
- `motion_previews` 中的 .mp4 为元数据引用，实际预览文件到 video-shotcraft 资产或本地存放位置查找
- 组件名自动转合法 JS 标识符（`Shot2.5D_Page_Push` → `Shot2_5D_Page_Push`）
- 追加配方：向 `scripts/recipes/` 写符合 schema 的 JSON 即可被加载