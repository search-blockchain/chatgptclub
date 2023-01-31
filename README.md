# 环境
Python 3.7.2+ support

# 依赖
## 定时任务管理
pip install apscheduler
## google 热门
pip install -U google_trends
## ChatGpt
pip install openai
## 界面交互
pip install PyQt5
pip install PyQt5-tools

# 结构
## 守护进程
### 执行命令
python  src/daemon.py
### 功能描述
通过一个定时器，执行4个任务
#### jobKeyWords任务
通过将google热搜词从google 公开的热门网站上获取到，并且存入数据库，现在暂定是sqlite，后期为了同步可以改
#### jobChatGpt任务
将获取到关键字或者实时热门信息，整理成问题，提交给到chatgpt来回答，将问题和回答成对存入数据库
#### jobRealtimeTrends任务
通过从google的公开网站获取实时搜索热点，整理并存入数据库
#### jobPushClub任务
将ChatGpt的回答内容，格式化推送给到club，这个等club上线，标准出来之后对接
#### 完成列表
1， 获取google热搜词，实时热点
2， 格式化问题，向chatgpt提问
3， 基础数据存储

#### 未完成列表
1， club 创建和内容推送，等club技术选型确定
2， 问题模板化，扩展现有关键字的提问形式，提高chatgpt的质量
3,  实时热点数据，内容提取和结构分析

## 客户端
### 执行命令
python  src/client.py
### 功能描述
用于对chatgpt的内容进行人工审核
### 完成列表
1，主界面
### 未完成列表
1，关键词审核
2，实时热点审核