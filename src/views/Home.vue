<template>
  <div class="catalog-page">
    <div class="products-grid">
      <ProductCard 
        v-for="product in displayedProducts" 
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import ProductCard from '@/components/Product/ProductCard.vue'
import { isMobileDevice } from '@/utils/deviceDetector'

// Временные данные для верстки - потом заменим на реальные
// Для десктопа: 10 товаров для сетки 5x2
// Для мобильных: только 4 товара (2 ряда × 2 колонки)
const products = ref([
  { id: 1, name: 'Товар 1', price: 1000, image: '' },
  { id: 2, name: 'Товар 2', price: 2000, image: '' },
  { id: 3, name: 'Товар 3', price: 3000, image: '' },
  { id: 4, name: 'Товар 4', price: 4000, image: '' },
  { id: 5, name: 'Товар 5', price: 5000, image: '' },
  { id: 6, name: 'Товар 6', price: 6000, image: '' },
  { id: 7, name: 'Товар 7', price: 7000, image: '' },
  { id: 8, name: 'Товар 8', price: 8000, image: '' },
  { id: 9, name: 'Товар 9', price: 9000, image: '' },
  { id: 10, name: 'Товар 10', price: 10000, image: '' }
])

// Проверяем тип устройства (компьютер или телефон)
const isMobile = ref(typeof window !== 'undefined' ? isMobileDevice() : false)

const updateIsMobile = () => {
  if (typeof window !== 'undefined') {
    // Проверяем тип устройства, а не размер экрана
    // Это предотвращает срабатывание мобильных стилей при масштабировании на десктопе
    isMobile.value = isMobileDevice()
  }
}

onMounted(() => {
  if (typeof window !== 'undefined') {
    updateIsMobile()
    window.addEventListener('resize', updateIsMobile)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('resize', updateIsMobile)
  }
})

const displayedProducts = computed(() => {
  // На десктопе показываем все 10 товаров, на мобильных только 4
  // Проверяем класс на documentElement для точности
  const isMobileDevice = typeof window !== 'undefined' && 
    document.documentElement.classList.contains('is-mobile-device')
  return isMobileDevice ? products.value.slice(0, 4) : products.value
})
</script>

<style scoped>
.catalog-page {
  width: 100%;
  height: 100%;
  padding: 0;
  padding-top: 0;
  margin-top: 0;
  overflow-x: hidden; /* Запрещаем горизонтальную прокрутку */
  overflow-y: auto; /* Вертикальная прокрутка разрешена */
  background-color: #F6F5EC;
}

/* Для десктопа добавляем отступ сверху для страницы каталога, чтобы товары не перекрывали фильтры */
.is-desktop-device .catalog-page {
  padding-top: 0 !important;
  margin-top: 0 !important;
  position: relative !important;
}

.products-grid {
  display: grid;
  /* Фиксируем 5 колонок для десктопа (5x2 для 10 товаров) */
  grid-template-columns: repeat(5, 1fr);
  gap: clamp(16px, 1.5vw, 24px);
  width: 100%;
  max-width: 100%;
  padding: clamp(20px, 2vh, 32px) clamp(32px, 3vw, 40px);
  box-sizing: border-box;
  justify-items: start; /* Выравниваем карточки по левому краю */
  margin-top: 0; /* Убираем лишние отступы */
}

/* Адаптация для планшетов и мобильных (до 768px, но не включая маленькие мобильные) */
/* Но только для мобильных устройств */
@media (min-width: 401px) and (max-width: 767px) {
  .is-mobile-device .catalog-page {
    overflow-x: hidden; /* Запрещаем горизонтальную прокрутку */
  }

  .is-mobile-device .products-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 колонки для планшетов и больших мобильных */
    gap: clamp(12px, 2vw, 16px);
    padding: clamp(16px, 2vh, 24px) clamp(20px, 3vw, 32px);
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
}

/* Стили для десктопа (от 1280px) */
@media (min-width: 1280px) {
  .products-grid {
    grid-template-columns: repeat(5, 1fr);
    gap: clamp(16px, 1.5vw, 24px);
    padding: clamp(20px, 2vh, 32px) clamp(32px, 3vw, 40px);
    padding-top: 60px; /* Увеличенный отступ сверху, чтобы не перекрывать фильтры в хедере (хедер 208px, фильтры на 137px) */
    justify-items: start; /* Выравниваем карточки по левому краю */
  }

  .product-card {
    max-width: 236px; /* Фиксируем максимальную ширину карточки */
    width: 100%;
  }
}

/* Для десктопных устройств всегда применяем десктопные стили даже при масштабировании */
.is-desktop-device .products-grid {
  grid-template-columns: repeat(5, 1fr) !important;
  gap: clamp(16px, 1.5vw, 24px) !important;
  padding-left: clamp(32px, 3vw, 40px) !important;
  padding-right: clamp(32px, 3vw, 40px) !important;
  padding-bottom: clamp(20px, 2vh, 32px) !important;
  padding-top: 60px !important; /* Увеличенный отступ сверху, чтобы не перекрывать фильтры в хедере */
  margin-top: 0 !important;
  justify-items: start !important;
}

.is-desktop-device .product-card {
  max-width: 236px !important;
  width: 100% !important;
}


/* Адаптация для планшетов (от 768px до 1279px), но только для мобильных устройств */
@media (min-width: 768px) and (max-width: 1279px) {
  .is-mobile-device .products-grid {
    grid-template-columns: repeat(3, 1fr); /* 3 колонки для планшетов */
    gap: clamp(16px, 2vw, 24px);
    padding: clamp(20px, 2vh, 28px) clamp(24px, 3vw, 36px);
    justify-items: start; /* Выравниваем карточки по левому краю */
  }
}

/* Адаптация для мобильных (до 400px - iPhone 12 и меньше) */
@media (max-width: 400px) {
  .is-mobile-device .catalog-page {
    padding-bottom: 0;
    overflow-x: hidden;
    width: 100%;
    max-width: 100%;
  }

  .is-mobile-device .products-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 колонки с равной шириной */
    gap: 8px;
    padding: 16px;
    padding-top: 10px;
  }
}
</style>
 
