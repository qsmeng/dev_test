## 1.后端

```
graph TD
    A[前端展示层] -->|API调用| B[后端服务层]
    B -->|模型调用| C[AI模型层]
    B -->|数据存储| D[(数据库)]
    C -->|训练数据| E[(数据仓库)]
```

## 2. 前端界面原型

```mermaid
wireframe
    page "舆情分析系统" {
        header "舆情分析系统"
        section "情感分析" {
            line "日期选择器"
            line "情感趋势折线图"
        }
        section "热点话题" {
            item "话题列表"
            item "话题详情"
        }
        section "数据监控" {
            table "舆情数据表格"
            button "刷新"
        }
    }
```

## 3. 数据流程图

```mermaid
graph LR
    F[外部数据源] --> G[数据采集接口]
    G --> H[数据清洗]
    H --> I[模型分析]
    I --> J[结果存储]
    J --> K[前端展示]