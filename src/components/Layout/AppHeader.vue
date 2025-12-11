<template>
  <header class="app-header" :class="{ 'menu-open': isMenuOpen, 'cart-page': route.name === 'Cart', 'orders-page': route.name === 'Orders', 'product-page': route.name === 'Product' }">
    <div class="header-container">
      <div class="logo-wrapper" @click="goToHome">
        <img 
          :src="logoImage" 
          alt="Logo" 
          class="logo-image"
        />
      </div>
      <button class="menu-button" type="button" aria-label="Меню" @click="toggleMenu">
        <img 
          :src="currentMenuIcon" 
          alt="Меню" 
          class="menu-icon"
        />
      </button>
      <button 
        v-if="searchQuery && route.name !== 'Orders'"
        type="button"
        class="search-clear-button"
        @click="clearSearch"
        aria-label="Очистить поиск"
      >
        <span class="search-clear-x">×</span>
      </button>
      <div v-if="route.name !== 'Orders'" class="search-wrapper">
        <input 
          type="text"
          v-model="searchQuery"
          class="search-input"
          placeholder="Найти"
          @keyup.enter="handleSearch"
        />
        <button 
          type="button"
          class="search-button"
          @click="handleSearch"
          aria-label="Найти"
        >
          <img 
            :src="searchIcon" 
            alt="Поиск" 
            class="search-icon-img"
          />
        </button>
      </div>
      <button class="login-button" type="button" aria-label="Профиль" @click="goToLogin">
        <img 
          :src="loginIcon" 
          alt="Профиль" 
          class="login-icon"
        />
        <span class="login-text">Профиль</span>
      </button>
      <button class="orders-button" type="button" aria-label="Заказы" @click="goToOrders">
        <img 
          :src="currentOrdersIcon" 
          alt="Заказы" 
          class="orders-icon"
        />
        <span class="orders-text">Заказы</span>
      </button>
      <button class="cart-button" type="button" aria-label="Корзина" @click="goToCart">
        <img 
          :src="currentCartIcon" 
          alt="Корзина" 
          class="cart-icon"
        />
        <span class="cart-text">Корзина</span>
        <span v-if="cartStore.totalItems > 0" class="cart-badge">
          {{ cartStore.totalItems }}
        </span>
      </button>
      <div class="info-banner">
        <span class="info-banner-text">Покупай по ценам от поставщика. В три раза выгоднее чем в бутиках</span>
        <div class="info-banner-contacts">
          <span class="info-banner-phone">+7 (495) 374-78-74</span>
          <button class="info-banner-icon" type="button" aria-label="Telegram">
            <img :src="telegramIcon" alt="Telegram" class="info-banner-icon-img" />
          </button>
          <button class="info-banner-icon" type="button" aria-label="WhatsApp">
            <img :src="whatsappIcon" alt="WhatsApp" class="info-banner-icon-img" />
          </button>
        </div>
      </div>
      <button class="filter-button" type="button" aria-label="Фильтры" @click="toggleFilterModal">
        <img 
          :src="filterIcon" 
          alt="Фильтры" 
          class="filter-icon"
        />
      </button>
      <div v-if="!isMenuOpen" class="categories-wrapper">
        <span class="category-item">Винтажная папфюмерия и косметика</span>
        <span class="category-item">Аксессуары</span>
        <span class="category-item">Одежда</span>
        <span class="category-item">Для коллекции</span>
        <span class="category-item">Мужское</span>
        <span class="category-item">Женское</span>
        <span class="category-item">Унисекс</span>
      </div>
      <div v-if="isFilterModalOpen" class="filter-modal-overlay" @click="closeFilterModal">
        <div class="filter-modal" @click.stop>
          <div class="filter-options">
            <label 
              v-for="option in filterOptions" 
              :key="option.value"
              class="filter-option"
              :class="{ 'filter-option-selected': selectedFilter === option.value }"
            >
              <input 
                type="radio" 
                :value="option.value"
                v-model="selectedFilter"
                class="filter-radio"
              />
              <span class="filter-radio-custom"></span>
              <span class="filter-option-text">{{ option.label }}</span>
            </label>
          </div>
        </div>
      </div>
      <!-- Десктопное меню -->
      <div v-if="isMenuOpen" class="menu-navigation">
        <div class="nav-column">
          <router-link to="/" class="nav-link" @click="closeMenuOnNavigate">Каталог</router-link>
          <router-link to="/reviews" class="nav-link" @click="closeMenuOnNavigate">Отзывы</router-link>
        </div>
        <div class="nav-divider"></div>
        <div class="nav-column">
          <router-link to="/orders" class="nav-link" @click="closeMenuOnNavigate">Ваши заказы</router-link>
          <router-link to="/login" class="nav-link" @click="closeMenuOnNavigate">Ваш профиль</router-link>
        </div>
        <div class="nav-divider"></div>
        <div class="nav-column">
          <a href="#" class="nav-link" @click.prevent="handleContacts">Контакты</a>
          <router-link to="/about-owner" class="nav-link" @click="closeMenuOnNavigate">О сайте</router-link>
        </div>
        <div class="nav-divider"></div>
        <div class="nav-column">
          <router-link to="/terms" class="nav-link" @click="closeMenuOnNavigate">Условия</router-link>
          <a href="#" class="nav-link" @click.prevent="handleOffer">Офферта</a>
        </div>
      </div>
      
      <!-- Мобильное меню -->
      <div v-if="isMenuOpen" class="mobile-menu-overlay" @click="toggleMenu">
        <div class="mobile-menu" @click.stop>
          <button class="mobile-menu-close" @click="toggleMenu" aria-label="Закрыть меню">
            <span class="mobile-menu-close-icon">×</span>
          </button>
          <nav class="mobile-menu-nav">
            <router-link to="/" class="mobile-menu-item" @click="toggleMenu">Каталог</router-link>
            <router-link to="/reviews" class="mobile-menu-item" :class="{ active: route.name === 'Reviews' }" @click="toggleMenu">Отзывы</router-link>
            <router-link to="/cart" class="mobile-menu-item" :class="{ active: route.name === 'Cart' }" @click="toggleMenu">Корзина</router-link>
            <router-link to="/orders" class="mobile-menu-item" @click="toggleMenu">Ваши заказы</router-link>
            <router-link to="/login" class="mobile-menu-item" @click="toggleMenu">Ваш профиль</router-link>
            <a href="#" class="mobile-menu-item" @click="toggleMenu">Контакты</a>
            <router-link to="/about-owner" class="mobile-menu-item" @click="toggleMenu">О сайте</router-link>
            <router-link to="/terms" class="mobile-menu-item" @click="toggleMenu">Условия</router-link>
            <a href="#" class="mobile-menu-item" @click="toggleMenu">Офферта</a>
          </nav>
        </div>
      </div>
      
      <!-- Рекламный баннер для мобильных -->
      <div v-if="route.name !== 'Cart' && route.name !== 'Orders' && route.name !== 'Product'" class="mobile-ad-banner">
        <img :src="adBanner" alt="Реклама" class="ad-banner-image" />
      </div>
      
      <!-- Поисковая строка для мобильных -->
      <div v-if="route.name !== 'Cart' && route.name !== 'Orders'" class="mobile-search-wrapper">
        <input 
          type="text"
          v-model="searchQuery"
          class="mobile-search-input"
          placeholder="Найти"
          @keyup.enter="handleSearch"
        />
        <button 
          type="button"
          class="mobile-search-button"
          @click="handleSearch"
          aria-label="Найти"
        >
          <img 
            :src="searchIcon" 
            alt="Поиск" 
            class="mobile-search-icon"
          />
        </button>
      </div>
      
      <!-- Категории для мобильных -->
      <div v-if="route.name !== 'Cart' && route.name !== 'Orders'" class="mobile-category">
        <button 
          type="button"
          class="mobile-category-icon" 
          @click="toggleFilterModal"
          aria-label="Фильтры"
        >
          <img :src="filterIcon" alt="Фильтры" class="category-icon-img" />
        </button>
        <div class="mobile-categories-scroll">
          <span class="mobile-category-item">Винтажная папфюмерия и косметика</span>
          <span class="mobile-category-item">Аксессуары</span>
          <span class="mobile-category-item">Одежда</span>
          <span class="mobile-category-item">Для коллекции</span>
          <span class="mobile-category-item">Мужское</span>
          <span class="mobile-category-item">Женское</span>
          <span class="mobile-category-item">Унисекс</span>
        </div>
      </div>
    </div>
  </header>
    
  <!-- Нижняя навигационная панель для мобильных -->
  <nav class="mobile-bottom-nav">
      <button 
        class="bottom-nav-item" 
        :class="{ active: route.name === 'Home' }"
        @click="goToHome"
      >
        <img 
          :src="homeIcon" 
          alt="Главная" 
          class="bottom-nav-icon"
        />
        <span class="bottom-nav-text">Главная</span>
      </button>
      <button 
        class="bottom-nav-item" 
        :class="{ active: route.name === 'Orders' }"
        @click="goToOrders"
      >
        <img 
          :src="route.name === 'Orders' ? ordersActiveIcon : ordersIcon" 
          alt="Заказы" 
          class="bottom-nav-icon"
        />
        <span class="bottom-nav-text">Заказы</span>
      </button>
      <button 
        class="bottom-nav-item bottom-nav-menu" 
        :class="{ active: isMenuOpen }"
        @click="toggleMenu"
      >
        <img 
          :src="menuIconMobile" 
          alt="Меню" 
          class="bottom-nav-icon"
        />
        <span class="bottom-nav-text">Меню</span>
      </button>
      <button 
        class="bottom-nav-item" 
        :class="{ active: route.name === 'Cart' }"
        @click="goToCart"
      >
        <img 
          :src="route.name === 'Cart' ? cartActiveIcon : cartIcon" 
          alt="Корзина" 
          class="bottom-nav-icon"
        />
        <span class="bottom-nav-text">Корзина</span>
      </button>
      <button 
        class="bottom-nav-item" 
        :class="{ active: route.name === 'Login' }"
        @click="goToLogin"
      >
        <img 
          :src="route.name === 'Login' ? loginActiveIcon : loginIcon" 
          alt="Войти" 
          class="bottom-nav-icon"
        />
        <span class="bottom-nav-text">Войти</span>
      </button>
    </nav>

    <!-- Модальное окно входа/регистрации -->
    <!-- TODO: Переместить в другое место по указанию пользователя -->
    <!-- <LoginModal 
      :is-open="isLoginModalOpen" 
      @close="closeLoginModal"
      @login="handleLogin"
      @register="handleRegister"
    /> -->
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useProductsStore } from '@/stores/products'
import { useCartStore } from '@/stores/cart'
// import LoginModal from '@/components/Auth/LoginModal.vue'
import logoImage from '../../../лого главный экран.svg'
import menuIcon from '../../../меню.svg'
import menuOpenIcon from '../../../открытое меню.svg'
import filterIcon from '../../../иконка фильтров.svg'
import searchIcon from '../../../иконка лупы.svg'
import loginIcon from '../../../значок аккаунта.svg'
import ordersIcon from '../../../значок заказов.svg'
import ordersActiveIcon from '../../../активная кнопка заказы.svg'
import cartIcon from '../../../значок корзины.svg'
import cartActiveIcon from '../../../активная иконка корзины.svg'
import telegramIcon from '../../../значок ТГ.svg'
import whatsappIcon from '../../../значок Whatshap.svg'
import homeIcon from '../../../иконка главное меню.svg'
import menuIconMobile from '../../../иконка меню.svg'
import loginActiveIcon from '../../../активная иконка профиля.svg'
import adBanner from '../../../реклама.svg'

const router = useRouter()
const route = useRoute()
const productsStore = useProductsStore()
const cartStore = useCartStore()

const searchQuery = ref('')
const isFilterModalOpen = ref(false)
const isMenuOpen = ref(false)
// const isLoginModalOpen = ref(false) // TODO: Использовать в другом месте
const selectedFilter = computed({
  get: () => productsStore.selectedFilter,
  set: (value) => {
    productsStore.setFilter(value)
    // Закрываем модальное окно после выбора фильтра
    closeFilterModal()
  }
})

const currentMenuIcon = computed(() => {
  return isMenuOpen.value ? menuOpenIcon : menuIcon
})

const currentCartIcon = computed(() => {
  return route.name === 'Cart' ? cartActiveIcon : cartIcon
})

const currentOrdersIcon = computed(() => {
  return route.name === 'Orders' ? ordersActiveIcon : ordersIcon
})

const filterOptions = [
  { value: 'default', label: 'По умолчанию' },
  { value: 'new', label: 'Новинки' },
  { value: 'price-asc', label: 'По возрастанию цены' },
  { value: 'price-desc', label: 'По убыванию цены' },
  { value: 'views-more', label: 'Больше просмотров' },
  { value: 'views-less', label: 'Меньше просмотров' }
]


const toggleFilterModal = () => {
  isFilterModalOpen.value = !isFilterModalOpen.value
}

const closeFilterModal = () => {
  isFilterModalOpen.value = false
}

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    productsStore.searchProducts(searchQuery.value)
  } else {
    productsStore.searchProducts('')
  }
}

const clearSearch = () => {
  searchQuery.value = ''
  productsStore.searchProducts('')
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
  // Закрываем модальное окно фильтров при открытии меню
  if (isMenuOpen.value) {
    isFilterModalOpen.value = false
  }
}

const goToCart = () => {
  router.push('/cart')
  isMenuOpen.value = false
}

const goToOrders = () => {
  router.push('/orders')
}

const goToHome = () => {
  router.push('/')
  isMenuOpen.value = false
}

const goToLogin = () => {
  router.push('/login')
  isMenuOpen.value = false
}

// TODO: Переместить логику модального окна в другое место по указанию пользователя
// const closeLoginModal = () => {
//   isLoginModalOpen.value = false
// }

// const handleLogin = (credentials) => {
//   console.log('Login attempt:', credentials)
//   // TODO: Реализовать логику входа
//   closeLoginModal()
// }

// const handleRegister = (data) => {
//   console.log('Register attempt:', data)
//   // TODO: Реализовать логику регистрации
//   closeLoginModal()
// }

const closeMenuOnNavigate = () => {
  isMenuOpen.value = false
}

const handleContacts = () => {
  // Обработка клика на "Контакты"
  // Можно добавить модальное окно или скролл к секции контактов
  isMenuOpen.value = false
  console.log('Контакты')
}

const handleOffer = () => {
  // Обработка клика на "Офферта"
  // Можно добавить модальное окно или переход на страницу
  isMenuOpen.value = false
  console.log('Офферта')
}

// Загружаем корзину при монтировании компонента
onMounted(() => {
  cartStore.fetchCart()
})

// Добавляем/убираем класс на body при открытии/закрытии меню для плавного сдвига контента
watch(isMenuOpen, (newValue) => {
  if (typeof document !== 'undefined') {
    if (newValue) {
      document.body.classList.add('menu-open')
    } else {
      document.body.classList.remove('menu-open')
    }
  }
})

onUnmounted(() => {
  if (typeof document !== 'undefined') {
    document.body.classList.remove('menu-open')
  }
})


</script>

<style lang="scss" scoped>
@use '@/assets/styles/breakpoints' as *;
.app-header {
  width: 100%;
  height: 208px;
  background-color: #F6F5EC;
  flex-shrink: 0;
  transition: height 0.3s ease;
}

.app-header.menu-open {
  height: 250px;
}

.header-container {
  width: 100%;
  max-width: 1280px;
  height: 100%;
  margin: 0 auto;
  position: relative;
}

.logo-wrapper {
  position: absolute;
  left: 40px;
  top: 0;
  width: 198px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  cursor: pointer;
  transition: opacity 0.2s;
  z-index: 10; /* Гарантируем, что логотип поверх других элементов */
}

.logo-wrapper:hover {
  opacity: 0.8;
}

.logo-image {
  width: 100%;
  height: 100%;
  max-width: 198px;
  max-height: 64px;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  position: relative;
  z-index: 1;
  will-change: transform;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.menu-button {
  position: absolute;
  left: 255px;
  top: 5px;
  width: 54px;
  height: 54px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-icon {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.search-clear-button {
  position: absolute;
  left: 309px;
  top: 14.5px;
  width: 26px;
  height: 26px;
  background-color: #FFFFFF;
  border: 2px solid #640000;
  border-radius: 0;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  z-index: 10;
}

.search-clear-x {
  color: #640000;
  font-size: 24px;
  font-weight: 400;
  line-height: 1;
  font-family: 'Inter', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-wrapper {
  position: absolute;
  left: 335px;
  top: 5.5px;
  width: 691px;
  height: 55px;
  border-radius: 10px;
  padding: 13px 16px;
  border: 2px solid #640000;
  background-color: #FFFFFF;
  opacity: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  gap: 10px;
}

.search-input {
  flex: 1;
  height: 100%;
  border: none;
  outline: none;
  background: transparent;
  font-size: 24px;
  color: #1B1716;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  line-height: 100%;
  letter-spacing: -0.24px;
  padding: 0;
  min-width: 0;
}

.search-input::placeholder {
  color: #1B1716;
  opacity: 0.6;
}

.search-button {
  width: 24px;
  height: 24px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.search-icon-img {
  width: 24px;
  height: 24px;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.filter-button {
  position: absolute;
  left: 33px;
  top: 137px;
  width: 30px;
  height: 30px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.filter-icon {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.categories-wrapper {
  position: absolute;
  left: 73px;
  top: 137px;
  display: flex;
  align-items: center;
  gap: 20px;
  height: 35px;
}

.category-item {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.16px;
  color: #1B1716;
  opacity: 0.6;
  white-space: nowrap;
  cursor: pointer;
  transition: opacity 0.2s;
}

.category-item:hover {
  opacity: 1;
}

.login-button {
  position: absolute;
  left: 1050px;
  top: 5.5px;
  width: 47px;
  height: 53px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.login-icon {
  width: 32px;
  height: 32px;
  max-width: 32px;
  max-height: 32px;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.login-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
  opacity: 0.6;
  white-space: nowrap;
}

.orders-button {
  position: absolute;
  left: 1117px;
  top: 5.5px;
  width: 56px;
  height: 53px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.orders-icon {
  width: 32px;
  height: 32px;
  max-width: 32px;
  max-height: 32px;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.orders-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
  opacity: 0.6;
  white-space: nowrap;
}

.cart-button {
  position: absolute;
  left: 1193px;
  top: 5.5px;
  width: 64px;
  height: 53px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  position: relative;
}

.cart-icon {
  width: 32px;
  height: 32px;
  max-width: 32px;
  max-height: 32px;
  object-fit: contain;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  will-change: transform;
}

.cart-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
  opacity: 0.6;
  white-space: nowrap;
}

.cart-badge {
  position: absolute;
  top: -5px;
  right: -5px;
  background-color: #640000;
  color: #FFFFFF;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 600;
  line-height: 1;
}

.menu-navigation {
  position: absolute;
  left: 50%;
  top: 137px;
  transform: translateX(-50%);
  width: 960px;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  background: #F6F5EC;
  z-index: 100;
}

.nav-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  flex: 1;
  height: 100%;
}

.nav-divider {
  width: 2px;
  height: 120px;
  background: #640000;
  opacity: 1;
  flex-shrink: 0;
}

.nav-link {
  width: 77px;
  height: 24px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
  text-decoration: none;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.nav-link:hover {
  opacity: 1;
}

.filter-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 1000;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  padding-top: 304px;
  padding-left: 32px;
}

.filter-modal {
  position: relative;
  width: 299px;
  min-height: 328px;
  background-color: #F6F5EC;
  border: 2px solid #640000;
  border-radius: 10px;
  padding: 32px 24px;
  box-sizing: border-box;
}

.filter-options {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.filter-option {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  position: relative;
}

.filter-radio {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.filter-radio-custom {
  width: 22px;
  height: 22px;
  border-radius: 11px;
  border: 2px solid #1B1716;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: all 0.2s;
}

.filter-option-selected .filter-radio-custom {
  background-color: transparent;
}

.filter-option-selected .filter-radio-custom::after {
  content: '';
  width: 12px;
  height: 12px;
  border-radius: 6px;
  background-color: #1B1716;
  display: block;
}

.filter-option-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.16px;
  color: #1B1716;
  opacity: 0.6;
  user-select: none;
}

.filter-option-selected .filter-option-text {
  opacity: 1;
}

.info-banner {
  position: absolute;
  left: 32px;
  top: 80px;
  width: 1216px;
  height: 40px;
  border-radius: 10px;
  background: #640000;
  opacity: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-sizing: border-box;
}

.info-banner-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0;
  color: #F6F5EC;
  width: 553px;
  height: 19px;
  opacity: 1;
  white-space: nowrap;
}

.info-banner-contacts {
  display: flex;
  align-items: center;
  gap: 16px;
}

.info-banner-phone {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0;
  color: #F6F5EC;
  width: 150px;
  height: 19px;
  opacity: 1;
  white-space: nowrap;
}

.info-banner-icon {
  width: 20px;
  height: 20px;
  border: none;
  background: none;
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.info-banner-icon-img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: contain;
}

/* Нижняя навигационная панель - скрыта по умолчанию, показывается на мобильных */
.mobile-bottom-nav {
  display: none;
}

/* Скрываем мобильные элементы на десктопе */
@include desktop {
  .mobile-bottom-nav,
  .mobile-ad-banner,
  .mobile-search-wrapper,
  .mobile-category,
  .mobile-menu-overlay {
    display: none;
  }
}

/* Также скрываем мобильные элементы на десктопных устройствах даже при масштабировании */
.is-desktop-device .mobile-bottom-nav,
.is-desktop-device .mobile-ad-banner,
.is-desktop-device .mobile-search-wrapper,
.is-desktop-device .mobile-category,
.is-desktop-device .mobile-menu-overlay {
  display: none !important;
}

/* Восстанавливаем десктопные стили хедера на десктопных устройствах даже при масштабировании */
.is-desktop-device .app-header {
  height: 208px !important; /* Полная высота хедера с фильтрами */
  position: relative !important;
}

.is-desktop-device .header-container {
  max-width: 1300px !important;
  width: 100% !important;
}

.is-desktop-device .logo-wrapper {
  position: absolute !important;
  left: 40px !important;
  top: 0 !important;
  width: 198px !important;
  height: 64px !important;
  z-index: 10 !important;
}

/* Гарантируем, что фильтры и категории всегда видны на десктопе */
.is-desktop-device .filter-button {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
}

.is-desktop-device .categories-wrapper {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
}

.is-desktop-device .logo-image {
  max-width: 198px !important;
  max-height: 64px !important;
  width: 100% !important;
  height: 100% !important;
}

.is-desktop-device .menu-button {
  position: absolute !important;
  left: 255px !important;
  top: 5px !important;
  width: 54px !important;
  height: 54px !important;
  display: flex !important;
}

.is-desktop-device .search-wrapper {
  position: absolute !important;
  left: 335px !important;
  top: 5.5px !important;
  width: 691px !important;
  height: 55px !important;
  display: flex !important;
}

.is-desktop-device .search-clear-button {
  position: absolute !important;
  left: 309px !important;
  top: 14.5px !important;
  display: flex !important;
}

.is-desktop-device .orders-button {
  position: absolute !important;
  left: 1117px !important;
  top: 5.5px !important;
  width: 56px !important;
  height: 53px !important;
  display: flex !important;
}

.is-desktop-device .cart-button {
  position: absolute !important;
  left: 1193px !important;
  top: 5.5px !important;
  width: 64px !important;
  height: 53px !important;
  display: flex !important;
}

.is-desktop-device .filter-button {
  position: absolute !important;
  left: 33px !important;
  top: 137px !important;
  display: flex !important;
}

.is-desktop-device .categories-wrapper {
  position: absolute !important;
  left: 73px !important;
  top: 137px !important;
  display: flex !important;
}

.is-desktop-device .menu-navigation {
  position: absolute !important;
  left: 50% !important;
  top: 137px !important;
  transform: translateX(-50%) !important;
  display: flex !important;
  z-index: 100 !important;
}

.is-desktop-device .login-button {
  position: absolute !important;
  left: 1050px !important;
  top: 5.5px !important;
  width: 47px !important;
  height: 53px !important;
  padding: 0 !important;
  gap: 2px !important;
  background: transparent !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
}

.is-desktop-device .login-icon {
  display: block !important;
}

.is-desktop-device .info-banner {
  position: absolute !important;
  left: 32px !important;
  top: 80px !important;
  width: 1216px !important;
  max-width: 1216px !important;
  height: 40px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 0 24px !important;
}

/* Дополнительные стили для очень маленьких экранов (до 400px) */
@include mobile {
  /* Можно добавить специфичные стили для очень маленьких экранов, если нужно */
}

/* Мобильная и планшетная адаптация (до 1279px), но только для мобильных устройств */
@include tablet-down {
  .is-mobile-device .app-header {
    height: 310px;
    position: relative;
    background-color: #F6F5EC;
  }

  /* Уменьшаем высоту хедера на странице корзины */
  .is-mobile-device .app-header.cart-page {
    height: 75px;
  }

  /* Уменьшаем высоту хедера на странице заказов */
  .is-mobile-device .app-header.orders-page {
    height: 100px;
  }

  /* Высота хедера на странице товара */
  .is-mobile-device .app-header.product-page {
    height: 200px;
  }

  .is-mobile-device .header-container {
    max-width: 100%;
    width: 100%;
  }

  /* Логотип */
  .is-mobile-device .logo-wrapper {
    position: absolute;
    left: 16px;
    top: 24px;
    width: 123.75px;
    height: 40px;
    z-index: 10;
  }

  .is-mobile-device .logo-image {
    max-width: 123.75px !important;
    max-height: 40px !important;
    width: 100% !important;
    height: 100% !important;
  }

  /* Скрываем десктопные элементы только на мобильных */
  .is-mobile-device .menu-button,
  .is-mobile-device .search-wrapper,
  .is-mobile-device .search-clear-button,
  .is-mobile-device .orders-button,
  .is-mobile-device .cart-button,
  .is-mobile-device .filter-button,
  .is-mobile-device .categories-wrapper,
  .is-mobile-device .menu-navigation,
  .is-mobile-device .info-banner-contacts {
    display: none;
  }


  /* Модальное окно фильтров на мобильных устройствах */
  .is-mobile-device .filter-modal-overlay {
    padding-top: 140px;
    padding-left: 16px;
    align-items: flex-start;
    justify-content: flex-start;
  }

  .is-mobile-device .filter-modal {
    width: calc(100vw - 32px);
    max-width: 299px;
    padding: 24px 16px;
  }

  /* На десктопных устройствах всегда показываем фильтры и категории (но не меню, оно показывается только при isMenuOpen) */
  .is-desktop-device .filter-button,
  .is-desktop-device .categories-wrapper {
    display: flex !important;
  }

  /* Меню показывается только когда оно открыто (v-if="isMenuOpen") */
  .is-desktop-device .menu-navigation {
    display: flex !important;
  }

  /* Кнопка "Профиль" - переопределяем десктопные стили */
  .login-button {
    position: absolute !important;
    right: 16px !important;
    left: auto !important;
    top: 30px !important;
    width: auto !important;
    min-width: 70px !important;
    max-width: 100px !important;
    height: 28px !important;
    border-radius: 10px !important;
    padding: 8px 10px !important;
    gap: 4px !important;
    background: #1B1716CC !important;
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    box-sizing: border-box !important;
    z-index: 100 !important;
  }

  .login-icon {
    display: none;
  }

  .login-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 10px;
    line-height: 100%;
    letter-spacing: 0%;
    color: #F6F5EC;
    white-space: nowrap;
  }

  /* Информационный баннер */
  .info-banner {
    position: absolute;
    left: 16px;
    top: 72px;
    width: calc(100% - 32px);
    max-width: 100%;
    height: 28px;
    border-radius: 10px;
    padding: 8px 16px;
    gap: 8px;
    background: #640000;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  .info-banner-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 9px;
    line-height: 100%;
    letter-spacing: 0;
    color: #F6F5EC;
    width: auto;
    height: auto;
    white-space: nowrap;
  }

  /* Рекламный баннер для мобильных */
  .mobile-ad-banner {
    position: absolute;
    left: 16px;
    top: 108px;
    width: calc(100% - 32px);
    max-width: 100%;
    height: 108px; /* Фиксированная высота для одинакового отображения */
    display: block;
    box-sizing: border-box;
    margin-bottom: 0;
    overflow: hidden; /* Обрезаем лишнее */
    border-radius: 10px; /* Скругление углов */
  }

  .ad-banner-image {
    width: 100%;
    height: 100%; /* Заполняем всю высоту контейнера */
    display: block;
    object-fit: cover; /* Заполняем контейнер, сохраняя пропорции */
    object-position: center;
    border-radius: 10px; /* Скругление углов для изображения */
  }

  /* Поисковая строка для мобильных */
  .mobile-search-wrapper {
    position: absolute;
    left: 16px;
    top: 108px;
    width: calc(100% - 32px);
    max-width: 100%;
    height: 35px;
    border-radius: 10px;
    padding: 8px 16px;
    border: 2px solid #640000;
    background: #F6F5EC;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
  }

  /* Позиция поиска на главной странице (когда есть рекламный баннер) */
  .app-header:has(.mobile-ad-banner) .mobile-search-wrapper {
    top: 224px; /* 108px (top баннера) + 108px (высота баннера) + 8px (отступ) */
  }

  .mobile-search-input {
    flex: 1;
    border: none;
    background: transparent;
    outline: none;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    padding: 0;
    margin: 0;
  }

  .mobile-search-input::placeholder {
    color: #1B1716;
    opacity: 0.6;
  }

  .mobile-search-button {
    width: 20px;
    height: 20px;
    border: none;
    background: none;
    padding: 0;
    margin: 0 0 0 8px; /* Отступ слева от кнопки до инпута */
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0; /* Предотвращаем сжатие кнопки */
    min-width: 20px; /* Минимальная ширина кнопки */
  }

  .mobile-search-icon {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: contain;
  }

  /* Исправление для очень маленьких экранов (< 300px) */
  @media (max-width: 299px) {
    .mobile-search-wrapper {
      left: 8px;
      width: calc(100% - 16px);
      padding: 6px 8px;
    }

    .mobile-search-input {
      font-size: 14px;
      min-width: 0; /* Позволяем инпуту сжиматься */
    }

    .mobile-search-button {
      width: 18px;
      height: 18px;
      min-width: 18px;
      margin-left: 4px;
    }
  }

  /* Категории для мобильных */
  .mobile-category {
    position: absolute;
    left: 16px;
    top: 151px;
    display: flex;
    align-items: center;
    gap: 10px;
    width: calc(100% - 32px);
    max-width: 100%;
    box-sizing: border-box;
  }

  /* Позиция категорий на главной странице (когда есть рекламный баннер) */
  .app-header:has(.mobile-ad-banner) .mobile-category {
    top: 267px; /* 108px (top баннера) + 108px (высота баннера) + 35px (высота поиска) + 8px (отступ) + 8px (дополнительный отступ) */
  }

  .mobile-category-icon {
    width: 32px;
    height: 32px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    flex-shrink: 0;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
  }

  .category-icon-img {
    width: 32px;
    height: 32px;
    display: block;
    object-fit: contain;
  }

  .mobile-categories-scroll {
    display: flex;
    align-items: center;
    gap: 10px;
    overflow-x: auto;
    overflow-y: hidden;
    flex: 1;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    -ms-overflow-style: none;
  }

  .mobile-categories-scroll::-webkit-scrollbar {
    display: none;
  }

  .mobile-category-item {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    white-space: nowrap;
    flex-shrink: 0;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }

  .mobile-category-item:active {
    color: #1B1716;
  }

  /* Нижняя навигационная панель */
  .mobile-bottom-nav {
    display: flex !important;
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
    height: 64px !important;
    background: #F6F5EC !important;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    align-items: center;
    justify-content: space-around;
    padding: 8px 0;
    z-index: 99999 !important;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    isolation: isolate;
  }

  .bottom-nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    flex: 1;
    max-width: 60px;
  }

  .bottom-nav-icon {
    width: 24px;
    height: 24px;
    object-fit: contain;
  }

  .bottom-nav-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    transition: color 0.2s ease;
  }

  .bottom-nav-item.active .bottom-nav-text {
    color: #1B1716;
  }

  /* Иконки для неактивных элементов делаем серыми */
  .bottom-nav-item:not(.active) .bottom-nav-icon {
    opacity: 0.6;
    filter: grayscale(1) brightness(0.6);
  }

  /* Активные иконки остаются с оригинальным цветом */
  .bottom-nav-item.active .bottom-nav-icon {
    opacity: 1;
    filter: none;
  }

  /* Кнопка меню всегда красная */
  .bottom-nav-menu .bottom-nav-icon {
    opacity: 1;
    filter: none;
  }

  .bottom-nav-menu .bottom-nav-text {
    color: #1B1716;
  }

  .bottom-nav-menu.active .bottom-nav-text {
    color: #1B1716;
  }

  /* Мобильное меню */
  .mobile-menu-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 64px;
    background: rgba(0, 0, 0, 0.5);
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    animation: fadeIn 0.3s ease forwards;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .mobile-menu {
    position: relative;
    width: 100%;
    max-width: 100%;
    height: 100%;
    background: #F6F5EC;
    border: 2px solid #1B1716;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
    transform: translateY(-20px);
    animation: slideIn 0.3s ease forwards;
  }

  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateY(-20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .mobile-menu-close {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 70px;
    height: 70px;
    padding: 10px;
    gap: 10px;
    background: transparent;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  .mobile-menu-close-icon {
    font-size: 60px;
    line-height: 1;
    color: #1B1716;
    font-weight: 300;
  }

  .mobile-menu-nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
    width: 100%;
    max-width: 300px;
  }

  .mobile-menu-item {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    text-decoration: none;
    text-align: center;
    transition: color 0.2s ease;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
  }

  .mobile-menu-item.active {
    color: #640000;
  }
}

/* Скрываем мобильные элементы на десктопе */
@include desktop {
  .mobile-ad-banner,
  .mobile-search-wrapper,
  .mobile-category,
  .mobile-bottom-nav,
  .mobile-menu-overlay {
    display: none;
  }
}

/* Также скрываем мобильные элементы на десктопных устройствах (даже при масштабировании) */
.is-desktop-device .mobile-ad-banner,
.is-desktop-device .mobile-search-wrapper,
.is-desktop-device .mobile-category,
.is-desktop-device .mobile-bottom-nav,
.is-desktop-device .mobile-menu-overlay {
  display: none !important;
}

/* Планшетная адаптация */
@include tablet {
  // Планшетные стили при необходимости
}

</style>
