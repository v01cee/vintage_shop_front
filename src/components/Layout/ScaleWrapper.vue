<template>
  <div ref="containerRef" class="scale-container" @scroll="handleScroll">
    <div ref="appRef" class="scale-wrapper" :style="scaleStyle">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'

const appRef = ref(null)
const containerRef = ref(null)
const scale = ref(1)
const maxScrollTop = ref(0)

const scaleStyle = computed(() => ({
  transform: `scale(${scale.value}) translateZ(0)`,
  transformOrigin: 'top center',
  transition: 'none'
}))

let resizeTimeout = null
let zoomInterval = null

const updateScale = () => {
  if (!appRef.value) return
  
  const windowWidth = window.innerWidth
  const windowHeight = window.innerHeight
  const appWidth = 1300
  const appHeight = 1544
  
  // Вычисляем масштаб для заполнения всего экрана
  const scaleWidth = windowWidth / appWidth
  const scaleHeight = windowHeight / appHeight
  
  // Всегда используем масштаб по ширине для заполнения всей ширины (без белых полос)
  // Немного увеличиваем для полного заполнения
  let newScale = scaleWidth * 1.01
  
  // Округляем до 4 знаков для более точного масштабирования и лучшего качества
  scale.value = Math.round(newScale * 10000) / 10000
  
  // Вычисляем максимальную позицию прокрутки
  // Масштабированная высота минус высота окна
  const scaledHeight = appHeight * scale.value
  if (scaledHeight > windowHeight) {
    maxScrollTop.value = scaledHeight - windowHeight
  } else {
    maxScrollTop.value = 0
  }
}

const handleScroll = () => {
  if (!containerRef.value) return
  
  // Ограничиваем прокрутку, чтобы нельзя было прокрутить за футер
  if (containerRef.value.scrollTop > maxScrollTop.value) {
    containerRef.value.scrollTop = maxScrollTop.value
  }
}

const handleResize = () => {
  // Debounce для более плавной работы
  if (resizeTimeout) {
    clearTimeout(resizeTimeout)
  }
  resizeTimeout = setTimeout(() => {
    updateScale()
  }, 50)
}

onMounted(() => {
  updateScale()
  window.addEventListener('resize', handleResize)
  window.addEventListener('orientationchange', updateScale)
  
  // Отслеживаем изменение масштаба браузера через devicePixelRatio
  let lastPixelRatio = window.devicePixelRatio
  const checkZoom = () => {
    if (window.devicePixelRatio !== lastPixelRatio) {
      lastPixelRatio = window.devicePixelRatio
      updateScale()
    }
  }
  
  // Проверяем zoom каждые 100ms
  zoomInterval = setInterval(checkZoom, 100)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('orientationchange', updateScale)
  if (resizeTimeout) {
    clearTimeout(resizeTimeout)
  }
  if (zoomInterval) {
    clearInterval(zoomInterval)
  }
})
</script>

<style scoped>
.scale-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  overflow-y: auto;
  overflow-x: hidden;
}

.scale-wrapper {
  display: inline-block;
  will-change: transform;
  backface-visibility: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transform-style: preserve-3d;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  -webkit-perspective: 1000;
  perspective: 1000;
  isolation: isolate;
}

.scale-wrapper :deep(img[src$=".svg"]),
.scale-wrapper :deep(svg) {
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  shape-rendering: crispEdges;
  text-rendering: optimizeLegibility;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.scale-wrapper :deep(img:not([src$=".svg"])) {
  image-rendering: -webkit-optimize-contrast;
  image-rendering: auto;
  -ms-interpolation-mode: bicubic;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.scale-wrapper :deep(svg) {
  vector-effect: non-scaling-stroke;
  shape-rendering: crispEdges;
}
</style>

