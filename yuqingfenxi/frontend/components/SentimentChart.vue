<template>
  <div class="chart-container">
    <canvas :id="chartId" width="400" height="200"></canvas>
  </div>
</template>

<script setup>
import { onMounted, defineProps } from 'vue';
import Chart from 'chart.js/auto';

const props = defineProps({
  data: {
    type: Array,
    required: true,
    default: () => []
  }
});

const chartId = `sentiment-chart-${Math.random().toString(36).substr(2, 9)}`;

onMounted(() => {
  const ctx = document.getElementById(chartId).getContext('2d');
  
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: props.data.map(item => item.date),
      datasets: [{
        label: '情感值',
        data: props.data.map(item => item.sentiment),
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: false,
          max: 1,
          min: -1
        }
      }
    }
  });
});
</script>

<style scoped>
.chart-container {
  position: relative;
  height: 200px;
  width: 100%;
}
</style>