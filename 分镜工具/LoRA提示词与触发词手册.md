# LoRA Studio — 提示词与触发词训练手册

> 适用于 SD1.5 / SDXL / FLUX.1 / Wan 2.x / CogVideoX / LTX-Video 全部支持模型。  
> 本手册含：触发词规范 · 各模型正/负提示词 · 风格/质量/光照标签 · 训练参数建议 · 通用技巧。

---

## 一、触发词（Trigger Word）规范

触发词是 LoRA 训练与推理时保持一致性的关键标记词。**训练时写在 caption 中，推理时写进提示词**，必须完全一致。

| 规则        | 说明                            |
| --------- | ----------------------------- |
| **短**     | 1~3 个词即可，如 `mycat8`，越短越不易干扰   |
| **唯一**    | 不与通用词（cat、girl、style）冲突       |
| **小写下划线** | 全小写，词间用下划线：`elf_red_hair_v1`  |
| **专用前缀**  | 建议加个人/主题前缀：`ls_`、`brs_`、`oc_` |
| **固定不变**  | 训练与推理必须用同一个字符串                |

**推荐触发词示例：** `ls_whitecat`、`oc_brown_dragon`、`brs_cyberpunk_armor_v1`

> 💡 **技巧**：让触发词在 caption 中周期性出现（每 3~5 个词出现一次），比句首只出现一次更能稳定学到该特征。

---

## 二、SD 1.5（512px，图像）

**触发词**：`ls_xxx`（短、唯一）

**正提示词**

```
photorealistic, ultra detailed, 8k, masterpiece
high quality, sharp focus, intricate details
natural lighting, soft studio light, cinematic
best quality, extremely detailed, professional
```

**负提示词**

```
worst quality, low quality, blurry, pixelated
bad anatomy, bad hands, extra fingers, deformed
watermark, text, logo, signature, jpeg artifacts
lowres, normal quality, jpeg, worst quality
```

**风格标签**：anime / realistic / 3d render / watercolor / oil painting / cyberpunk / sci-fi / fantasy / portrait / landscape

**质量词**：masterpiece · best quality · ultra detailed · highres · 8k · 4k · sharp focus · professional · award winning

**光照词**：soft lighting · studio light · golden hour · rim light · volumetric lighting · cinematic lighting · neon lighting

**训练参数建议**：guidance 7.0 · steps 1500 · clip_skip 1 · dim 32 · lr 1e-4~5e-5 · AdamW8bit

---

## 三、SDXL（1024px，图像）

**正提示词**

```
masterpiece, best quality, high quality, ultra detailed
8k, breathtaking, sharp focus, professional, award winning
soft cinematic lighting, detailed face, intricate details
highly detailed, extremely detailed, beautiful composition
```

**负提示词**

```
worst quality, low quality, normal quality, lowres
bad anatomy, bad hands, deformed, extra limbs, fused fingers
watermark, text, logo, jpeg artifacts, blurry, oversaturated
cinema style, film grain, low contrast, dull colors
```

**风格**：realistic / anime / photoreal / digital art / concept art / 3d model / unreal engine / fantasy / sci-fi / nouveau

**质量词**：masterpiece · best quality · ultra detailed · detailed · sharp focus · 8k · high resolution · intricate details · professional

**光照词**：cinematic lighting · soft diffused lighting · golden hour · volumetric light · dramatic lighting

**训练参数建议**：guidance 6.0 · steps 2000 · clip_skip 2 · dim 16 · lr 2e-5~1e-4 · AdamW8bit

---

## 四、FLUX.1（1024px，图像）

> FLUX 对提示词更敏感，推荐「触发词 + 主体词 + 风格词」三段式。

**正提示词**

```
photorealistic, hyper detailed, 8k, highly detailed
masterpiece, cinematic, professional lighting
clean composition, sharp focus, natural colors, high contrast
high quality, ultra high fidelity, intricate texture details
```

**负提示词**

```
worst quality, low quality, blurry, distorted
deformed, bad anatomy, bad hands, extra fingers
text, watermark, logo, jpeg, artifacts, oversharpen
dark, low contrast, muted, desaturated
```

**风格**：photoreal / anime / cinematic / concept art / matte painting / isometric / low poly / pixel art / vintage / minimal

**训练参数建议**：guidance 3.5 · steps 1500 · dim 16 · lr 1e-4~4e-4 · AdamW8bit

---

## 五、Wan 2.1 / 2.2（720px，视频）

> 视频模型：把**动作动词与镜头语言**写进正提示词，比堆质量词更关键。

**正提示词**

```
masterpiece, best quality, highres, cinematic
fluid motion, natural movement, smooth animation
detailed character, expressive face, consistent style
dynamic camera, depth of field, professional vfx
```

**负提示词**

```
low quality, worst quality, blurry, flickering
distorted, warped, deformed, bad anatomy
watermark, text, logo, jpeg artifacts
static, slow motion, jittery, motion blur, duplicate frames
```

**动作/镜头建议**：walking · running · waving · dancing · camera pan · close-up · zoom in/out · tracking shot · slow motion

**训练参数建议**：guidance 5.0 · steps 2000 · dim 32 · lr 2e-5~1e-4 · 49 帧 720p

---

## 六、CogVideoX 2B（480px，视频）

**正提示词**

```
masterpiece, best quality, high quality
smooth motion, natural movement, expressive
detailed subject, consistent character, cinematic
dynamic scene, subtle animation, professional
```

**负提示词**

```
low quality, worst quality, blurry, jitter
deformed, distortion, glitch, morphing
watermark, text, logo, jpeg, artifacts
still image, frozen, choppy, low frame rate
```

**动作建议**：waves · dances · fights · turns · blinks · subtle head movement · camera push-in

**训练参数建议**：guidance 5.5 · steps 1500 · dim 32 · lr 1e-4~1e-3 · 49 帧 480p

---

## 七、LTX-Video 2B（480px，视频）

> 偏重简洁主体 + 清晰运动，不建议过度堆砌质量词。

**正提示词**

```
masterpiece, best quality, clear subject
smooth motion, natural physics, fluid animation
sharp focus, detailed subject, bright lighting
cinematic, subtle camera movement, consistent style
```

**负提示词**

```
blurry, low quality, distorted, warped subject
ghosting, glitch, deformation, jittery motion
text, watermark, logo, artifacts
static, stiff, robotic motion, slow, low fps
```

**风格**：anime / realistic / stylized / toon / fantasy / vfx / particle / abstract motion

**训练参数建议**：guidance 4.0 · steps 1500 · dim 32 · lr 5e-5~5e-4 · 49 帧 480p

---

## 八、通用训练技巧

1. **提示词三段式**：质量词 + 主体/风格词 + 光照环境词。
2. **负提示词**用来排除手部、水印、模糊、低质等常见瑕疵。
3. **训练集规模**：20~200 张图。目标越单一图可越少（提高复现），风格越杂图越多（提高一致性）。
4. **触发词频率**：caption 中定期出现效果最稳。
5. **推理 LoRA 强度**：0.6~0.9 通常最佳，过高易过拟合。
6. **视频模型**：动作动词 + 镜头语言 >> 堆质量词。
7. **Data 一致性**：训练集图片分辨率尽量接近模型建议分辨率（见各模型章节）。

---

## 九、一键使用 AI 优化

应用内 **AI 助手** 页可填写 DeepSeek / OpenAI / 豆包等 LLM API Key：

- 输入目标模型 + 训练主题 → 自动生成触发词 + 正负提示词
- 粘贴已有提示词 → AI 增强改写
- 内置连通测试，验证 Key 是否可用

---

*本手册由 LoRA Studio 生成 · 提示词与触发词资料库也有对应可视化页面，可在应用侧边栏「📖 提示词库」查看。*
