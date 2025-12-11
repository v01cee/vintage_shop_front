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
import { onMounted } from 'vue'
import { initDeviceClass } from '@/utils/deviceDetector'

// Определяем тип устройства и добавляем класс для CSS
onMounted(() => {
  initDeviceClass()
})
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
  .is-mobile-device #app {
    width: 100%;
    max-width: 1300px;
  }
}

/* Отступ для нижней навигационной панели на мобильных и планшетах */
/* Но не применяем на десктопных устройствах даже при масштабировании */
@media (max-width: 1279px) {
  .is-mobile-device #app {
    width: 100%;
    max-width: 100%;
  }

  .is-mobile-device .main-content {
    padding-bottom: 64px; /* Отступ для навигационной панели */
  }
}

/* Для десктопных устройств сохраняем фиксированную ширину даже при масштабировании */
.is-desktop-device #app {
  width: 1300px;
  max-width: 1300px;
}

.is-desktop-device .main-content {
  padding-bottom: 0;
  transition: margin-top 0.3s ease; /* Плавная анимация при открытии меню */
}

/* Когда меню открыто, сдвигаем весь контент вниз плавно */
.is-desktop-device body.menu-open .main-content {
  margin-top: 42px !important; /* Высота меню (250px - 208px = 42px) */
}
</style>

