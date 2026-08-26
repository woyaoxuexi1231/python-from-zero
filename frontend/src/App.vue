<!-- 薄壳：布局 + 路由出口。全局 CSS 移入 styles/tokens.css + styles/base.css -->
<script setup>
import AppLayout from './layouts/AppLayout.vue'
</script>

<template>
  <AppLayout>
    <router-view/>
  </AppLayout>
</template>
