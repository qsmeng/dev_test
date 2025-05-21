ai_models/
├── core_models/           # 核心模型实现
│   ├── sentiment_analysis/  # 文本情感分析模型
│   │   ├── model.py       # 模型实现
│   │   ├── train.py       # 训练脚本
│   │   └── config.json    # 模型配置
│   ├── topic_clustering/  # 主题聚类模型
│   ├── hot_spot/          # 热点检测算法  
│   └── early_warning/     # 舆情预警模型
├── data/                  # 数据处理
│   ├── preprocess.py      # 数据预处理
│   ├── dataset.py         # 数据集管理
│   └── utils.py           # 数据工具
├── evaluation/            # 模型评估
│   ├── metrics.py         # 评估指标
│   └── reports/           # 评估报告
├── deployment/            # 模型部署
│   ├── api.py             # 推理API
│   └── service.py         # 服务封装
├── requirements.txt       # Python依赖
└── README.md              # 项目说明
```

## 核心模型技术选型
| 模型 | 技术方案 |
|------|----------|
| 文本情感分析 | BERT + 微调 |
| 主题聚类 | LDA / Top2Vec |
| 热点检测 | 时间序列分析 + 异常检测 |
| 舆情预警 | 规则引擎 + 随机森林 |