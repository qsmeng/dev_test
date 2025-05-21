<template>
  <div class="data-grid">
    <h2>舆情数据</h2>
    <table>
      <thead>
        <tr>
          <th v-for="(value, key) in items[0]" :key="key">
            {{ key }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td v-for="(value, key) in item" :key="key">
            {{ value }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  items: {
    type: Array,
    required: true,
    default: () => []
  }
});
</script>

<style scoped>
.data-grid {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 0.5rem;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
}

th {
  background-color: #e9ecef;
}
</style>