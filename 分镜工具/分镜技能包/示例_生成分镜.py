# -*- coding: utf-8 -*-
"""示例：需求 → 分镜 JSON → Remotion 工程（一条流水线）
改 user_prompt 就能换需求；删掉 template_id 那行则改为自动编排模式。
"""
import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "镜头配方与分镜生成", "scripts")
sys.path.insert(0, BASE)

from library import ShotRecipeLibrary          # 技能1：配方库
from shot_agent import ShotAgentReasoner       # 技能2：分镜编排
from remotion_generator import RemotionCodeGenerator  # 技能3：Remotion工程

lib = ShotRecipeLibrary(auto_populate=False)
agent = ShotAgentReasoner(lib)

sb = agent.build_storyboard(
    user_prompt="石墨烯充电宝产品宣传片：快充科技感、能量流动、参数展示",
    total_duration=36.2,
    template_id="inkpress_promo_36.2s",   # 模板模式；想自动编排就删掉这一行
    style_id="inkpress-dark",
)
n = len(sb.get("storyboard", [])) if isinstance(sb, dict) else 0
print(f"✓ 分镜编排完成：{n} 个镜头")

gen = RemotionCodeGenerator(lib)
out = gen.generate(sb, output_dir="remotion_output")
print("✓ Remotion 工程已生成：", os.path.abspath(out))
print()
print("下一步渲染视频：")
print("  cd remotion_output")
print("  npm install && npm run dev   # 预览（电脑已有 node v22 可直接跑）")
