<template>
  <div class="cart-page">
    <div class="cart-content">
      <div class="cart-header">
        <div class="breadcrumbs">
          <router-link to="/" class="breadcrumb-item breadcrumb-first">Каталог</router-link>
          <span class="breadcrumb-slash">/</span>
          <span class="breadcrumb-item breadcrumb-active">Корзина</span>
        </div>
        <div class="cart-summary-header">
          <span class="total-label">Сумма:</span>
          <span class="total-value">5650 ₽</span>
          <span class="items-count">3 товара</span>
          <span class="items-separator"> • </span>
          <span class="items-unavailable">1 недоступен</span>
        </div>
      </div>
      
      <div class="table-headers-wrapper">
        <div class="table-header header-name">Название</div>
        <div class="table-header header-quantity">Количество</div>
        <div class="table-header header-price">Цена</div>
        <div class="table-header header-article">Артикул</div>
      </div>
      
      <div class="cart-items">
        <div class="cart-item">
          <div class="item-name-cell">
            <button class="delete-button" type="button">
              <img :src="deleteIcon" alt="Удалить" class="delete-icon" />
            </button>
            <div class="item-image"></div>
            <div class="item-name-text">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</div>
          </div>
          <div class="item-quantity-cell">
            <div class="quantity-controls">
              <button class="quantity-button">-</button>
              <span class="quantity-value">2</span>
              <button class="quantity-button">+</button>
            </div>
          </div>
          <div class="item-price-cell">3650 ₽</div>
          <div class="item-article-cell">DH20 270</div>
        </div>
        <div class="cart-item">
          <div class="item-name-cell">
            <button class="delete-button" type="button">
              <img :src="deleteIcon" alt="Удалить" class="delete-icon" />
            </button>
            <div class="item-image"></div>
            <div class="item-name-text">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</div>
          </div>
          <div class="item-quantity-cell">
            <div class="quantity-controls">
              <button class="quantity-button">-</button>
              <span class="quantity-value">1</span>
              <button class="quantity-button">+</button>
            </div>
          </div>
          <div class="item-price-cell">3650 ₽</div>
          <div class="item-article-cell">DH20 270</div>
        </div>
        <div class="cart-item unavailable-item">
          <div class="item-name-cell">
            <button class="similar-button" type="button">
              <span class="similar-button-text">Похожее</span>
            </button>
            <div class="item-image-wrapper">
              <div class="item-image unavailable-image"></div>
              <div class="sold-badge">ПРОДАН</div>
            </div>
            <div class="item-name-text">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</div>
          </div>
          <div class="item-quantity-cell">
            <div class="quantity-controls disabled-quantity">
              <span class="quantity-value">0</span>
            </div>
          </div>
          <div class="item-price-cell">0 ₽</div>
          <div class="item-article-cell">DH20 270</div>
        </div>
      </div>
      <div class="checkout-section">
        <button class="checkout-button" type="button" @click="goToCheckout">
          Перейти к оформлению
        </button>
        <div class="checkout-warning">
          <span class="warning-bold">ВНИМАНИЕ!</span> При переходе к оформлению заказа товары будут зарезервированы за Вами на 30 минут. Если заказ не оплачен, то он будет отменен.
        </div>
      </div>
      <div class="recommended-section">
        <h2 class="recommended-title">Рекомендуем</h2>
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
      
      <!-- Мобильная версия корзины -->
      <div class="mobile-cart">
        <!-- Заголовок с суммой -->
        <div class="mobile-cart-header">
          <div class="mobile-cart-summary">
            <span class="mobile-summary-label">Сумма:</span>
            <span class="mobile-summary-value">5650 ₽</span>
            <span class="mobile-items-count">3 товара</span>
            <span class="mobile-items-dot"></span>
            <span class="mobile-items-unavailable">1 недоступен</span>
          </div>
        </div>
        
        <!-- Товары в корзине -->
        <div class="mobile-cart-items">
          <!-- Первый товар -->
          <div class="mobile-cart-item">
            <div class="mobile-item-image-placeholder"></div>
            <div class="mobile-item-info">
              <div class="mobile-item-header">
                <h3 class="mobile-item-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Пол...</h3>
                <button class="mobile-item-delete" type="button">
                  <img :src="deleteIcon" alt="Удалить" class="mobile-delete-icon" />
                </button>
              </div>
              <div class="mobile-item-price-row">
                <span class="mobile-price-label">Цена:</span>
                <span class="mobile-item-price">5650 ₽</span>
              </div>
              <div class="mobile-item-article-row">
                <span class="mobile-article-label">Артикул:</span>
                <span class="mobile-item-article">GH20 270</span>
                <button class="mobile-copy-button" type="button">
                  <img :src="copyIconSvg" alt="Копировать" class="mobile-copy-icon" />
                </button>
              </div>
              <div class="mobile-item-quantity">
                <button class="mobile-quantity-button mobile-quantity-minus"></button>
                <span class="mobile-quantity-value">2</span>
                <button class="mobile-quantity-button mobile-quantity-plus"></button>
              </div>
            </div>
          </div>
          
          <!-- Второй товар -->
          <div class="mobile-cart-item">
            <div class="mobile-item-image-placeholder"></div>
            <div class="mobile-item-info">
              <div class="mobile-item-header">
                <h3 class="mobile-item-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Пол...</h3>
                <button class="mobile-item-delete" type="button">
                  <img :src="deleteIcon" alt="Удалить" class="mobile-delete-icon" />
                </button>
              </div>
              <div class="mobile-item-price-row">
                <span class="mobile-price-label">Цена:</span>
                <span class="mobile-item-price">5650 ₽</span>
              </div>
              <div class="mobile-item-article-row">
                <span class="mobile-article-label">Артикул:</span>
                <span class="mobile-item-article">GH20 270</span>
                <button class="mobile-copy-button" type="button">
                  <img :src="copyIconSvg" alt="Копировать" class="mobile-copy-icon" />
                </button>
              </div>
              <div class="mobile-item-quantity">
                <button class="mobile-quantity-button mobile-quantity-minus"></button>
                <span class="mobile-quantity-value">1</span>
                <button class="mobile-quantity-button mobile-quantity-plus"></button>
              </div>
            </div>
          </div>
          
          <!-- Третий товар (ПРОДАН) -->
          <div class="mobile-cart-item mobile-cart-item-unavailable">
            <div class="mobile-item-image-section">
              <div class="mobile-item-image-wrapper">
                <div class="mobile-item-image-placeholder mobile-item-image-unavailable"></div>
                <div class="mobile-sold-badge">ПРОДАН</div>
              </div>
              <button class="mobile-similar-button" type="button">
                <span class="mobile-similar-button-text">Похожее</span>
              </button>
            </div>
            <div class="mobile-item-info">
              <div class="mobile-item-header">
                <h3 class="mobile-item-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Пол...</h3>
                <button class="mobile-item-delete" type="button">
                  <img :src="deleteIcon" alt="Удалить" class="mobile-delete-icon" />
                </button>
              </div>
              <div class="mobile-item-price-row">
                <span class="mobile-price-label">Цена:</span>
                <span class="mobile-item-price">0 ₽</span>
              </div>
              <div class="mobile-item-article-row">
                <span class="mobile-article-label">Артикул:</span>
                <span class="mobile-item-article">GH20 270</span>
                <button class="mobile-copy-button" type="button">
                  <img :src="copyIconSvg" alt="Копировать" class="mobile-copy-icon" />
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Предупреждение -->
        <div class="mobile-checkout-warning">
          <span class="mobile-warning-bold">ВНИМАНИЕ!</span> При переходе к оформлению заказа товары будут зарезервированы за Вами на 30 минут. Если заказ не оплачен, то он будет отменен.
        </div>
        
        <!-- Рекомендуем -->
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
        
        <!-- Меню действий над нижней панелью -->
        <div class="mobile-cart-actions-menu">
          <button class="mobile-checkout-button" type="button" @click="goToCheckout">
            <span class="mobile-checkout-text">Перейти к оформлению</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import deleteIcon from '@/assets/images/icon-delete.svg'
import exampleImg from '@/assets/images/example.png'
import cardViewsSvg from '@/assets/images/icon-views-card.svg'
import cartIconSvg from '@/assets/images/icon-cart-button.svg'
import copyIconSvg from '@/assets/images/icon-copy.svg'

const router = useRouter()

const goToCheckout = () => {
  router.push('/checkout')
}
</script>

<style scoped>
.cart-page {
  width: 100%;
  min-height: 100%;
  background-color: #F6F5EC;
}

.cart-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 0 32px;
  box-sizing: border-box;
}

.cart-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.breadcrumbs {
  display: flex;
  align-items: center;
  gap: 8px;
}

.breadcrumb-item {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  text-decoration: none;
  height: 24px;
  display: flex;
  align-items: center;
}

.breadcrumb-first {
  width: 77px;
  opacity: 0.6;
}

.breadcrumb-active {
  width: 80px;
  opacity: 1;
}

.breadcrumb-slash {
  width: 8px;
  height: 24px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cart-summary-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.total-label {
  width: 73px;
  height: 24px;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  display: flex;
  align-items: center;
}

.total-value {
  width: 71px;
  height: 24px;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #640000;
  opacity: 1;
  display: flex;
  align-items: center;
}


.items-count {
  width: 68px;
  height: 19px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
  display: flex;
  align-items: center;
}

.items-separator {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
}

.items-unavailable {
  width: 103px;
  height: 19px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #640000;
  opacity: 1;
  display: flex;
  align-items: center;
}

.table-headers-wrapper {
  width: 100%;
  padding: 0 32px;
  box-sizing: border-box;
  margin-top: 24px;
  display: grid;
  grid-template-columns: 1fr 150px 120px 120px;
  gap: 40px;
  align-items: center;
}

.table-header {
  height: 19px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
  display: flex;
  align-items: center;
}

.header-name {
  opacity: 1;
  padding-left: 360px;
}

.header-quantity {
  justify-content: center;
}

.header-price {
  justify-content: center;
}

.header-article {
  justify-content: flex-end;
}

.cart-items {
  width: 100%;
  box-sizing: border-box;
  margin-top: 16px;
}

.cart-item {
  display: grid;
  grid-template-columns: 1fr 150px 120px 120px;
  gap: 40px;
  align-items: flex-start;
  margin-bottom: 24px;
  padding: 0 32px;
  box-sizing: border-box;
}

.item-name-cell {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  position: relative;
  padding-left: 75px;
}

.delete-button {
  width: 27px;
  height: 32px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 37.5px;
  position: absolute;
  left: 0;
}

.delete-icon {
  width: 27px;
  height: 32px;
  display: block;
}

.item-image {
  width: 107px;
  height: 107px;
  border-radius: 10px;
  background: #D9D9D9;
  opacity: 1;
  flex-shrink: 0;
}

.item-name-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  display: flex;
  align-items: center;
  flex: 1;
  margin-left: 8px;
}

.item-quantity-cell {
  width: 108px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.quantity-controls {
  width: 108px;
  height: 40px;
  border-radius: 8px;
  padding: 8px;
  background: rgba(27, 23, 22, 0.1);
  opacity: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}

.quantity-button {
  width: 24px;
  height: 24px;
  background: none;
  border: none;
  color: #1B1716;
  font-size: 20px;
  font-weight: 400;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

.quantity-value {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
}

.item-price-cell {
  height: 24px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-article-cell {
  height: 24px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.similar-button {
  width: 107px;
  height: 35px;
  border-radius: 10px;
  padding: 8px 24px;
  background: rgba(27, 23, 22, 0.6);
  opacity: 1;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 36px;
  position: absolute;
  left: -45px;
  box-sizing: border-box;
}

.similar-button-text {
  width: 70px;
  height: 19px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0%;
  color: #F6F5EC;
  opacity: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-image-wrapper {
  position: relative;
  flex-shrink: 0;
}

.unavailable-image {
  width: 107px;
  height: 107px;
  border-radius: 10px;
  padding: 10px;
  background: rgba(27, 23, 22, 0.1);
  opacity: 1;
  box-sizing: border-box;
  flex-shrink: 0;
}

.sold-badge {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 71px;
  height: 19px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-transform: uppercase;
  color: #640000;
  background: transparent;
  opacity: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.disabled-quantity {
  justify-content: center;
  cursor: not-allowed;
  width: 108px;
  height: 40px;
}

.disabled-quantity .quantity-button {
  display: none;
}

.disabled-quantity .quantity-value {
  margin: 0;
}

.empty-cart,
.loading-cart {
  width: 100%;
  padding: 40px;
  text-align: center;
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  color: #1B1716;
  opacity: 0.6;
}

.empty-cart-mobile,
.loading-cart-mobile {
  width: 100%;
  padding: 40px 16px;
  text-align: center;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  color: #1B1716;
  opacity: 0.6;
}

.checkout-section {
  width: 100%;
  padding: 40px 20px 60px 32px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.checkout-button {
  width: 476px;
  height: 35px;
  border-radius: 10px;
  padding: 8px 24px;
  background: #640000;
  border: none;
  color: #F6F5EC;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-sizing: border-box;
  transition: background-color 0.2s ease, opacity 0.2s ease;
}

.checkout-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

.checkout-warning {
  width: 100%;
  max-width: 800px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
  background: transparent;
  padding: 16px;
  border-radius: 10px;
  box-sizing: border-box;
}

.warning-bold {
  font-weight: 700;
  font-style: normal;
  color: #640000;
}

.recommended-section {
  width: 100%;
  max-width: 100%;
  padding: 0px 20px 60px 30px;
  box-sizing: border-box;
  overflow-x: hidden;
  position: relative;
}

.recommended-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 24px -16px;
  padding: 0;
  width: 243px;
  height: 29px;
  opacity: 1;
}

.recommended-products {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 236px));
  gap: 16px;
  justify-content: center;
  max-width: 100%;
  overflow-x: hidden;
  width: 100%;
}

.recommended-card {
  width: 236px;
  max-width: 100%;
  background: #F6F5EC;
  border-radius: 10px;
  overflow: hidden;
  opacity: 1;
  flex-shrink: 0;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 287px;
  overflow: hidden;
  border-radius: 10px 10px 0 0;
}

.card-image-wrapper::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50%;
  background: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.3));
  pointer-events: none;
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
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
  box-sizing: border-box;
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
  width: 100%;
  max-width: 230px;
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
  box-sizing: border-box;
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
  letter-spacing: 0;
  color: #F6F5EC;
  opacity: 1;
  width: 78px;
  height: 19px;
}

/* Скрываем мобильную версию на десктопе */
.mobile-cart {
  display: none;
}

/* Показываем мобильную версию только на мобильных устройствах */
@media (min-width: 551px) and (max-width: 1279px) {
  .mobile-cart {
    display: none !important;
  }
}

/* Адаптация сетки рекомендаций для разных размеров экрана */
@media (max-width: 1400px) {
  .recommended-products {
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 12px;
  }
  
  .recommended-card {
    width: 100%;
    max-width: 236px;
  }
}

@media (max-width: 1200px) {
  .recommended-products {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

/* Явно показываем десктопную версию на экранах от 1280px (даже при масштабировании) */
@media (min-width: 1280px) {
  .mobile-cart {
    display: none !important;
  }

  .cart-header,
  .table-headers-wrapper,
  .cart-items,
  .checkout-section,
  .recommended-section {
    display: flex;
  }
}

/* Мобильная версия корзины */
@media (max-width: 550px) {
  .cart-header,
  .table-headers-wrapper,
  .cart-items,
  .checkout-section,
  .recommended-section {
    display: none;
  }

  .mobile-cart {
    display: block;
  }

  .cart-content {
    padding: 0;
    min-height: 100vh;
    padding-top: 0;
    padding-bottom: 131px; /* 67px (меню действий) + 64px (нижняя панель) */
    overflow: visible;
    margin-top: 0;
    box-sizing: border-box;
  }

  .mobile-cart {
    padding: 16px;
    padding-top: 16px;
    padding-bottom: 0;
    margin-top: 0;
    overflow: visible;
    box-sizing: border-box;
  }

  /* Заголовок с суммой */
  .mobile-cart-header {
    margin-bottom: 16px;
    padding-top: 16px;
  }

  .mobile-cart-summary {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }

  .mobile-summary-label {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: 73px;
    height: 24px;
  }

  .mobile-summary-value {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
    width: 71px;
    height: 24px;
  }

  .mobile-items-count {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    width: 68px;
    height: 19px;
  }

  .mobile-items-dot {
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: #73706C;
    flex-shrink: 0;
  }

  .mobile-items-unavailable {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
    width: 103px;
    height: 19px;
  }

  /* Товары в корзине */
  .mobile-cart-items {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .mobile-cart-item {
    display: flex;
    gap: 16px;
    align-items: flex-start;
  }

  .mobile-item-image-placeholder {
    width: 128px;
    height: 128px;
    border-radius: 10px;
    background: #CACACA;
    flex-shrink: 0;
  }

  .mobile-item-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .mobile-item-header {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    justify-content: space-between;
  }

  .mobile-item-title {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: 174px;
    height: 58px;
    margin: 0;
    padding: 0;
  }

  .mobile-item-delete {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    flex-shrink: 0;
  }

  .mobile-delete-icon {
    width: 20px;
    height: 20px;
    display: block;
  }

  .mobile-item-price-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-price-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    width: 44px;
    height: 19px;
  }

  .mobile-item-price {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
  }

  .mobile-item-article-row {
    display: flex;
    align-items: center;
    gap: 8px;
    white-space: nowrap;
    flex-wrap: nowrap;
  }

  .mobile-article-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    height: 17px;
    white-space: nowrap;
    flex-shrink: 0;
  }

  .mobile-item-article {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    height: 17px;
    white-space: nowrap;
    flex-shrink: 0;
  }

  .mobile-copy-button {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mobile-copy-icon {
    width: 16px;
    height: 16px;
    display: block;
  }

  /* Селектор количества */
  .mobile-item-quantity {
    width: 124px;
    height: 32px;
    border-radius: 8px;
    padding: 4px 8px;
    background: #1B17161A;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
  }

  .mobile-quantity-button {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mobile-quantity-minus {
    width: 16px;
    height: 3px;
    background: #1B1716;
    opacity: 1;
    border-radius: 0;
    position: relative;
    border: none;
  }

  .mobile-quantity-minus::after {
    content: '';
    display: none;
  }

  .mobile-quantity-plus {
    width: 16px;
    height: 16px;
    background: transparent;
    opacity: 1;
    border-radius: 0;
    position: relative;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mobile-quantity-plus::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    width: 16px;
    height: 2px;
    background: #1B171699;
  }

  .mobile-quantity-plus::after {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    width: 2px;
    height: 16px;
    background: #1B171699;
  }

  .mobile-quantity-value {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: 13px;
    height: 24px;
  }

  /* Проданный товар - opacity убран, чтобы товар не был мутным */

  .mobile-item-image-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }

  .mobile-item-image-wrapper {
    position: relative;
    width: 128px;
    height: 128px;
    flex-shrink: 0;
  }

  .mobile-item-image-unavailable {
    opacity: 0.5;
  }

  .mobile-sold-badge {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 71px;
    height: 19px;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    text-transform: uppercase;
    color: #640000;
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
  }

  .mobile-similar-button {
    width: 107px;
    height: 35px;
    border-radius: 10px;
    padding: 8px 24px;
    background: rgba(27, 23, 22, 0.6);
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  .mobile-similar-button-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #F6F5EC;
  }

  /* Предупреждение */
  .mobile-checkout-warning {
    width: 100%;
    padding: 16px;
    box-sizing: border-box;
    text-align: center;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-warning-bold {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    text-align: center;
    color: #640000;
  }

  /* Рекомендуем */
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
    margin: 0 0 24px 0;
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
  .mobile-cart-actions-menu {
    position: fixed;
    bottom: 64px;
    left: 0;
    right: 0;
    width: 100%;
    height: 67px;
    padding: 16px;
    gap: 8px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background: #F6F5EC;
    box-shadow: 0px -4px 8px 0px #1B171640;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 999;
    box-sizing: border-box;
  }

  .mobile-checkout-button {
    width: 100%;
    max-width: 100%;
    height: 35px;
    border-radius: 10px;
    padding: 8px 24px;
    background: #640000;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  .mobile-checkout-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: 0%;
    color: #F6F5EC;
    width: 187px;
    height: 19px;
    white-space: nowrap;
  }

  /* Адаптация для очень маленьких экранов (до 300px) */
  @media (max-width: 300px) {
    .mobile-cart {
      padding: 8px;
      padding-top: 8px;
    }

    .mobile-cart-header {
      margin-bottom: 12px;
      padding-top: 8px;
    }

    .mobile-summary-label,
    .mobile-summary-value {
      font-size: 18px;
    }

    .mobile-items-count,
    .mobile-items-unavailable {
      font-size: 14px;
    }

    .mobile-cart-items {
      gap: 12px;
    }

    .mobile-cart-item {
      gap: 12px;
    }

    .mobile-item-image-placeholder,
    .mobile-item-image-wrapper {
      width: 100px;
      height: 100px;
    }

    .mobile-item-image-section {
      width: 100px;
    }

    .mobile-similar-button {
      width: 100px;
    }

    .mobile-item-title {
      font-size: 12px;
      width: auto;
      height: auto;
    }

    .mobile-price-label {
      font-size: 14px;
    }

    .mobile-item-price {
      font-size: 18px;
    }

    .mobile-article-label,
    .mobile-item-article {
      font-size: 12px;
    }

    .mobile-item-quantity {
      width: 100px;
      height: 28px;
    }

    .mobile-quantity-value {
      font-size: 18px;
    }

    .mobile-checkout-warning {
      padding: 12px;
      font-size: 14px;
    }

    .mobile-warning-bold {
      font-size: 14px;
    }

    .mobile-recommended-section {
      margin-top: 40px;
      margin-bottom: 30px;
      padding: 0 8px;
    }

    .mobile-recommended-title {
      font-size: 14px;
      margin-bottom: 16px;
    }

    .mobile-recommended-products {
      gap: 6px;
    }

    .mobile-recommended-card {
      max-width: 140px;
    }

    .mobile-card-image-wrapper {
      max-width: 140px;
      height: 180px;
    }

    .mobile-card-content {
      padding: 12px 0;
    }

    .mobile-card-price-current {
      font-size: 14px;
    }

    .mobile-card-price-old {
      font-size: 10px;
    }

    .mobile-card-price-label {
      font-size: 9px;
    }

    .mobile-card-description {
      font-size: 10px;
    }

    .mobile-card-add-to-cart-button {
      max-width: 140px;
      height: 28px;
      padding: 6px 16px;
    }

    .mobile-card-cart-text {
      font-size: 11px;
    }

    .mobile-cart-actions-menu {
      padding: 12px 8px;
      height: 60px;
    }

    .mobile-checkout-button {
      height: 32px;
      padding: 6px 16px;
    }

    .mobile-checkout-text {
      font-size: 14px;
      width: auto;
    }
  }
}
</style>