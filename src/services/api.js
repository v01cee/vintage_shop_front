// Используем переменную окружения или значение по умолчанию
// В продакшене через Docker используем относительный путь (прокси через nginx)
// В разработке используем полный URL
const API_BASE_URL = import.meta.env.VITE_API_URL || 
  (import.meta.env.PROD ? '/api/v1' : 'http://localhost:8000/api/v1')

/**
 * Базовый метод для выполнения HTTP запросов
 */
async function request(url, options = {}) {
  try {
    const response = await fetch(`${API_BASE_URL}${url}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      ...options
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    console.error('API request failed:', error)
    throw error
  }
}

/**
 * API для работы с товарами
 */
export const productsAPI = {
  /**
   * Получить список всех товаров
   */
  async getAll(skip = 0, limit = 100) {
    return request(`/products?skip=${skip}&limit=${limit}`)
  },

  /**
   * Получить товар по ID
   */
  async getById(id) {
    return request(`/products/${id}`)
  },

  /**
   * Поиск товаров по названию
   */
  async search(query) {
    const products = await this.getAll()
    if (!query) return products
    
    const lowerQuery = query.toLowerCase()
    return products.filter(product => 
      product.name.toLowerCase().includes(lowerQuery) ||
      (product.description && product.description.toLowerCase().includes(lowerQuery))
    )
  }
}

/**
 * API для работы с корзиной
 */
export const cartAPI = {
  /**
   * Получить корзину пользователя
   */
  async getCart(userId = 'default') {
    return request(`/cart/${userId}`)
  },

  /**
   * Добавить товар в корзину
   */
  async addItem(userId, productId, quantity = 1) {
    return request(`/cart/${userId}/items`, {
      method: 'POST',
      body: JSON.stringify({
        product_id: productId,
        quantity
      })
    })
  },

  /**
   * Обновить количество товара в корзине
   */
  async updateItem(userId, itemId, quantity) {
    return request(`/cart/${userId}/items/${itemId}?quantity=${quantity}`, {
      method: 'PUT'
    })
  },

  /**
   * Удалить товар из корзины
   */
  async removeItem(userId, itemId) {
    return request(`/cart/${userId}/items/${itemId}`, {
      method: 'DELETE'
    })
  },

  /**
   * Очистить корзину
   */
  async clearCart(userId = 'default') {
    return request(`/cart/${userId}`, {
      method: 'DELETE'
    })
  }
}

