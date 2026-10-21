"""
技能2：ShotAgentReasoner 分镜推理层
接收用户需求，调用技能1配方库（library.py），输出标准化分镜 JSON。
供技能3（remotion_generator.py）消费。
"""
import json
from typing import List, Dict, Optional, Any

from library import ShotRecipeLibrary


class ShotAgentReasoner:
    """接收需求，调用配方库，输出标准化分镜JSON"""

    def __init__(self, recipe_lib: ShotRecipeLibrary):
        self.lib = recipe_lib

    def build_storyboard(self, user_prompt: str, total_duration: float,
                         asset_list: Optional[List[str]] = None,
                         beat_points: Optional[List[float]] = None,
                         template_id: Optional[str] = None,
                         style_id: Optional[str] = None) -> Dict[str, Any]:
        asset_list = asset_list or []
        beat_points = beat_points or []
        storyboard = []
        template_data = None

        if template_id:
            template_data = self.lib.getTemplate(template_id)

        if template_data:
            # 使用模板骨架
            for shot_info in template_data["shotSequence"]:
                shot_id = shot_info["shotId"]
                shot_def = self.lib.getShotById(shot_id)
                if not shot_def:
                    continue
                storyboard.append({
                    "shotId": shot_id,
                    "duration": shot_info["duration"],
                    "asset": asset_list.pop(0) if asset_list else None,
                    "textContent": user_prompt,
                    "customParams": shot_def["defaultParams"],
                    "startTime": 0
                })
        else:
            # 自动编排分镜
            available_shots = self.lib.searchShots(materialType="image")
            remain_time = total_duration
            current_time = 0
            asset_idx = 0

            while remain_time > 0.3 and len(available_shots) > 0:
                shot = available_shots[len(storyboard) % len(available_shots)]
                min_d, max_d = shot["durationRange"]
                use_dur = min(max_d, remain_time)
                if use_dur < min_d:
                    break

                storyboard.append({
                    "shotId": shot["shotId"],
                    "duration": round(use_dur, 2),
                    "asset": asset_list[asset_idx] if asset_idx < len(asset_list) else None,
                    "textContent": "",
                    "customParams": shot["defaultParams"],
                    "startTime": round(current_time, 2)
                })
                current_time += use_dur
                remain_time -= use_dur
                asset_idx += 1

        # 节拍对齐
        if beat_points and len(beat_points) > 0:
            for idx, beat_ts in enumerate(beat_points):
                if idx < len(storyboard):
                    storyboard[idx]["startTime"] = beat_ts

        output = {
            "meta": {
                "totalDuration": total_duration,
                "templateId": template_id,
                "styleId": style_id,
                "userPrompt": user_prompt
            },
            "storyboard": storyboard,
            "audio": {
                "beatPoints": beat_points
            }
        }
        return output


if __name__ == "__main__":
    lib = ShotRecipeLibrary(auto_populate=False)
    agent = ShotAgentReasoner(lib)

    # 测试：模板模式
    result = agent.build_storyboard(
        user_prompt="产品演示短片",
        total_duration=36.2,
        asset_list=["./assets/screenshot1.png", "./assets/screenshot2.png"],
        template_id="inkpress_promo_36.2s"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 测试：自动编排模式
    result2 = agent.build_storyboard(
        user_prompt="数据增长展示",
        total_duration=8.0,
        asset_list=["./assets/hero.png"]
    )
    print("\n=== 自动编排（8s）===")
    print(json.dumps(result2, indent=2, ensure_ascii=False))
