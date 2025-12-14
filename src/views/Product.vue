<template>
  <div class="product-page">
    <div class="product-content">
      <!-- Десктопная версия -->
      <div class="desktop-product">
      <div class="product-main">
        <div class="product-photos">
          <div class="product-photo-placeholder" @click="openPhotoModal"></div>
          <div class="photo-thumbnails">
            <button class="thumbnail-nav-button thumbnail-nav-left" type="button">
                <img :src="arrowIcon" alt="Назад" class="arrow-icon" />
            </button>
            <div class="thumbnail-list">
              <div class="thumbnail-item" @click="openPhotoModal"></div>
              <div class="thumbnail-item" @click="openPhotoModal"></div>
              <div class="thumbnail-item" @click="openPhotoModal"></div>
              <div class="thumbnail-item" @click="openPhotoModal"></div>
            </div>
            <button class="thumbnail-nav-button thumbnail-nav-right" type="button">
                <img :src="arrowIcon" alt="Вперёд" class="arrow-icon arrow-icon-right" />
            </button>
          </div>
        </div>
        <div class="product-info">
          <!-- Фильтры/теги товара для десктопа -->
          <div class="desktop-tags-container">
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">Винтаж</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">Туалетная вода</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">L'Air du Temps</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">EDT</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">Спрей</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">120 мл</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">Полный</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">Nina Ricci</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">Франция</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
            <span class="desktop-tag-item">
              <span class="desktop-tag-text">1990-е</span>
              <img :src="arrowIcon" alt="Стрелка" class="desktop-tag-arrow-icon" />
            </span>
          </div>
            <h1 class="product-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</h1>
          <div class="product-details">
            <div class="detail-item">
              <span class="detail-label">Артикул товара:</span>
              <div class="article-container">
                <span class="article-value">GH20 270</span>
                <button class="copy-button" type="button">
                  <img :src="copyIconSvg" alt="Копировать" class="copy-icon" />
                </button>
              </div>
            </div>
            <div class="detail-item">
              <span class="detail-label">Количество товара:</span>
              <span class="detail-value product-quantity">1 шт</span>
            </div>
            <div class="detail-item">
              <span class="detail-label">Количество просмотров:</span>
              <div class="views-container">
                <span class="detail-value">24</span>
                <img :src="viewsIconSvg" alt="Просмотры" class="views-icon" />
              </div>
            </div>
          </div>
          <div class="product-price">
            <span class="price-value">2500 ₽</span>
            <span class="price-label">цена от поставщика</span>
          </div>
          <div class="boutique-price">
            <span class="boutique-price-value">7500 ₽</span>
            <span class="boutique-price-label">цена в бутиках (средняя)</span>
          </div>
          <button class="add-to-cart-button" type="button">
              <img :src="cartIconSvg" alt="Корзина" class="card-cart-icon" />
              <span class="card-cart-text">В корзину</span>
          </button>
          <button class="buy-now-button" type="button">
            Купить сейчас
          </button>
          <button class="ask-question-button" type="button">
            Задать вопрос
          </button>
        </div>
      </div>
      <div class="recommended-section">
        <h2 class="recommended-title">Рекомендуем также</h2>
        <div class="recommended-products">
          <div class="recommended-card" v-for="i in 10" :key="i">
            <div class="card-image-wrapper">
              <img :src="exampleImg" alt="Товар" class="card-image" />
              <div class="card-views">
                <img :src="cardViewsSvg" alt="Просмотры" class="card-views-icon" />
                <span class="card-views-count">24</span>
              </div>
            </div>
            <div class="card-content">
              <div class="card-prices">
                <span class="card-price-current">2500 ₽</span>
                <span class="card-price-old">7500 ₽</span>
              </div>
              <div class="card-price-label">цена от поставщика</div>
              <div class="card-description">Lorem ipsum dolor sit amet d...</div>
              <button class="card-add-to-cart-button" type="button">
                <img :src="cartIconSvg" alt="Корзина" class="card-cart-icon" />
                <span class="card-cart-text">В корзину</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    
      <!-- Мобильная версия -->
      <div class="mobile-product">
        <!-- Галерея фото с горизонтальной прокруткой -->
        <div class="mobile-photos-container">
          <div class="mobile-photos-scroll">
            <div class="mobile-photo-item" v-for="i in 3" :key="i"></div>
          </div>
        </div>
        
        <!-- Название товара -->
        <h1 class="mobile-product-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</h1>
        
        <!-- Цены -->
        <div class="mobile-price-section">
          <div class="mobile-price-row">
            <span class="mobile-price-value">2500 ₽</span>
            <span class="mobile-price-label">цена от поставщика</span>
          </div>
          <div class="mobile-boutique-price-row">
            <span class="mobile-boutique-price-value">7500 ₽</span>
            <span class="mobile-boutique-price-label">цена в бутиках (средняя)</span>
          </div>
        </div>
        
        <!-- Детали товара -->
        <div class="mobile-product-details">
          <div class="mobile-detail-item">
            <span class="mobile-detail-label">Артикул товара:</span>
            <span class="mobile-detail-value">GH20 270</span>
          </div>
          <div class="mobile-detail-item">
            <span class="mobile-detail-label">Количество товара:</span>
            <span class="mobile-detail-value">1 шт</span>
          </div>
          <div class="mobile-detail-item">
            <span class="mobile-detail-label">Количество просмотров:</span>
            <span class="mobile-detail-value">24</span>
          </div>
        </div>
        
        <!-- Все характеристики -->
        <div class="mobile-characteristics-link">Все характеристики</div>
        
        <!-- Характеристики товара (прокручиваемые теги) -->
        <div class="mobile-tags-container">
          <div class="mobile-tags-scroll">
            <span class="mobile-tag-item">
              <span class="tag-text">Винтаж</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">Туалетная вода</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">L'Air du Temps</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">EDT</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">Спрей</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">120 мл</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">Полный</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">Nina Ricci</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">Франция</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
            <span class="mobile-tag-item">
              <span class="tag-text">1990-е</span>
              <img :src="arrowIcon" alt="Стрелка" class="tag-arrow-icon" />
            </span>
          </div>
        </div>
        
        <!-- Секция Рекомендуем -->
        <div class="mobile-recommended-section">
          <h2 class="mobile-recommended-title">Рекомендуем</h2>
          <div class="mobile-recommended-products">
            <div class="mobile-recommended-card" v-for="i in 4" :key="i">
              <div class="mobile-card-image-wrapper">
                <img :src="exampleImg" alt="Товар" class="mobile-card-image" />
                <div class="mobile-card-views">
                  <span class="mobile-card-views-count">24</span>
                </div>
              </div>
              <div class="mobile-card-content">
                <div class="mobile-card-prices">
                  <span class="mobile-card-price-current">2500 ₽</span>
                  <span class="mobile-card-price-old">7500 ₽</span>
                </div>
                <div class="mobile-card-price-label">цена от поставщика</div>
                <div class="mobile-card-description">Lorem ipsum dolor sit amet...</div>
                <button class="mobile-card-add-to-cart-button" type="button">
                  <img :src="cartIconSvg" alt="Корзина" class="mobile-card-cart-icon" />
                  <span class="mobile-card-cart-text">В корзину</span>
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Меню действий (над нижней панелью) -->
        <div class="mobile-actions-menu">
          <div class="mobile-actions-row">
            <button class="mobile-action-button mobile-buy-now-button" type="button">
              <span class="mobile-action-text">Купить сейчас</span>
            </button>
            <button class="mobile-action-button mobile-add-to-cart-button" type="button">
              <span class="mobile-action-text">В корзину</span>
            </button>
          </div>
          <button class="mobile-action-button mobile-ask-question-button" type="button">
            <span class="mobile-action-text">Задать вопрос</span>
          </button>
        </div>
      </div>
      
      <!-- Модальное окно просмотра фото (десктоп) -->
    <div v-if="isPhotoModalOpen" class="photo-modal-overlay" @click="closePhotoModal">
      <div class="photo-modal-content" @click.stop>
        <div class="modal-main-image"></div>
        <div class="modal-thumbnails">
          <div class="modal-thumbnail"></div>
          <div class="modal-thumbnail"></div>
          <div class="modal-thumbnail"></div>
          <div class="modal-thumbnail"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import arrowIcon from '@/assets/images/icon-arrow.svg'
import cartIconSvg from '@/assets/images/icon-cart-button.svg'
import exampleImg from '@/assets/images/example.png'
import copyIconSvg from '@/assets/images/icon-copy.svg'
import viewsIconSvg from '@/assets/images/icon-views.svg'
import cardViewsSvg from '@/assets/images/icon-views-card.svg'

const route = useRoute()
const productId = route.params.id

const isPhotoModalOpen = ref(false)

const openPhotoModal = () => {
  isPhotoModalOpen.value = true
}

const closePhotoModal = () => {
  isPhotoModalOpen.value = false
}

// TODO: Загрузить данные товара по ID
</script>

<style scoped>
.product-page {
  width: 100%;
  min-height: 100%;
  padding: 0;
  background-color: #F6F5EC;
}

.product-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
}

.breadcrumbs {
  width: 100%;
  padding: 16px 20px 0 32px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'Inter', sans-serif;
}

.breadcrumb-item {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
}

.breadcrumb-first {
  opacity: 0.6;
}

.breadcrumb-second {
  opacity: 1;
}

.breadcrumb-slash {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  display: inline-block;
  flex-shrink: 0;
}

.filters-container {
  width: 100%;
  padding: 16px 20px 0 32px;
  box-sizing: border-box;
}

.filters-image {
  width: 100%;
  max-width: 1216px;
  height: auto;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
}

.product-main {
  width: 100%;
  padding: 24px 20px 0 32px;
  box-sizing: border-box;
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

.product-photos {
  display: flex;
  flex-direction: column;
  gap: 16px;
  flex-shrink: 0;
}

.product-photo-placeholder {
  width: 477px;
  height: 477px;
  border-radius: 10px;
  background: #D9D9D9;
  opacity: 1;
  cursor: pointer;
  transition: opacity 0.2s;
  user-select: none;
  -webkit-user-select: none;
  pointer-events: auto;
}

.product-photo-placeholder:hover {
  opacity: 0.9;
}

.photo-thumbnails {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 477px;
}

.thumbnail-nav-button {
  width: 11px;
  height: 24px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 1;
  flex-shrink: 0;
}

.arrow-icon {
  width: 11px;
  height: 24px;
  display: block;
}

.arrow-icon-right {
  transform: scaleX(-1);
}

.thumbnail-list {
  display: flex;
  gap: 8px;
  flex: 1;
  justify-content: center;
}

.thumbnail-item {
  width: 80px;
  height: 80px;
  border-radius: 10px;
  background: #D9D9D9;
  opacity: 1;
  flex-shrink: 0;
}

.product-info {
  flex: 1 1 auto;
  min-width: 0;
  padding-left: 0;
}

/* Фильтры/теги товара для десктопа */
.desktop-tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 24px;
  width: 100%;
}

.desktop-tag-item {
  background: #1B171699;
  border-radius: 10px;
  padding: 8px 16px;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.desktop-tag-item:hover {
  opacity: 0.8;
}

.desktop-tag-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0%;
  color: #F6F5EC;
}

.desktop-tag-arrow-icon {
  width: 6px;
  height: 13px;
  display: block;
  filter: brightness(0) invert(1);
  transform: rotate(180deg);
}

.product-title {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 24px 0;
  padding: 0;
  opacity: 1;
}

.product-details {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 345px;
  opacity: 1;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
}

.detail-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
}

.article-container {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 8px;
  color: inherit;
  background-color: #F6F5EC;
}

.article-value {
  color: #1B1716 !important;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  opacity: 1;
  display: inline-block;
}

.copy-button {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.copy-icon {
  width: 16px;
  height: 16px;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
}

.views-container {
  display: flex;
  align-items: center;
  gap: 4px;
}

.detail-value {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
}

.product-quantity {
  color: #1B1716 !important;
  opacity: 1;
}

.views-icon {
  width: 19px;
  height: 12px;
  display: block;
  opacity: 0.6;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
}

.copy-icon {
  opacity: 0.6;
}

.product-price {
  opacity: 1;
  margin-top: 90px;
  display: flex;
  flex-direction: row;
  align-items: baseline;
  gap: 16px;
}

.price-value {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #640000;
  width: 85px;
  height: 29px;
}

.price-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  width: 157px;
  height: 19px;
  opacity: 1;
}

.boutique-price {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  margin-top: 8px;
  width: 268px;
}

.boutique-price-value {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  text-decoration: line-through;
  width: 56px;
  height: 19px;
  opacity: 0.6;
}

.boutique-price-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  width: 196px;
  height: 19px;
  opacity: 0.6;
}

.add-to-cart-button {
  width: 477px;
  height: 35px;
  border-radius: 10px;
  padding: 8px 24px;
  background-color: #640000;
  border: none;
  cursor: pointer;
  opacity: 1;
  margin-top: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: background-color 0.2s ease, opacity 0.2s ease;
}

.add-to-cart-button .card-cart-icon {
  width: 16px;
  height: 16px;
  display: block;
}

.add-to-cart-button .card-cart-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0%;
  color: #F6F5EC;
  opacity: 1;
  width: auto;
  height: auto;
  white-space: nowrap;
}

.add-to-cart-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

.add-to-cart-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

.buy-now-button {
  width: 477px;
  height: 35px;
  border-radius: 10px;
  padding: 8px 24px;
  background-color: rgba(27, 23, 22, 0.6);
  border: none;
  color: #F6F5EC;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0;
  cursor: pointer;
  opacity: 1;
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.buy-now-button:hover {
  opacity: 0.7;
}

.ask-question-button {
  width: 477px;
  height: 35px;
  border-radius: 10px;
  padding: 8px 24px;
  background-color: #F6F5EC;
  border: 2px solid #1B1716;
  color: #1B1716;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0;
  cursor: pointer;
  opacity: 1;
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.ask-question-button:hover {
  opacity: 0.9;
}

.recommended-section {
  width: 100%;
  padding: 40px 20px 60px 32px;
  box-sizing: border-box;
}

.recommended-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 24px 0;
  padding: 0;
  width: 243px;
  height: 29px;
  opacity: 1;
}

.recommended-products {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.recommended-card {
  width: 236px;
  background: #F6F5EC;
  border-radius: 10px;
  overflow: hidden;
  opacity: 1;
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 287px;
  overflow: hidden;
  border-radius: 10px 10px 0 0;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.card-views {
  position: absolute;
  top: 8px;
  left: 8px;
  display: flex;
  align-items: center;
  gap: 4px;
  z-index: 1;
}

.card-views-icon {
  width: 20px;
  height: 19px;
  display: block;
  opacity: 1;
}

.card-views-count {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #F6F5EC;
  opacity: 1;
}

.card-content {
  padding: 16px 16px 16px 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.card-prices {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.card-price-current {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #640000;
  width: 85px;
  height: 29px;
  opacity: 1;
}

.card-price-old {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
  text-decoration: line-through;
  width: 54px;
  height: 19px;
}

.card-price-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 14px;
  line-height: 100%;
  letter-spacing: 0;
  color: #640000;
  width: 147px;
  height: 17px;
  opacity: 1;
}

.card-description {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #72706b;
  opacity: 1;
  margin-top: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.card-add-to-cart-button {
  width: 230px;
  height: 35px;
  border-radius: 10px;
  padding: 8px 24px;
  background: #640000;
  border: none;
  cursor: pointer;
  margin-top: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  opacity: 1;
}

.card-cart-icon {
  width: 16px;
  height: 16px;
  display: block;
}

.card-cart-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0%;
  color: #F6F5EC;
  opacity: 1;
  width: auto;
  height: auto;
  white-space: nowrap;
}

.photo-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.photo-modal-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.modal-main-image {
  width: 614px;
  height: 614px;
  border-radius: 10px;
  background: #D9D9D9;
  opacity: 1;
  flex-shrink: 0;
}

.modal-thumbnails {
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: center;
}

.modal-thumbnail {
  width: 80px;
  height: 80px;
  border-radius: 10px;
  background: #D9D9D9;
  opacity: 1;
  flex-shrink: 0;
  cursor: pointer;
  transition: opacity 0.2s;
}

.modal-thumbnail:hover {
  opacity: 0.8;
}

.thumbnail-item {
  cursor: pointer;
  transition: opacity 0.2s;
}

.thumbnail-item:hover {
  opacity: 0.8;
}

/* Мобильная версия страницы товара (до 550px) */
@media (max-width: 550px) {
  .mobile-product {
    padding: 0 16px;
    padding-bottom: 182px; /* 118px (меню действий) + 64px (нижняя панель) */
  }

  /* Галерея фото */
  .mobile-photos-container {
    width: 100%;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    -ms-overflow-style: none;
    margin-top: 16px;
  }

  .mobile-photos-container::-webkit-scrollbar {
    display: none;
  }

  .mobile-photos-scroll {
    display: flex;
    gap: 8px;
    width: max-content;
    padding: 0 0 8px 0;
  }

  .mobile-photo-item {
    width: 316px;
    height: 316px;
    border-radius: 10px;
    background: #D9D9D9;
    flex-shrink: 0;
  }


  /* Название товара */
  .mobile-product-title {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 16px 0 0 0;
    padding: 0;
    width: 100%;
    max-width: 100%;
    height: auto;
    min-height: 57px;
    box-sizing: border-box;
  }

  /* Прокручиваемые теги характеристик */
  .mobile-tags-container {
    width: 100%;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    -ms-overflow-style: none;
    margin-top: 16px;
  }

  .mobile-tags-container::-webkit-scrollbar {
    display: none;
  }

  .mobile-tags-scroll {
    display: flex;
    gap: 8px;
    width: max-content;
    padding: 0 0 8px 0;
  }

  .mobile-tag-item {
    background: #1B171699;
    border-radius: 10px;
    padding: 8px 16px;
    white-space: nowrap;
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }

  .tag-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: 0%;
    color: #F6F5EC;
  }

  .tag-arrow-icon {
    width: 6px;
    height: 13px;
    display: block;
    filter: brightness(0) invert(1);
    transform: rotate(180deg);
  }

  /* Секция цен */
  .mobile-price-section {
    margin-top: 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .mobile-price-row {
    display: flex;
    align-items: baseline;
    gap: 16px;
  }

  .mobile-price-value {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 24px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
    width: 85px;
    height: 29px;
  }

  .mobile-price-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: 157px;
    height: 19px;
  }

  .mobile-boutique-price-row {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .mobile-boutique-price-value {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    text-decoration: line-through;
    width: 56px;
    height: 19px;
    opacity: 0.6;
  }

  .mobile-boutique-price-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    width: 196px;
    height: 19px;
  }

  /* Детали товара */
  .mobile-product-details {
    margin-top: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .mobile-detail-item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-detail-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .mobile-detail-value {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  /* Все характеристики */
  .mobile-characteristics-link {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin-top: 24px;
    width: 158px;
    height: 19px;
    cursor: pointer;
  }

  /* Секция Рекомендуем */
  .mobile-recommended-section {
    margin-top: 60px;
    margin-bottom: 40px;
    padding: 0 16px;
    box-sizing: border-box;
  }

  .mobile-recommended-title {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: 109px;
    height: 19px;
    margin: 0 0 16px 0;
    padding: 0;
  }

  .mobile-recommended-products {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    width: 100%;
    box-sizing: border-box;
  }

  .mobile-recommended-card {
    width: 100%;
    max-width: 175px;
    margin: 0 auto;
    background: #F6F5EC;
    border-radius: 10px;
    overflow: hidden;
  }

  .mobile-card-image-wrapper {
    position: relative;
    width: 100%;
    height: 231px;
    overflow: visible;
  }

  .mobile-card-image-wrapper::before {
    content: '';
    position: absolute;
    top: -5px;
    left: -3px;
    width: calc(100% + 6px);
    height: calc(100% + 10px);
    background: linear-gradient(180deg, rgba(0, 0, 0, 0.7) 7.68%, rgba(0, 0, 0, 0) 18.39%);
    z-index: 1;
    pointer-events: none;
  }

  .mobile-card-image {
    width: calc(100% + 6px);
    height: calc(100% + 10px);
    position: absolute;
    top: -5px;
    left: -3px;
    object-fit: cover;
    display: block;
  }

  .mobile-card-views {
    position: absolute;
    top: 8px;
    left: 8px;
    display: flex;
    align-items: center;
    gap: 4px;
    z-index: 2;
  }

  .mobile-card-views-count {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #F6F5EC;
  }

  .mobile-card-content {
    padding: 16px 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    width: 100%;
    box-sizing: border-box;
  }

  .mobile-card-prices {
    display: flex;
    align-items: baseline;
    gap: 8px;
    width: 100%;
    padding-left: 0;
  }

  .mobile-card-price-current {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
    width: 57px;
    height: 19px;
  }

  .mobile-card-price-old {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    text-decoration: line-through;
    width: auto;
    height: auto;
  }

  .mobile-card-price-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 10px;
    line-height: 100%;
    letter-spacing: 0;
    color: #640000;
    width: auto;
    height: auto;
    padding-left: 0;
  }

  .mobile-card-description {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: auto;
    height: auto;
    padding-left: 0;
  }

  .mobile-card-add-to-cart-button {
    width: 100%;
    max-width: 175px;
    height: 31px;
    border-radius: 10px;
    padding: 8px 24px;
    background: #640000;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin: 8px auto 0;
    align-self: center;
    box-sizing: border-box;
  }

  .mobile-card-cart-icon {
    width: 12px;
    height: 12px;
    display: block;
  }

  .mobile-card-cart-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: 0;
    color: #F6F5EC;
    white-space: nowrap;
  }

  /* Меню действий над нижней панелью */
  .mobile-actions-menu {
    position: fixed;
    bottom: 64px;
    left: 0;
    right: 0;
    width: 100%;
    max-width: 100%;
    height: 118px;
    padding: 16px;
    gap: 8px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background: #F6F5EC;
    box-shadow: 0px -4px 8px 0px #1B171640;
    display: flex;
    flex-direction: column;
    z-index: 999;
    box-sizing: border-box;
  }

  .mobile-actions-row {
    display: flex;
    gap: 8px;
    width: 100%;
  }

  .mobile-action-button {
    border-radius: 10px;
    padding: 8px 24px;
    gap: 8px;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  .mobile-buy-now-button {
    flex: 1;
    height: 35px;
    background: #1B171699;
    min-width: 0;
  }

  .mobile-add-to-cart-button {
    flex: 1;
    height: 35px;
    background: #640000;
    min-width: 0;
  }

  .mobile-ask-question-button {
    width: 100%;
    height: 35px;
    background: #F6F5EC;
    border: 2px solid #1B1716;
  }

  .mobile-action-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: 0%;
    white-space: nowrap;
  }

  .mobile-buy-now-button .mobile-action-text,
  .mobile-add-to-cart-button .mobile-action-text {
    color: #F6F5EC;
  }

  .mobile-ask-question-button .mobile-action-text {
    color: #1B1716;
  }

  /* Адаптация для очень маленьких экранов (до 300px) */
  @media (max-width: 300px) {
    .mobile-product {
      padding: 0 8px;
    }

    .mobile-photo-item {
      width: calc(100vw - 32px);
      max-width: 284px;
      height: calc(100vw - 32px);
      max-height: 284px;
    }

    .mobile-product-title {
      font-size: 14px;
    }

    .mobile-price-value {
      font-size: 20px;
    }

    .mobile-price-label,
    .mobile-boutique-price-label {
      font-size: 14px;
    }

    .mobile-recommended-section {
      padding: 0 8px;
    }

    .mobile-recommended-products {
      gap: 6px;
    }

    .mobile-actions-menu {
      padding: 12px;
    }

    .mobile-action-button {
      padding: 8px 16px;
      font-size: 14px;
    }

    .mobile-buy-now-button,
    .mobile-add-to-cart-button {
      flex: 1;
      min-width: 0;
    }

    .mobile-ask-question-button {
      width: 100%;
    }

    .mobile-action-text {
      font-size: 14px;
    }
  }
}

/* Явно показываем десктопную версию на экранах от 1280px (даже при масштабировании) */
@media (min-width: 1280px) {
  .mobile-product {
    display: none !important;
  }

  .desktop-product {
    display: block !important;
  }
}

/* Скрываем мобильную версию на планшетах и десктопе (до 1280px тоже) */
@media (min-width: 551px) and (max-width: 1279px) {
  .mobile-product {
    display: none;
  }
}

/* Скрываем десктопную версию на мобильных */
@media (max-width: 550px) {
  .desktop-product {
    display: none;
  }
}
</style>

