import { defineStore } from 'pinia'
import { productsAPI } from '@/services/api'

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [],
    filteredProducts: [],
    loading: false,
    error: null,
    searchQuery: '',
    selectedFilter: 'default'
  }),

  getters: {
    /**
     * Применить фильтры и сортировку к товарам
     */
    sortedProducts: (state) => {
      let result = [...state.filteredProducts]

      // Применяем сортировку
      switch (state.selectedFilter) {
        case 'price-asc':
          result.sort((a, b) => a.price - b.price)
          break
        case 'price-desc':
          result.sort((a, b) => b.price - a.price)
          break
        case 'new':
          // Для новинок можно сортировать по ID (последние добавленные)
          result.sort((a, b) => b.id - a.id)
          break
        case 'default':
        default:
          // По умолчанию - порядок из API
          break
      }

      return result
    }
  },

  actions: {
    /**
     * Загрузить все товары из API
     */
    async fetchProducts() {
      this.loading = true
      this.error = null
      try {
        const products = await productsAPI.getAll()
        this.products = products || []
        this.applyFilters()
        
        // Если товаров нет, показываем сообщение
        if (this.products.length === 0) {
          console.warn('Товары не найдены')
        }
      } catch (error) {
        this.error = error.message
        console.error('Ошибка загрузки товаров:', error)
        // Используем временные данные для разработки, если API недоступен
        if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError')) {
          console.warn('API недоступен, используем временные данные')
          this.products = this.getMockProducts()
          this.applyFilters()
          this.error = null // Скрываем ошибку, если есть мок-данные
        }
      } finally {
        this.loading = false
      }
    },

    /**
     * Временные данные для разработки
     */
    getMockProducts() {
      return [
        { id: 1, name: 'Винтажная сумка', description: 'Красивая винтажная сумка из кожи', price: 5000, image: '', category: 'Аксессуары' },
        { id: 2, name: 'Винтажное платье', description: 'Элегантное платье 80-х годов', price: 8000, image: '', category: 'Одежда' },
        { id: 3, name: 'Винтажные духи', description: 'Редкие духи из коллекции', price: 12000, image: '', category: 'Парфюмерия' },
        { id: 4, name: 'Винтажные часы', description: 'Швейцарские часы 70-х', price: 15000, image: '', category: 'Аксессуары' },
        { id: 5, name: 'Винтажная куртка', description: 'Кожаная куртка в отличном состоянии', price: 10000, image: '', category: 'Одежда' },
        { id: 6, name: 'Винтажная косметика', description: 'Ретро косметика из коллекции', price: 3000, image: '', category: 'Косметика' },
        { id: 7, name: 'Винтажные очки', description: 'Стильные очки 90-х', price: 4000, image: '', category: 'Аксессуары' },
        { id: 8, name: 'Винтажное украшение', description: 'Серебряное кольцо с камнем', price: 6000, image: '', category: 'Аксессуары' },
        { id: 9, name: 'Винтажная блузка', description: 'Шелковая блузка в винтажном стиле', price: 4500, image: '', category: 'Одежда' },
        { id: 10, name: 'Винтажный парфюм', description: 'Классический аромат', price: 7000, image: '', category: 'Парфюмерия' }
      ]
    },

    /**
     * Поиск товаров
     */
    async searchProducts(query) {
      this.searchQuery = query
      this.loading = true
      this.error = null
      
      try {
        if (query.trim()) {
          this.filteredProducts = await productsAPI.search(query)
        } else {
          this.filteredProducts = [...this.products]
        }
        this.applyFilters()
      } catch (error) {
        this.error = error.message
        console.error('Ошибка поиска:', error)
      } finally {
        this.loading = false
      }
    },

    /**
     * Применить фильтры
     */
    applyFilters() {
      if (this.searchQuery.trim()) {
        // Если есть поисковый запрос, фильтры уже применены в searchProducts
        return
      }
      // Копируем все товары в filteredProducts
      this.filteredProducts = this.products.length > 0 ? [...this.products] : []
    },

    /**
     * Установить фильтр сортировки
     */
    setFilter(filter) {
      this.selectedFilter = filter
    },

    /**
     * Получить товар по ID
     */
    async getProductById(id) {
      try {
        return await productsAPI.getById(id)
      } catch (error) {
        console.error('Ошибка загрузки товара:', error)
        throw error
      }
    }
  }
})

