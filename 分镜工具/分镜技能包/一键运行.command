

#!/bin/zsh
# 双击这个文件 = 自动生成分镜 Remotion 工程（会打开终端窗口执行）
cd "$(dirname "$0")"
echo "▸ 正在编排分镜并生成 Remotion 工程..."
python3 示例_生成分镜.py
echo ""
echo "▸ 全部完成。想渲染视频：cd remotion_output && npm install && npm run dev"
echo ""
echo "按任意键关闭窗口..."
read -k 1



