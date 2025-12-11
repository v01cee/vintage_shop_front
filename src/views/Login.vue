<template>
  <div class="login-page">
    <div class="login-content">
      <div class="login-message">
        <h1 class="login-title">Вы не авторизованы</h1>
        <p class="login-text">
          Для доступа к личному кабинету необходимо <span class="login-link">войти</span>
        </p>
        <button class="login-button" @click="openLoginModal">Войти</button>
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

    <!-- Модальное окно входа/регистрации -->
    <LoginModal 
      :is-open="isLoginModalOpen" 
      @close="closeLoginModal"
      @login="handleLogin"
      @register="handleRegister"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LoginModal from '@/components/Auth/LoginModal.vue'
import exampleImg from '../../пример.png'
import cardViewsSvg from '../../значок просмотры на карточке .svg'
import cartIconSvg from '../../значок корзины на кнопке в корзину.svg'

const isLoginModalOpen = ref(false)

const openLoginModal = () => {
  // Открываем модальное окно на всех устройствах
  isLoginModalOpen.value = true
}

const closeLoginModal = () => {
  isLoginModalOpen.value = false
}

const handleLogin = (credentials) => {
  console.log('Login attempt:', credentials)
  // TODO: Реализовать логику входа
  closeLoginModal()
}

const handleRegister = (data) => {
  console.log('Register attempt:', data)
  // TODO: Реализовать логику регистрации
  closeLoginModal()
}
</script>

<style lang="scss" scoped>
@use '@/assets/styles/breakpoints' as *;

.login-page {
  width: 100%;
  min-height: calc(100vh - 224px);
  background: #F6F5EC;
}

.login-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 180px 32px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-message {
  text-align: center;
  margin: 80px 0 80px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 16px 0;
  padding: 0;
}

.login-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
  margin: 0;
  padding: 0;
}

.login-link {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #640000;
}

.login-button {
  width: 230px;
  height: 48px;
  border-radius: 10px;
  padding: 12px 24px;
  background: #640000;
  border: none;
  cursor: pointer;
  margin-top: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: 0%;
  color: #F6F5EC;
  opacity: 1;
  transition: background-color 0.2s ease, opacity 0.2s ease;
  box-sizing: border-box;
}

.login-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

.recommended-section {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 40px 20px 180px 32px;
  box-sizing: border-box;
}

/* Мобильная версия страницы логина */
@media (max-width: 1279px) {
  .is-mobile-device .login-content {
    padding: 16px;
    padding-bottom: 182px; /* Отступ для нижней навигационной панели и action menu */
  }

  .is-mobile-device .login-message {
    margin: 40px 0 40px 0;
  }

  .is-mobile-device .login-title {
    font-size: 18px;
    margin-bottom: 12px;
  }

  .is-mobile-device .login-text {
    font-size: 16px;
  }

  .is-mobile-device .login-button {
    width: 100%;
    max-width: 230px;
    height: 48px;
    font-size: 16px;
    margin-top: 20px;
  }
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
  white-space: nowrap;
}

.recommended-products {
  display: grid;
  grid-template-columns: repeat(5, 236px);
  gap: 16px;
  justify-content: center;
}

.recommended-card {
  width: 236px;
  background: #F6F5EC;
  border-radius: 10px;
  overflow: hidden;
  opacity: 1;
  flex-shrink: 0;
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
  white-space: nowrap;
}

/* Десктопная версия - всегда показываем десктопные стили */
@include desktop {
  .recommended-section {
    padding: 40px 20px 180px 32px;
  }

  .recommended-products {
    grid-template-columns: repeat(5, 236px);
    gap: 16px;
    justify-content: center;
  }
}

/* Для десктопных устройств всегда применяем десктопные стили даже при масштабировании */
.is-desktop-device .recommended-section {
  padding: 40px 20px 180px 32px !important;
}

.is-desktop-device .recommended-products {
  grid-template-columns: repeat(5, 236px) !important;
  gap: 16px !important;
  justify-content: center !important;
}

.is-desktop-device .recommended-card {
  width: 236px !important;
}

.is-desktop-device .card-image-wrapper {
  height: 287px !important;
}

.is-desktop-device .card-add-to-cart-button {
  width: 230px !important;
  height: 35px !important;
}

/* Мобильная адаптация для секции "Рекомендуем" */
@media (max-width: 1279px) {
  .is-mobile-device .recommended-section {
    margin-top: 60px;
    margin-bottom: 40px;
    padding: 0 16px;
    box-sizing: border-box;
  }

  .is-mobile-device .recommended-title {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    width: auto;
    height: auto;
    margin: 0 0 24px 0;
    padding: 0;
    white-space: nowrap;
  }

  .is-mobile-device .recommended-products {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    width: 100%;
    box-sizing: border-box;
  }

  .is-mobile-device .recommended-card {
    width: 100%;
    max-width: 175px;
    margin: 0 auto;
    background: #F6F5EC;
    border-radius: 10px;
    overflow: hidden;
  }

  .is-mobile-device .card-image-wrapper {
    position: relative;
    width: 100%;
    max-width: 175px;
    height: 231px;
    overflow: hidden;
    margin: 0 auto;
  }

  .is-mobile-device .card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .is-mobile-device .card-views {
    position: absolute;
    top: 8px;
    left: 8px;
    display: flex;
    align-items: center;
    gap: 4px;
    z-index: 2;
  }

  .is-mobile-device .card-views-count {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #F6F5EC;
  }

  .is-mobile-device .card-content {
    padding: 16px 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    width: 100%;
    box-sizing: border-box;
  }

  .is-mobile-device .card-prices {
    display: flex;
    align-items: baseline;
    gap: 8px;
    width: 100%;
    padding-left: 0;
  }

  .is-mobile-device .card-price-current {
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

  .is-mobile-device .card-price-old {
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

  .is-mobile-device .card-price-label {
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

  .is-mobile-device .card-description {
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
    text-align: left;
  }

  .is-mobile-device .card-add-to-cart-button {
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

  .is-mobile-device .card-cart-icon {
    width: 12px;
    height: 12px;
    display: block;
  }

  .is-mobile-device .card-cart-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: 0;
    color: #F6F5EC;
    white-space: nowrap;
  }
}

/* Адаптация для очень маленьких экранов (до 300px) */
@media (max-width: 300px) {
  .is-mobile-device .login-message {
    margin: 30px 0 30px 0;
  }

  .is-mobile-device .login-title {
    font-size: 16px;
    margin-bottom: 10px;
  }

  .is-mobile-device .login-text {
    font-size: 14px;
  }

  .is-mobile-device .login-link {
    font-size: 14px;
  }

  .is-mobile-device .recommended-section {
    padding: 0 8px;
  }

  .is-mobile-device .recommended-products {
    gap: 6px;
  }

  .is-mobile-device .recommended-title {
    font-size: 14px;
    margin-bottom: 20px;
    white-space: nowrap;
  }
}
</style>

