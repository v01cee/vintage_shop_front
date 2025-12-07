<template>
  <div class="product-card" @click="handleClick">
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
      <button class="card-add-to-cart-button" type="button" @click.stop="handleAddToCart">
        <img :src="cartIconSvg" alt="Корзина" class="card-cart-icon" />
        <span class="card-cart-text">В корзину</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import exampleImg from '../../../пример.png'
import cardViewsSvg from '../../../значок просмотры на карточке .svg'
import cartIconSvg from '../../../значок корзины на кнопке в корзину.svg'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const handleClick = () => {
  try {
    router.push(`/product/${props.product.id}`).catch(err => {
      // Игнорируем ошибки навигации, если пользователь быстро кликает
      if (err.name !== 'NavigationDuplicated') {
        console.error('Navigation error:', err)
      }
    })
  } catch (error) {
    console.error('Error navigating to product:', error)
  }
}

const handleAddToCart = (e) => {
  e.stopPropagation()
  // TODO: Добавить товар в корзину
}
</script>

<style scoped>
.product-card {
  width: 236px;
  background: #F6F5EC;
  border-radius: 10px;
  overflow: hidden;
  opacity: 1;
  cursor: pointer;
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
  transition: background-color 0.2s ease, opacity 0.2s ease;
}

.card-add-to-cart-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
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
}

/* Мобильная адаптация для экранов 390px */
@media (max-width: 390px) {
  .product-card {
    width: 175px;
    max-width: 175px;
    overflow: hidden;
  }

  .card-image-wrapper {
    width: 175px;
    height: 231px;
    position: relative;
    overflow: hidden;
  }

  .card-image-wrapper::before {
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

  .card-image {
    width: calc(100% + 6px);
    height: calc(100% + 10px);
    position: absolute;
    top: -5px;
    left: -3px;
    object-fit: cover;
  }

  .card-views {
    top: 8px;
    left: 8px;
    z-index: 2;
  }

  .card-views-count {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #F6F5EC;
  }

  .card-content {
    padding: 16px 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    box-sizing: border-box;
  }

  .card-prices {
    width: 100%;
    display: flex;
    align-items: baseline;
    gap: 8px;
    padding-left: 0;
  }

  .card-price-current {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
    width: 57px;
    height: 19px;
    opacity: 1;
  }

  .card-price-old {
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
    opacity: 1;
  }

  .card-price-label {
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

  .card-description {
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

  .card-prices {
    padding-left: 0;
  }

  .card-add-to-cart-button {
    width: 175px;
    height: 31px;
    padding: 8px 24px;
    margin: 8px auto 0;
    align-self: center;
  }

  .card-cart-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 12px;
    line-height: 100%;
    letter-spacing: 0;
    color: #F6F5EC;
    width: auto;
    height: auto;
    white-space: nowrap;
  }
}
</style>

