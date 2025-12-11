<template>
  <div class="reviews-page">
    <div class="mobile-reviews-content">
      <h1 class="mobile-reviews-title">Отзывы</h1>
      <div class="mobile-reviews-list">
        <!-- Первый отзыв - развернут, с ответом продавца -->
        <div class="mobile-review-item">
          <div class="mobile-review-header">
            <div class="mobile-review-content-wrapper">
              <div class="mobile-review-username">Имя пользователя</div>
              <div class="mobile-review-product">
                <span class="mobile-review-label">Отзыв на:</span>
                <span class="mobile-review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[0]" class="mobile-review-text">
                <p>Lorem ipsum dolor sit amet consectetur. Tincidunt velit feugiat pretium libero orci molestie facilisi enim semper. Dapibus in magna egestas felis enim nunc turpis. Amet sit elementum porttitor leo viverra magna orci accumsan cras. Et turpis phasellus tortor magna nibh at viverra amet ligula.</p>
              </div>
              <div v-if="expandedReviews[0]" class="mobile-review-seller-response">
                <span class="mobile-seller-label">Ответ продавца</span>
                <p class="mobile-seller-text">Lorem ipsum dolor sit amet consectetur. Natoque quam pellentesque ac iaculis. Convallis fermentum quis tincidunt massa risus erat a.</p>
              </div>
            </div>
            <button class="mobile-review-toggle-button" @click="toggleReview(0)">
              <img :src="arrowIcon" alt="" class="mobile-review-arrow" :class="{ 'arrow-rotated': !expandedReviews[0] }" />
            </button>
          </div>
        </div>
        
        <!-- Второй отзыв - развернут, с текстом и 4 изображениями -->
        <div class="mobile-review-item">
          <div class="mobile-review-header">
            <div class="mobile-review-content-wrapper">
              <div class="mobile-review-username">Имя пользователя</div>
              <div class="mobile-review-product">
                <span class="mobile-review-label">Отзыв на:</span>
                <span class="mobile-review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[1]" class="mobile-review-text">
                <p>Lorem ipsum dolor sit amet consectetur. Tincidunt velit feugiat pretium libero orci molestie facilisi enim semper. Dapibus in magna egestas felis enim nunc turpis. Amet sit elementum porttitor leo viverra magna orci accumsan cras. Et turpis phasellus tortor magna nibh at viverra amet ligula.</p>
                <div class="mobile-review-images">
                  <div class="mobile-review-image-placeholder"></div>
                  <div class="mobile-review-image-placeholder"></div>
                  <div class="mobile-review-image-placeholder"></div>
                  <div class="mobile-review-image-placeholder"></div>
                </div>
              </div>
            </div>
            <button class="mobile-review-toggle-button" @click="toggleReview(1)">
              <img :src="arrowIcon" alt="" class="mobile-review-arrow" :class="{ 'arrow-rotated': !expandedReviews[1] }" />
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="reviews-content desktop-reviews-content">
      <div class="breadcrumbs">
        <router-link to="/" class="breadcrumb-item breadcrumb-link">Каталог</router-link>
        <span class="breadcrumb-slash">/</span>
        <span class="breadcrumb-item breadcrumb-active">Отзывы</span>
      </div>
      
      <div class="reviews-list">
        <!-- Первый отзыв - развернут, с ответом продавца -->
        <div class="review-item">
          <div class="review-header">
            <div class="review-content-wrapper">
              <div class="review-username">Имя пользователя</div>
              <div class="review-product">
                <span class="review-label">Отзыв на:</span>
                <span class="review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[0]" class="review-seller-response">
                <span class="seller-label">Ответ продавца</span>
                <p class="seller-text">Lorem ipsum dolor sit amet consectetur. Natoque quam pellentesque ac iaculis. Convallis fermentum quis tincidunt massa risus erat a.</p>
              </div>
            </div>
            <button class="review-toggle-button" @click="toggleReview(0)">
              <img :src="arrowIcon" alt="" class="review-arrow" :class="{ 'arrow-rotated': !expandedReviews[0] }" />
            </button>
          </div>
        </div>
        
        <!-- Второй отзыв - развернут, с текстом и 4 изображениями -->
        <div class="review-item">
          <div class="review-header">
            <div class="review-content-wrapper">
              <div class="review-username">Имя пользователя</div>
              <div class="review-product">
                <span class="review-label">Отзыв на:</span>
                <span class="review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[1]" class="review-text">
                <p>Lorem ipsum dolor sit amet consectetur. Tincidunt velit feugiat pretium libero orci molestie facilisi enim semper. Dapibus in magna egestas felis enim nunc turpis. Amet sit elementum porttitor leo viverra magna orci accumsan cras. Et turpis phasellus tortor magna nibh at viverra amet ligula.</p>
                <div class="review-images">
                  <div class="review-image-placeholder"></div>
                  <div class="review-image-placeholder"></div>
                  <div class="review-image-placeholder"></div>
                  <div class="review-image-placeholder"></div>
                </div>
              </div>
            </div>
            <button class="review-toggle-button" @click="toggleReview(1)">
              <img :src="arrowIcon" alt="" class="review-arrow" :class="{ 'arrow-rotated': !expandedReviews[1] }" />
            </button>
          </div>
        </div>
        
        <!-- Третий отзыв - свернут -->
        <div class="review-item">
          <div class="review-header">
            <div class="review-content-wrapper">
              <div class="review-username">Имя пользователя</div>
              <div class="review-product">
                <span class="review-label">Отзыв на:</span>
                <span class="review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[2]" class="review-text">
                <p>Lorem ipsum dolor sit amet consectetur. Tincidunt velit feugiat pretium libero orci molestie facilisi enim semper. Dapibus in magna egestas felis enim nunc turpis. Amet sit elementum porttitor leo viverra magna orci accumsan cras. Et turpis phasellus tortor magna nibh at viverra amet ligula.</p>
              </div>
            </div>
            <button class="review-toggle-button" @click="toggleReview(2)">
              <img :src="arrowIcon" alt="" class="review-arrow" :class="{ 'arrow-rotated': !expandedReviews[2] }" />
            </button>
          </div>
        </div>
        
        <!-- Четвертый отзыв - свернут -->
        <div class="review-item">
          <div class="review-header">
            <div class="review-content-wrapper">
              <div class="review-username">Имя пользователя</div>
              <div class="review-product">
                <span class="review-label">Отзыв на:</span>
                <span class="review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[3]" class="review-text">
                <p>Lorem ipsum dolor sit amet consectetur. Tincidunt velit feugiat pretium libero orci molestie facilisi enim semper. Dapibus in magna egestas felis enim nunc turpis. Amet sit elementum porttitor leo viverra magna orci accumsan cras. Et turpis phasellus tortor magna nibh at viverra amet ligula.</p>
              </div>
            </div>
            <button class="review-toggle-button" @click="toggleReview(3)">
              <img :src="arrowIcon" alt="" class="review-arrow" :class="{ 'arrow-rotated': !expandedReviews[3] }" />
            </button>
          </div>
        </div>
        
        <!-- Пятый отзыв - развернут, с текстом и 2 изображениями -->
        <div class="review-item">
          <div class="review-header">
            <div class="review-content-wrapper">
              <div class="review-username">Имя пользователя</div>
              <div class="review-product">
                <span class="review-label">Отзыв на:</span>
                <span class="review-product-name">Винтаж Туалетная вода L'Air du Temps Nina Ricci EDT Спрей 120 мл. Полный Франция 1990-е</span>
              </div>
              <div v-if="expandedReviews[4]" class="review-text">
                <p>Lorem ipsum dolor sit amet consectetur. Tincidunt velit feugiat pretium libero orci molestie facilisi enim semper. Dapibus in magna egestas felis enim nunc turpis. Amet sit elementum porttitor leo viverra magna orci accumsan cras. Et turpis phasellus tortor magna nibh at viverra amet ligula.</p>
                <div class="review-images">
                  <div class="review-image-placeholder"></div>
                  <div class="review-image-placeholder"></div>
                </div>
              </div>
            </div>
            <button class="review-toggle-button" @click="toggleReview(4)">
              <img :src="arrowIcon" alt="" class="review-arrow" :class="{ 'arrow-rotated': !expandedReviews[4] }" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import arrowIcon from '../../стрелочка в заказах .svg'

const expandedReviews = ref({
  0: true,  // Первый - развернут
  1: true,  // Второй - развернут
  2: false, // Третий - свернут
  3: false, // Четвертый - свернут
  4: true   // Пятый - развернут
})

const toggleReview = (index) => {
  expandedReviews.value[index] = !expandedReviews.value[index]
}
</script>

<style lang="scss" scoped>
@use '@/assets/styles/breakpoints' as *;

.reviews-page {
  width: 100%;
  min-height: 100%;
  background-color: #F6F5EC;
}

/* Скрываем мобильную версию на десктопе */
.mobile-reviews-content {
  display: none;
}

/* Показываем десктопную версию на десктопе */
.desktop-reviews-content {
  display: block;
}

.reviews-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 240px 32px;
  box-sizing: border-box;
}

.breadcrumbs {
  display: flex;
  align-items: center;
  gap: 12px;
}

.breadcrumb-item {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-decoration: none;
  color: #1B1716;
}

.breadcrumb-link {
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.breadcrumb-link:hover {
  opacity: 1;
}

.breadcrumb-active {
  opacity: 1;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
}

.breadcrumb-slash {
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

.reviews-list {
  width: 100%;
  max-width: 1216px;
  margin-top: 40px;
  display: flex;
  flex-direction: column;
}

.review-item {
  width: 100%;
  min-height: 264px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  border-bottom: 2px solid #640000;
  padding: 24px 0;
  box-sizing: border-box;
}

.review-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}

.review-content-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.review-username {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
}

.review-product {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.review-label {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B171699;
}

.review-product-name {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B171699;
}

.review-seller-response {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.seller-label {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B171699;
}

.seller-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B171699;
  margin: 0;
}

.review-text {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.review-text p {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0;
}

.review-images {
  display: flex;
  gap: 16px;
}

.review-image-placeholder {
  width: 100px;
  height: 100px;
  border-radius: 10px;
  background: #888888;
  flex-shrink: 0;
}

.review-toggle-button {
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
  margin-top: 0;
}

.review-arrow {
  width: 13px;
  height: 6px;
  object-fit: contain;
  display: block;
  transition: transform 0.2s ease;
}

.arrow-rotated {
  transform: rotate(180deg);
}

/* Мобильная версия - показываем только на мобильных устройствах */
@media (max-width: 1279px) {
  .is-mobile-device .desktop-reviews-content {
    display: none;
  }

  .is-mobile-device .mobile-reviews-content {
    display: block;
    width: 100%;
    max-width: 100%;
    padding: 16px;
    padding-top: 20px;
    padding-bottom: 80px; /* Отступ для нижней навигационной панели */
    box-sizing: border-box;
    overflow-x: hidden;
  }

  .is-mobile-device .mobile-reviews-title {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
    padding: 0;
    margin-bottom: 16px;
  }

  .is-mobile-device .mobile-reviews-list {
    width: 100%;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    gap: 0;
    overflow-x: hidden;
  }

  .is-mobile-device .mobile-review-item {
    width: 100%;
    border-bottom: 2px solid #640000;
    padding: 16px 0;
    box-sizing: border-box;
    overflow: visible;
  }

  .is-mobile-device .mobile-review-header {
    width: 100%;
    max-width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
  }

  .is-mobile-device .mobile-review-content-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 16px;
    overflow: visible;
    width: 100%;
    min-width: 0;
  }

  .is-mobile-device .mobile-review-username {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .is-mobile-device .mobile-review-product {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .is-mobile-device .mobile-review-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .is-mobile-device .mobile-review-product-name {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .is-mobile-device .mobile-review-text {
    display: flex;
    flex-direction: column;
    gap: 0;
  }

  .is-mobile-device .mobile-review-text p {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
  }

  .is-mobile-device .mobile-review-seller-response {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .is-mobile-device .mobile-seller-label {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .is-mobile-device .mobile-seller-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    margin: 0;
  }

  .is-mobile-device .mobile-review-toggle-button {
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
    margin-top: 0;
  }

  .is-mobile-device .mobile-review-arrow {
    width: 13px;
    height: 6px;
    object-fit: contain;
    display: block;
    transition: transform 0.2s ease;
  }

  .is-mobile-device .mobile-review-images {
    display: flex;
    gap: 16px;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    -ms-overflow-style: none;
    width: calc(100% + 32px);
    margin-top: 16px;
    margin-left: -16px;
    margin-right: -16px;
    padding-left: 16px;
    padding-right: 16px;
    box-sizing: content-box;
  }

  .is-mobile-device .mobile-review-images::-webkit-scrollbar {
    display: none;
  }

  .is-mobile-device .mobile-review-image-placeholder {
    width: 100px;
    height: 100px;
    border-radius: 10px;
    background: #888888;
    flex-shrink: 0;
  }
}

/* Десктопная версия - всегда показываем десктопную версию на десктопных устройствах */
@include desktop {
  .desktop-reviews-content {
    display: block;
  }

  .mobile-reviews-content {
    display: none;
  }
}

/* Для десктопных устройств всегда применяем десктопные стили даже при масштабировании */
.is-desktop-device .desktop-reviews-content {
  display: block !important;
}

.is-desktop-device .mobile-reviews-content {
  display: none !important;
}

/* Адаптация для очень маленьких экранов (до 300px) */
@media (max-width: 300px) {
  .is-mobile-device .mobile-reviews-content {
    padding: 0 8px 80px 8px;
  }

  .is-mobile-device .mobile-reviews-title {
    font-size: 18px;
  }

  .is-mobile-device .mobile-review-username,
  .is-mobile-device .mobile-review-label,
  .is-mobile-device .mobile-review-product-name,
  .is-mobile-device .mobile-review-text p {
    font-size: 14px;
  }
}
</style>

