import { defineStore } from 'pinia'
import { cartAPI, productsAPI } from '@/services/api'

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [], // Массив товаров в корзине { id, product_id, quantity, product }
    loading: false,
    error: null,
    userId: 'default' // Временный ID пользователя
  }),
  
  getters: {
    // Общее количество товаров
    totalItems: (state) => {
      return state.items.reduce((sum, item) => sum + item.quantity, 0)
    },
    
    // Общая стоимость
    totalPrice: (state) => {
      return state.items.reduce((sum, item) => {
        const price = item.product?.price || 0
        return sum + (price * item.quantity)
      }, 0)
    }
  },
  
  actions: {
    /**
     * Загрузить корзину из API
     */
    async fetchCart() {
      this.loading = true
      this.error = null
      try {
        const cartItems = await cartAPI.getCart(this.userId)
        // Загружаем полную информацию о товарах
        const itemsWithProducts = await Promise.all(
          cartItems.map(async (item) => {
            try {
              const product = await productsAPI.getById(item.product_id)
              return {
                ...item,
                product
              }
            } catch (error) {
              console.error(`Ошибка загрузки товара ${item.product_id}:`, error)
              return {
                ...item,
                product: null
              }
            }
          })
        )
        this.items = itemsWithProducts
      } catch (error) {
        // Если API недоступен, не показываем ошибку пользователю, просто используем пустую корзину
        if (error.message === 'API_SERVER_UNAVAILABLE') {
          console.warn('Бэкенд API недоступен. Работаем в оффлайн режиме.')
          this.items = []
          // Не устанавливаем error, чтобы не пугать пользователя
        } else {
          this.error = error.message
          console.error('Ошибка загрузки корзины:', error)
        }
      } finally {
        this.loading = false
      }
    },

    /**
     * Добавить товар в корзину
     */
    async addItem(product, quantity = 1) {
      this.loading = true
      this.error = null
      try {
        await cartAPI.addItem(this.userId, product.id, quantity)
        // Обновляем локальное состояние
        await this.fetchCart()
      } catch (error) {
        this.error = error.message
        console.error('Ошибка добавления товара в корзину:', error)
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * Удалить товар из корзины
     */
    async removeItem(itemId) {
      this.loading = true
      this.error = null
      try {
        await cartAPI.removeItem(this.userId, itemId)
        // Обновляем локальное состояние
        await this.fetchCart()
      } catch (error) {
        this.error = error.message
        console.error('Ошибка удаления товара из корзины:', error)
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * Изменить количество товара
     */
    async updateQuantity(itemId, quantity) {
      if (quantity <= 0) {
        await this.removeItem(itemId)
        return
      }

      this.loading = true
      this.error = null
      try {
        await cartAPI.updateItem(this.userId, itemId, quantity)
        // Обновляем локальное состояние
        await this.fetchCart()
      } catch (error) {
        this.error = error.message
        console.error('Ошибка обновления количества товара:', error)
        throw error
      } finally {
        this.loading = false
      }
    },
    
    /**
     * Очистить корзину
     */
    async clearCart() {
      this.loading = true
      this.error = null
      try {
        await cartAPI.clearCart(this.userId)
        this.items = []
      } catch (error) {
        this.error = error.message
        console.error('Ошибка очистки корзины:', error)
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})

