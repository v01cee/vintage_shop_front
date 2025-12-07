<template>
  <div class="checkout-page">
    <!-- Десктопная версия -->
    <div class="checkout-content desktop-checkout">
      <div class="breadcrumbs">
        <router-link to="/" class="breadcrumb-item breadcrumb-first">Каталог</router-link>
        <span class="breadcrumb-slash">/</span>
        <router-link to="/cart" class="breadcrumb-item breadcrumb-second">Корзина</router-link>
        <span class="breadcrumb-slash">/</span>
        <span class="breadcrumb-item breadcrumb-active">Оформление заказа</span>
      </div>

      <div class="order-items-section">
        <div class="table-headers-wrapper">
          <div class="table-header header-name">Название</div>
          <div class="table-header header-quantity">Количество</div>
          <div class="table-header header-price">Цена</div>
          <div class="table-header header-article">Артикул</div>
        </div>
        <div class="order-items-list">
          <div class="order-item">
            <div class="order-item-name-cell">
              <div class="order-item-image"></div>
              <div class="order-item-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</div>
            </div>
            <div class="order-item-quantity-cell">
              <div class="order-item-quantity">
                <button class="quantity-button quantity-button-minus"></button>
                <span class="quantity-value">2</span>
                <button class="quantity-button quantity-button-plus"></button>
              </div>
            </div>
            <div class="order-item-price-cell">3650 ₽</div>
            <div class="order-item-article-cell">DH20 270</div>
          </div>
          <div class="order-item">
            <div class="order-item-name-cell">
              <div class="order-item-image"></div>
              <div class="order-item-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</div>
            </div>
            <div class="order-item-quantity-cell">
              <div class="order-item-quantity">
                <button class="quantity-button quantity-button-minus"></button>
                <span class="quantity-value">1</span>
                <button class="quantity-button quantity-button-plus"></button>
              </div>
            </div>
            <div class="order-item-price-cell">3650 ₽</div>
            <div class="order-item-article-cell">DH20 270</div>
          </div>
          <div class="order-delivery-item">
            <div class="delivery-label">Доставка</div>
            <div class="delivery-quantity"></div>
            <div class="delivery-price">600 ₽</div>
            <div class="delivery-article"></div>
          </div>
        </div>
      </div>

      <div class="checkout-main">
        <div class="order-info-section">
          <div class="info-item">
            <span class="info-label">Заказ №:</span>
            <div class="info-value-container">
              <span class="info-value">111114532</span>
              <button class="copy-button" type="button">
                <img :src="copyIconSvg" alt="Копировать" class="copy-icon" />
              </button>
            </div>
          </div>
          <div class="info-item">
            <span class="info-label">Дата:</span>
            <span class="info-value">13.02.2025</span>
          </div>
          <div class="info-item">
            <span class="info-label">Статус:</span>
            <span class="info-value">Новый</span>
          </div>
          <div class="info-item">
            <span class="info-label">Всего:</span>
            <span class="info-value"><span class="info-value-bold">3</span> товара</span>
          </div>
          <div class="info-item">
            <span class="info-label">Сумма:</span>
            <span class="info-value"><span class="info-value-bold">6250</span> рублей</span>
          </div>
          <div class="info-item">
            <span class="info-label">Трек:</span>
            <div class="info-value-container">
              <span class="info-value">8665 11 00 1347 2</span>
              <button class="copy-button" type="button">
                <img :src="copyIconSvg" alt="Копировать" class="copy-icon" />
              </button>
            </div>
          </div>
        </div>

        <div class="delivery-section">
          <h3 class="delivery-section-title">Данные для доставки</h3>
          <div class="form-group">
            <label class="form-label">ФИО*</label>
            <input type="text" class="form-input" placeholder="Иванов Иван Иванович" />
          </div>
          <div class="form-group">
            <label class="form-label">Адрес*</label>
            <input type="text" class="form-input" placeholder="Город, почтовый индекс, улица, дом, квартира" />
          </div>
          <div class="form-group">
            <label class="form-label">Телефон*</label>
            <input type="text" class="form-input" placeholder="X XXX XXX-XX-XX" />
          </div>
          <div class="form-group">
            <label class="form-label">Служба доставки</label>
            <select class="form-select">
              <option>Почта РФ</option>
            </select>
          </div>
        </div>
      </div>
      
      <div class="comments-section">
        <h3 class="comments-title">Комментарии к заказу</h3>
        <div class="comments-display">
          <div class="comment-item comment-user">
            <span class="comment-author">Вы:</span>
            <span class="comment-text">Упакуйте в коробку!</span>
          </div>
          <div class="comment-item comment-seller">
            <span class="comment-author">Продавец:</span>
            <span class="comment-text">Всегда упаковываем в коробках</span>
          </div>
        </div>
        <div class="comment-input-wrapper">
          <input 
            type="text" 
            class="comment-input" 
            placeholder="Добавить комментарий к заказу"
          />
          <button class="send-comment-button" type="button">
            Отправить
          </button>
        </div>
      </div>
      
      <div class="payment-section">
        <button class="pay-button" type="button">
          Оплатить
        </button>
        <div class="timer-warning">
          <span class="timer-label">Заказ будет отменен через:</span>
          <span class="timer-value">00:29:31</span>
        </div>
      </div>
    </div>
    
    <!-- Мобильная версия оформления заказа -->
    <div class="mobile-checkout">
      <!-- Кнопка назад -->
      <div class="mobile-checkout-back">
        <button class="mobile-back-button" type="button" @click="goBack">
          <div class="mobile-back-arrow"></div>
          <span class="mobile-back-text">К списку заказов</span>
        </button>
      </div>
      
      <!-- Информация о заказе -->
      <div class="mobile-checkout-info">
        <div class="mobile-checkout-info-item">
          <span class="mobile-checkout-info-label">Заказ №:</span>
          <div class="mobile-checkout-info-value-container">
            <span class="mobile-checkout-info-value">111114532</span>
            <button class="mobile-checkout-copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIconSvg" alt="Копировать" class="mobile-checkout-copy-icon" />
            </button>
          </div>
        </div>
        <div class="mobile-checkout-info-item">
          <span class="mobile-checkout-info-label">Дата:</span>
          <span class="mobile-checkout-info-value">13.02.2025</span>
        </div>
        <div class="mobile-checkout-info-item">
          <span class="mobile-checkout-info-label">Статус:</span>
          <span class="mobile-checkout-info-value">Новый</span>
        </div>
        <div class="mobile-checkout-info-item">
          <span class="mobile-checkout-info-label">Всего:</span>
          <span class="mobile-checkout-info-value"><span class="mobile-checkout-info-value-bold">3</span> товара</span>
        </div>
        <div class="mobile-checkout-info-item">
          <span class="mobile-checkout-info-label">Сумма:</span>
          <span class="mobile-checkout-info-value"><span class="mobile-checkout-info-value-bold">6250</span> рублей</span>
        </div>
        <div class="mobile-checkout-info-item">
          <span class="mobile-checkout-info-label">Трек:</span>
          <div class="mobile-checkout-info-value-container">
            <span class="mobile-checkout-info-value">8665 11 00 1347 2</span>
            <button class="mobile-checkout-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIconSvg" alt="Копировать" class="mobile-checkout-copy-icon" />
            </button>
          </div>
        </div>
      </div>
      
      <!-- Товары в заказе -->
      <div class="mobile-checkout-items">
        <!-- Первый товар -->
        <div class="mobile-checkout-item">
          <div class="mobile-checkout-item-image"></div>
          <div class="mobile-checkout-item-info">
            <div class="mobile-checkout-item-header">
              <h3 class="mobile-checkout-item-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</h3>
              <button class="mobile-checkout-item-delete" type="button">
                <img :src="deleteIcon" alt="Удалить" class="mobile-checkout-delete-icon" />
              </button>
            </div>
            <div class="mobile-checkout-item-price-row">
              <span class="mobile-checkout-price-label">Цена:</span>
              <span class="mobile-checkout-item-price">5650 ₽</span>
            </div>
            <div class="mobile-checkout-item-article-row">
              <span class="mobile-checkout-article-label">Артикул:</span>
              <span class="mobile-checkout-item-article">GH20 270</span>
              <button class="mobile-checkout-copy-button" type="button" @click="copyToClipboard('GH20 270')">
                <img :src="copyIconSvg" alt="Копировать" class="mobile-checkout-copy-icon" />
              </button>
            </div>
            <div class="mobile-checkout-item-quantity">
              <button class="mobile-checkout-quantity-button mobile-checkout-quantity-minus"></button>
              <span class="mobile-checkout-quantity-value">2</span>
              <button class="mobile-checkout-quantity-button mobile-checkout-quantity-plus"></button>
            </div>
          </div>
        </div>
        
        <!-- Второй товар -->
        <div class="mobile-checkout-item">
          <div class="mobile-checkout-item-image"></div>
          <div class="mobile-checkout-item-info">
            <div class="mobile-checkout-item-header">
              <h3 class="mobile-checkout-item-title">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</h3>
              <button class="mobile-checkout-item-delete" type="button">
                <img :src="deleteIcon" alt="Удалить" class="mobile-checkout-delete-icon" />
              </button>
            </div>
            <div class="mobile-checkout-item-price-row">
              <span class="mobile-checkout-price-label">Цена:</span>
              <span class="mobile-checkout-item-price">5650 ₽</span>
            </div>
            <div class="mobile-checkout-item-article-row">
              <span class="mobile-checkout-article-label">Артикул:</span>
              <span class="mobile-checkout-item-article">GH20 270</span>
              <button class="mobile-checkout-copy-button" type="button" @click="copyToClipboard('GH20 270')">
                <img :src="copyIconSvg" alt="Копировать" class="mobile-checkout-copy-icon" />
              </button>
            </div>
            <div class="mobile-checkout-item-quantity">
              <button class="mobile-checkout-quantity-button mobile-checkout-quantity-minus"></button>
              <span class="mobile-checkout-quantity-value">1</span>
              <button class="mobile-checkout-quantity-button mobile-checkout-quantity-plus"></button>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Доставка -->
      <div class="mobile-checkout-delivery">
        <span class="mobile-checkout-delivery-label">Доставка</span>
        <span class="mobile-checkout-delivery-price">600 ₽</span>
      </div>
      
      <!-- Данные для доставки -->
      <div class="mobile-checkout-delivery-section">
        <h3 class="mobile-checkout-delivery-section-title">Данные для доставки</h3>
        
        <!-- Форма доставки -->
        <div class="mobile-checkout-form">
          <div class="mobile-checkout-form-group">
            <label class="mobile-checkout-form-label">ФИО*</label>
            <input 
              type="text" 
              class="mobile-checkout-form-input" 
              value="Иванов Иван Иванович"
            />
          </div>
          
          <div class="mobile-checkout-form-group">
            <label class="mobile-checkout-form-label">Адрес*</label>
            <input 
              type="text" 
              class="mobile-checkout-form-input" 
              placeholder="Город, почтовый индекс, улица, дом"
            />
          </div>
          
          <div class="mobile-checkout-form-group">
            <label class="mobile-checkout-form-label">Телефон*</label>
            <input 
              type="text" 
              class="mobile-checkout-form-input" 
              placeholder="X XXX XXX-XX-XX"
            />
          </div>
          
          <div class="mobile-checkout-form-group">
            <label class="mobile-checkout-form-label">Служба доставки</label>
            <select class="mobile-checkout-form-select">
              <option>Почта РФ</option>
            </select>
          </div>
        </div>
      </div>
      
      <!-- Комментарии к заказу -->
      <div class="mobile-checkout-comments-section">
        <h3 class="mobile-checkout-comments-title">Комментарии к заказу</h3>
        
        <div class="mobile-checkout-comments-display">
          <div class="mobile-checkout-comment-item mobile-checkout-comment-user">
            <span class="mobile-checkout-comment-author">Вы:</span>
            <span class="mobile-checkout-comment-text">Упакуйте в коробку!</span>
          </div>
          <div class="mobile-checkout-comment-item mobile-checkout-comment-seller">
            <span class="mobile-checkout-comment-author">Продавец:</span>
            <span class="mobile-checkout-comment-text">Всегда упаковываем в коробках</span>
          </div>
        </div>
        
        <input 
          type="text" 
          class="mobile-checkout-comment-input" 
          placeholder="Добавить комментарий к заказу"
        />
        
        <button class="mobile-checkout-send-button" type="button">
          Отправить
        </button>
      </div>
      
      <!-- Кнопка оплаты и таймер -->
      <div class="mobile-checkout-payment-section">
        <button class="mobile-checkout-pay-button" type="button">
          Оплатить
        </button>
        <div class="mobile-checkout-timer-warning">
          <span class="mobile-checkout-timer-label">Заказ будет отменен через:</span>
          <span class="mobile-checkout-timer-value">00:29:31</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import copyIconSvg from '../../значок копирования.svg'
import deleteIcon from '../../иконка корзина.svg'

const router = useRouter()

const goBack = () => {
  router.back()
}

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text)
  } catch (err) {
    console.error('Ошибка копирования:', err)
  }
}
</script>

<style scoped>
.checkout-page {
  width: 100%;
  min-height: 100%;
  background-color: #F6F5EC;
}

.checkout-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 0 32px;
  box-sizing: border-box;
}

.breadcrumbs {
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: 'Inter', sans-serif;
  margin-bottom: 24px;
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

.breadcrumb-first,
.breadcrumb-second {
  opacity: 0.6;
}

.breadcrumb-active {
  opacity: 1;
}

.breadcrumb-slash {
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

.order-items-section {
  width: 100%;
  margin-bottom: 0;
}

.table-headers-wrapper {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 150px 120px 120px;
  gap: 40px;
  align-items: center;
  margin-bottom: 16px;
  padding: 0 16px;
  box-sizing: border-box;
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
  opacity: 1;
  display: flex;
  align-items: center;
}

.header-name {
  opacity: 1;
  padding-left: 390px;
}

.header-quantity {
  justify-content: center;
}

.header-price {
  justify-content: center;
}

.header-article {
  justify-content: center;
  padding-left: 30px;
}

.order-items-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.order-item {
  display: grid;
  grid-template-columns: 1fr 150px 120px 120px;
  gap: 40px;
  align-items: flex-start;
  padding: 0 16px;
  background: transparent;
  border-radius: 10px;
  margin-bottom: 24px;
  box-sizing: border-box;
}

.order-item-name-cell {
  display: flex;
  align-items: flex-start;
  gap: 24px;
}

.order-item-image {
  width: 107px;
  height: 107px;
  border-radius: 10px;
  background: #D9D9D9;
  flex-shrink: 0;
}

.order-item-name {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  flex: 1;
  margin-left: 8px;
}


.order-item-quantity-cell {
  display: flex;
  align-items: center;
  justify-content: center;
}

.order-item-quantity {
  width: 108px;
  height: 40px;
  border-radius: 8px;
  padding: 8px;
  background: rgba(27, 23, 22, 0.1);
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
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  position: relative;
}

.quantity-button-minus::before {
  content: '';
  position: absolute;
  width: 12px;
  height: 2px;
  background: #1B1716;
  border-radius: 1px;
}

.quantity-button-plus::before {
  content: '';
  position: absolute;
  width: 12px;
  height: 2px;
  background: rgba(27, 23, 22, 0.6);
  border-radius: 1px;
}

.quantity-button-plus::after {
  content: '';
  position: absolute;
  width: 2px;
  height: 12px;
  background: rgba(27, 23, 22, 0.6);
  border-radius: 1px;
}

.quantity-value {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  text-align: center;
}

.order-item-price-cell {
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

.order-item-article-cell {
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

.order-delivery-item {
  display: grid;
  grid-template-columns: 1fr 150px 120px 120px;
  gap: 40px;
  align-items: center;
  padding: 0 16px;
  background: transparent;
  border-radius: 10px;
  margin-bottom: 24px;
  box-sizing: border-box;
}

.delivery-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  padding-left: 140px;
}

.delivery-quantity {
  display: flex;
  align-items: center;
  justify-content: center;
}

.delivery-price {
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

.delivery-article {
  display: flex;
  align-items: center;
  justify-content: center;
}

.checkout-main {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  margin-top: -20px;
}

.order-info-section {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-top: 80px;
}

.delivery-section {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.delivery-section-title {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0;
  padding: 0;
}

.info-section-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0;
  padding: 0;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.info-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
  min-width: 100px;
}

.info-value {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 1;
}

.info-value-bold {
  font-weight: 700;
}

.info-value-container {
  display: flex;
  align-items: center;
  gap: 8px;
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
  opacity: 0.6;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: crisp-edges;
  image-rendering: pixelated;
  -ms-interpolation-mode: nearest-neighbor;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  opacity: 0.6;
}

.form-input,
.form-select {
  width: 100%;
  height: 40px;
  padding: 8px 16px;
  border: 2px solid #1B1716;
  border-radius: 10px;
  background: #F6F5EC;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  box-sizing: border-box;
}

.form-input::placeholder {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B171699;
  opacity: 1;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: #640000;
}

.form-input:focus::placeholder {
  color: transparent;
}

.comments-section {
  width: 100%;
  padding: 40px 0 60px 0;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.comments-title {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0;
  padding: 0;
}

.comments-display {
  width: 100%;
  max-width: 100%;
  min-height: 94px;
  border-radius: 10px;
  padding: 16px 24px;
  border: 1px solid #1B1716;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.comment-item {
  display: flex;
  gap: 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
}

.comment-user {
  color: #640000;
}

.comment-seller {
  color: #1B1716;
}

.comment-author {
  font-weight: 400;
}

.comment-text {
  font-weight: 400;
}

.comment-input-wrapper {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  width: 100%;
}

.comment-input {
  flex: 1;
  min-width: 0;
  height: 51px;
  border-radius: 10px;
  padding: 16px 24px;
  border: 1px solid #1B1716;
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  background: #F6F5EC;
  outline: none;
}

.comment-input::placeholder {
  color: #1B171699;
  opacity: 1;
}

.comment-input:focus {
  border-color: #640000;
}

.send-comment-button {
  width: 230px;
  height: 51px;
  flex-shrink: 0;
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

.send-comment-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

.payment-section {
  width: 100%;
  padding: 40px 20px 60px 32px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.pay-button {
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

.pay-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

.timer-warning {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.timer-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
}

.timer-value {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #640000;
}

/* Мобильная версия - скрываем десктопную версию */
@media (max-width: 390px) {
  .desktop-checkout {
    display: none;
  }

  .mobile-checkout {
    display: block;
    width: 100%;
    padding: 16px;
    padding-bottom: 200px; /* Отступ для фиксированных элементов внизу */
    box-sizing: border-box;
    background-color: #F6F5EC;
  }

  /* Кнопка назад */
  .mobile-checkout-back {
    margin-bottom: 24px;
  }

  .mobile-back-button {
    display: flex;
    align-items: center;
    gap: 8px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
  }

  .mobile-back-arrow {
    width: 6px;
    height: 13px;
    background: transparent;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mobile-back-arrow::before {
    content: '<';
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-size: 16px;
    line-height: 1;
    color: #1B171699;
  }

  .mobile-back-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    width: 133px;
    height: 19px;
    white-space: nowrap;
  }

  /* Информация о заказе */
  .mobile-checkout-info {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 24px;
  }

  .mobile-checkout-info-item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-checkout-info-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-checkout-info-value {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-checkout-info-value-bold {
    font-weight: 700;
  }

  .mobile-checkout-info-value-container {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-checkout-copy-button {
    width: 16px;
    height: 16px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0.6;
  }

  .mobile-checkout-copy-icon {
    width: 16px;
    height: 16px;
    display: block;
  }

  /* Товары в заказе */
  .mobile-checkout-items {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 16px;
  }

  .mobile-checkout-item {
    display: flex;
    gap: 16px;
  }

  .mobile-checkout-item-image {
    width: 128px;
    height: 128px;
    border-radius: 10px;
    background: #CACACA;
    flex-shrink: 0;
  }

  .mobile-checkout-item-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .mobile-checkout-item-header {
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }

  .mobile-checkout-item-title {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
    padding: 0;
    flex: 1;
  }

  .mobile-checkout-item-delete {
    width: 16px;
    height: 16px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    flex-shrink: 0;
  }

  .mobile-checkout-delete-icon {
    width: 16px;
    height: 16px;
    display: block;
  }

  .mobile-checkout-item-price-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-checkout-price-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .mobile-checkout-item-price {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
  }

  .mobile-checkout-item-article-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-checkout-article-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .mobile-checkout-item-article {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-checkout-item-quantity {
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

  .mobile-checkout-quantity-button {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mobile-checkout-quantity-minus {
    width: 16px;
    height: 3px;
    background: #1B1716;
    opacity: 1;
    border-radius: 0;
    position: relative;
    border: none;
  }

  .mobile-checkout-quantity-plus {
    width: 16px;
    height: 16px;
    background: transparent;
    opacity: 1;
    border-radius: 0;
    position: relative;
    border: none;
  }

  .mobile-checkout-quantity-plus::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    width: 16px;
    height: 2px;
    background: #1B171699;
  }

  .mobile-checkout-quantity-plus::after {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    width: 2px;
    height: 16px;
    background: #1B171699;
  }

  .mobile-checkout-quantity-value {
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

  /* Доставка */
  .mobile-checkout-delivery {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }

  .mobile-checkout-delivery-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-checkout-delivery-price {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  /* Данные для доставки */
  .mobile-checkout-delivery-section {
    margin-bottom: 24px;
  }

  .mobile-checkout-delivery-section-title {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0 0 24px 0;
    padding: 0;
  }

  /* Форма доставки */
  .mobile-checkout-form {
    display: flex;
    flex-direction: column;
    gap: 24px;
    margin-bottom: 24px;
  }

  .mobile-checkout-form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .mobile-checkout-form-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-checkout-form-input,
  .mobile-checkout-form-select {
    width: 358px;
    height: 40px;
    border-radius: 10px;
    padding: 8px 16px;
    border: 1px solid #1B1716;
    background: #F6F5EC;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    box-sizing: border-box;
    outline: none;
  }

  .mobile-checkout-form-input::placeholder {
    color: #1B171699;
    opacity: 1;
  }

  .mobile-checkout-form-input:not(:placeholder-shown) {
    color: #1B171699;
  }

  .mobile-checkout-form-select {
    width: 197px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg width='13' height='6' viewBox='0 0 13 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L6.5 5L12 1' stroke='%231B1716' stroke-width='2'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 16px center;
    padding-right: 40px;
  }

  .mobile-checkout-form-select option {
    color: #1B171699;
  }

  /* Комментарии к заказу */
  .mobile-checkout-comments-section {
    margin-bottom: 24px;
  }

  .mobile-checkout-comments-title {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0 0 24px 0;
    padding: 0;
  }

  .mobile-checkout-comments-display {
    width: 358px;
    height: 113px;
    border-radius: 10px;
    padding: 16px 24px;
    border: 1px solid #1B1716;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 24px;
    margin-bottom: 16px;
  }

  .mobile-checkout-comment-item {
    display: flex;
    gap: 8px;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
  }

  .mobile-checkout-comment-user {
    color: #640000;
  }

  .mobile-checkout-comment-seller {
    color: #1B1716;
  }

  .mobile-checkout-comment-author {
    font-weight: 400;
  }

  .mobile-checkout-comment-text {
    font-weight: 400;
  }

  .mobile-checkout-comment-input {
    width: 358px;
    height: 51px;
    border-radius: 10px;
    padding: 16px 24px;
    border: 1px solid #1B1716;
    background: #F6F5EC;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    box-sizing: border-box;
    outline: none;
    margin-bottom: 16px;
  }

  .mobile-checkout-comment-input::placeholder {
    color: #1B171699;
    opacity: 1;
  }

  .mobile-checkout-send-button {
    width: 358px;
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
    letter-spacing: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  /* Кнопка оплаты и таймер - фиксированы над навигационной панелью */
  .mobile-checkout-payment-section {
    position: fixed;
    bottom: 64px; /* Высота навигационной панели */
    left: 0;
    right: 0;
    width: 390px;
    height: 94px;
    padding: 16px;
    gap: 8px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background: #F6F5EC;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    z-index: 9998; /* Ниже навигационной панели, но выше контента */
    box-shadow: 0px -4px 8px 0px #1B171640;
  }

  .mobile-checkout-pay-button {
    width: 358px;
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
    letter-spacing: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
  }

  .mobile-checkout-timer-warning {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }

  .mobile-checkout-timer-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    text-align: center;
    color: #1B1716;
  }

  .mobile-checkout-timer-value {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    text-align: center;
    color: #640000;
  }
}

/* Десктопная версия - показываем контент */
@media (min-width: 391px) {
  .desktop-checkout {
    display: block;
  }

  .mobile-checkout {
    display: none;
  }
}
</style>
