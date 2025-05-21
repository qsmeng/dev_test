<template>
  <div id="app">
    <h1>舆情分析系统</h1>
    <div class="dashboard">
      <SentimentChart :data="sentimentData" />
      <HotTopics :topics="hotTopics" />
      <DataGrid :items="舆情数据" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SentimentChart from './components/SentimentChart.vue';
import HotTopics from './components/HotTopics.vue';
import DataGrid from './components/DataGrid.vue';

// 示例数据
const sentimentData = ref([]);
const hotTopics = ref([]);
const舆情数据 = ref([]);

// 获取真实数据
onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: 'This is a sample text for analysis. It contains both positive and negative elements.',
        analysis_type: 'all'
      })
    });
    
    const result = await response.json();
    
    // 更新情感数据
    sentimentData.value = [{ date: new Date().toISOString(), sentiment: result.sentiment_score }];
    
    // 更新热点话题
    hotTopics.value = result.topics.map(topic => `Topic ${topic[0]}: ${topic[1].toFixed(2)}`);
    
    // 更新舆情数据
    舆情数据.value = [{
      id: 1,
      content: 'This is a sample text for analysis. It contains both positive and negative elements.',
      sentiment: result.sentiment_score,
      topics: result.topics.map(topic => `Topic ${topic[0]}`)
    }];
  } catch (error) {
    console.error('API请求失败:', error);
  }
});
</script>

<style scoped>
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}
</style>