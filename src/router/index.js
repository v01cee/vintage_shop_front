import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Cart from '../views/Cart.vue'
import Checkout from '../views/Checkout.vue'
import Orders from '../views/Orders.vue'
import Reviews from '../views/Reviews.vue'
import Terms from '../views/Terms.vue'
import AboutOwner from '../views/AboutOwner.vue'
import Login from '../views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: Product
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: Checkout
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders
  },
  {
    path: '/reviews',
    name: 'Reviews',
    component: Reviews
  },
  {
    path: '/terms',
    name: 'Terms',
    component: Terms
  },
  {
    path: '/about-owner',
    name: 'AboutOwner',
    component: AboutOwner
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  // Фоллбек: все неизвестные маршруты редиректим на главную
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Обработка ошибок навигации
router.onError((error) => {
  console.error('Router error:', error)
})

export default router

