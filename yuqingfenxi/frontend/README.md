# 舆情分析系统 - 前端模块

## 项目说明
基于Vue3 + Vite构建的舆情分析系统前端展示层，包含数据可视化、监控面板等功能。

## 技术栈
- Vue3: 使用Composition API构建响应式组件
- Vite: 快速构建工具
- ECharts: 数据可视化图表库
- Pinia: 状态管理

## 安装依赖
```bash
npm install
```

## 开发服务器
```bash
npm run dev
```

## 构建生产环境
```bash
npm run build
```

## 主要组件
- `App.vue`: 主页面布局
- `components/SentimentChart.vue`: 情感分析可视化
- `components/HotTopics.vue`: 热点话题展示
- `components/DataGrid.vue`: 舆情数据表格展示