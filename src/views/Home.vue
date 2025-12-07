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

const isMobile = ref(typeof window !== 'undefined' ? window.innerWidth <= 390 : false)

const updateIsMobile = () => {
  if (typeof window !== 'undefined') {
    isMobile.value = window.innerWidth <= 390
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
  return isMobile.value ? products.value.slice(0, 4) : products.value
})
</script>

<style scoped>
.catalog-page {
  width: 100%;
  height: 100%;
  padding: 0;
  overflow: auto;
  background-color: #F6F5EC;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(5, 236px);
  gap: 16px;
  justify-content: center;
  width: 100%;
  padding: 20px 32px;
  box-sizing: border-box;
}

/* Адаптация для мобильных */
@media (max-width: 390px) {
  .catalog-page {
    padding-bottom: 0;
    overflow-x: hidden;
    width: 100%;
    max-width: 100%;
  }

  .products-grid {
    display: grid;
    grid-template-columns: repeat(2, 175px);
    gap: 8px;
    justify-content: center;
    padding: 16px;
    padding-top: 10px;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
    overflow-x: hidden;
  }
}
</style>
 
