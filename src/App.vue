<template>
  <div class="app-root">
    <div id="app">
      <AppHeader />
      <main class="main-content">
        <router-view />
      </main>
      <AppFooter />
    </div>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import AppFooter from '@/components/Layout/AppFooter.vue'
import AppHeader from '@/components/Layout/AppHeader.vue'
</script>

<style>
.app-root {
  width: 100%;
  min-height: 100vh;
  background-color: #F6F5EC;
  display: flex;
  justify-content: center;
}

#app {
  display: flex;
  flex-direction: column;
  width: 1300px;
  min-height: 100vh;
  margin: 0 auto;
  background-color: #F6F5EC;
  position: relative;
  overflow-x: visible;
}

.main-content {
  flex: 1;
}

@media (max-width: 1320px) {
  #app {
    width: 100%;
    max-width: 1300px;
  }
}

@media (max-width: 390px) {
  #app {
    width: 100%;
    max-width: 390px;
  }

  .main-content {
    padding-bottom: 64px; /* Отступ для навигационной панели */
  }
}
</style>

