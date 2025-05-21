backend/
├── app/                   # 应用核心
│   ├── api/               # API路由
│   │   ├── v1/            # API版本
│   │   │   ├── endpoints/ # 端点模块
│   │   │   └── __init__.py
│   ├── core/              # 核心配置
│   ├── db/                # 数据库相关
│   ├── models/            # 数据模型
│   ├── schemas/           # Pydantic模型
│   ├── services/          # 业务逻辑
│   │   ├── data_collection/   # 数据采集服务
│   │   ├── data_processing/   # 数据处理管道
│   │   ├── model_service/     # 模型推理服务
│   │   └── storage/           # 数据存储管理
│   └── __init__.py
├── tests/                 # 测试代码
├── .env                   # 环境变量
├── .gitignore             # Git忽略规则
├── main.py                # 应用入口
├── requirements.txt       # 依赖管理
└── README.md              # 项目说明
```

## API 端点设计
- `POST /api/v1/collect`      # 数据采集接口
- `POST /api/v1/process`     # 数据处理接口
- `POST /api/v1/analyze`      # 模型分析接口
- `GET /api/v1/results`      # 结果查询接口