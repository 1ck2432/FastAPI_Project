Simple Social 全栈社交平台
一个轻量级、响应迅速的全栈社交媒体平台。本项目采用前后端分离架构，致力于提供极简、流畅的社交交互体验。

🛠️ 技术栈
后端 (Backend): FastAPI - 提供高性能、支持异步的 RESTful API 接口。

前端 (Frontend): Streamlit - 纯 Python 驱动的交互式 Web 界面，实现快速的 UI 构建与数据流转。

语言: Python 3.9+

✨ 核心功能 (待按需调整)
用户认证: 注册、登录及基于 JWT 的安全会话管理。

内容发布: 支持发布纯文本或图文动态。

社交互动: 浏览公共时间线（Timeline），支持点赞与基础评论功能。

个人主页: 展示个人信息及历史发布内容。

🚀 快速开始
1. 克隆项目
Bash
git clone https://github.com/1ck2432/FastAPI_Project.git
cd FastAPI_Project
2. 环境配置
建议使用虚拟环境（venv 或 conda）来隔离依赖：

Bash
python -m venv venv
# Windows 激活方式:
venv\Scripts\activate
# Linux/macOS 激活方式:
source venv/bin/activate

# 安装前后端依赖
pip install -r requirements.txt
3. 运行后端服务 (FastAPI)
打开一个终端窗口，启动 FastAPI 所在的 Uvicorn 服务器：

Bash
# 假设你的后端入口文件是 main.py，且应用实例名为 app
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
后端 API 文档将在 http://localhost:8000/docs 自动生成。

4. 运行前端应用 (Streamlit)
打开另一个新的终端窗口（保持后端运行状态），启动前端页面：

Bash
# 假设你的前端入口文件是 app.py
streamlit run frontend/app.py
执行后，浏览器会自动打开 http://localhost:8501 展示平台界面。

📁 项目结构参考
Plaintext
simple-social/
├── backend/               # FastAPI 后端服务
│   ├── main.py            # 后端应用入口
│   ├── routers/           # API 路由 (用户、帖子等)
│   ├── models/            # 数据模型 
│   └── utils/             # 工具函数 (认证、配置等)
├── frontend/              # Streamlit 前端应用
│   ├── app.py             # 前端主页面入口
│   ├── components/        # 可复用的 UI 组件
│   └── pages/             # 多页面路由
├── requirements.txt       # 项目依赖清单
└── README.md              # 项目说明文档