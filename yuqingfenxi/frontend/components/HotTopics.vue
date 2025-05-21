<template>
  <div class="hot-topics">
    <h2>热点话题</h2>
    <ul>
      <li v-for="(topic, index) in topics" :key="index">
        {{ topic }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  topics: {
    type: Array,
    required: true,
    default: () => []
  }
});
</script>

<style scoped>
.hot-topics {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

li {
  margin: 0.5rem 0;
  padding: 0.5rem;
  background-color: #e9ecef;
  border-radius: 4px;
}
</style>