<template>
  <div class="orders-page">
    <!-- Десктопная версия -->
    <div class="orders-content desktop-orders">
      <div class="orders-header">
        <div class="breadcrumbs">
          <router-link to="/" class="breadcrumb-item breadcrumb-link">Каталог</router-link>
          <span class="breadcrumb-slash">/</span>
          <span class="breadcrumb-item breadcrumb-active">Заказы</span>
        </div>
        <div class="order-search-wrapper">
          <input 
            type="text"
            v-model="orderSearchQuery"
            class="order-search-input"
            placeholder="Поиск по номеру заказа"
            @keyup.enter="handleOrderSearch"
          />
          <button 
            type="button"
            class="order-search-button"
            @click="handleOrderSearch"
            aria-label="Найти заказ"
          >
            <img 
              :src="searchIcon" 
              alt="Поиск" 
              class="order-search-icon"
            />
          </button>
        </div>
      </div>
      
      <div class="orders-table-headers">
        <div class="table-header header-order-number">
          <span>Заказ №</span>
        </div>
        <div class="table-header header-date" @click="toggleDateFilter">
          <span>Дата</span>
          <img :src="arrowIcon" alt="" class="header-arrow" :class="{ 'arrow-rotated': isDateFilterOpen }" />
          <div v-if="isDateFilterOpen" class="filter-dropdown date-filter-dropdown">
            <div class="filter-option" @click.stop="selectDateFilter('new')">
              <img :src="dateFilter === 'new' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': dateFilter === 'new' }">Сначала новые</span>
            </div>
            <div class="filter-option" @click.stop="selectDateFilter('old')">
              <img :src="dateFilter === 'old' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': dateFilter === 'old' }">Сначала старые</span>
            </div>
          </div>
        </div>
        <div class="table-header header-status" @click="toggleStatusFilter">
          <span>Статус</span>
          <img :src="arrowIcon" alt="" class="header-arrow" :class="{ 'arrow-rotated': isStatusFilterOpen }" />
          <div v-if="isStatusFilterOpen" class="filter-dropdown status-filter-dropdown">
            <div class="filter-option" @click.stop="selectStatusFilter('all')">
              <img :src="statusFilter === 'all' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'all' }">Все</span>
            </div>
            <div class="filter-option" @click.stop="selectStatusFilter('new')">
              <img :src="statusFilter === 'new' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'new' }">Новый</span>
            </div>
            <div class="filter-option" @click.stop="selectStatusFilter('paid')">
              <img :src="statusFilter === 'paid' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'paid' }">Оплачен</span>
            </div>
            <div class="filter-option" @click.stop="selectStatusFilter('in-progress')">
              <img :src="statusFilter === 'in-progress' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'in-progress' }">В работе</span>
            </div>
            <div class="filter-option" @click.stop="selectStatusFilter('sent')">
              <img :src="statusFilter === 'sent' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'sent' }">Отправлен</span>
            </div>
            <div class="filter-option" @click.stop="selectStatusFilter('cancelled')">
              <img :src="statusFilter === 'cancelled' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'cancelled' }">Отменен</span>
            </div>
            <div class="filter-option" @click.stop="selectStatusFilter('return')">
              <img :src="statusFilter === 'return' ? activeRadioIcon : inactiveRadioIcon" alt="" class="radio-icon" />
              <span :class="{ 'filter-option-active': statusFilter === 'return' }">Возврат</span>
            </div>
          </div>
        </div>
        <div class="table-header header-amount">
          <span>Сумма</span>
        </div>
        <div class="table-header header-track">
          <span>Трек</span>
        </div>
      </div>
      
      <div class="orders-list">
        <div class="order-row order-row-sent">
          <div class="order-cell order-number-cell">
            <span>111114532</span>
            <button class="copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
          <div class="order-cell order-date-cell"><span>13.02.2025</span></div>
          <div class="order-cell order-status-cell"><span>Отправлен</span></div>
          <div class="order-cell order-amount-cell"><span>6250 рублей</span></div>
          <div class="order-cell order-track-cell">
            <span>8665 11 00 1347 2</span>
            <button class="copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
        </div>
        
        <div class="order-row order-row-in-progress">
          <div class="order-cell order-number-cell">
            <span>111114532</span>
            <button class="copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
          <div class="order-cell order-date-cell"><span>13.02.2025</span></div>
          <div class="order-cell order-status-cell"><span>В работе</span></div>
          <div class="order-cell order-amount-cell"><span>6250 рублей</span></div>
          <div class="order-cell order-track-cell">
            <span>8665 11 00 1347 2</span>
            <button class="copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
        </div>
        
        <div class="order-row order-row-paid">
          <div class="order-cell order-number-cell">
            <span>111114532</span>
            <button class="copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
          <div class="order-cell order-date-cell"><span>13.02.2025</span></div>
          <div class="order-cell order-status-cell"><span>Оплачен</span></div>
          <div class="order-cell order-amount-cell"><span>6250 рублей</span></div>
          <div class="order-cell order-track-cell">
            <span>8665 11 00 1347 2</span>
            <button class="copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
        </div>
        
        <div class="order-row order-row-cancelled">
          <div class="order-cell order-number-cell">
            <span>111114532</span>
            <button class="copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
          <div class="order-cell order-date-cell"><span>13.02.2025</span></div>
          <div class="order-cell order-status-cell"><span>Отменен</span></div>
          <div class="order-cell order-amount-cell"><span>6250 рублей</span></div>
          <div class="order-cell order-track-cell">
            <span>8665 11 00 1347 2</span>
            <button class="copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
        </div>
        
        <div class="order-row order-row-new">
          <div class="order-cell order-number-cell">
            <span>111114532</span>
            <button class="copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
          <div class="order-cell order-date-cell"><span>13.02.2025</span></div>
          <div class="order-cell order-status-cell"><span>Новый</span></div>
          <div class="order-cell order-amount-cell"><span>6250 рублей</span></div>
          <div class="order-cell order-track-cell">
            <span>8665 11 00 1347 2</span>
            <button class="copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
        </div>
        
        <div class="order-row order-row-return">
          <div class="order-cell order-number-cell">
            <span>111114532</span>
            <button class="copy-button" type="button" @click="copyToClipboard('111114532')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
          <div class="order-cell order-date-cell"><span>13.02.2025</span></div>
          <div class="order-cell order-status-cell"><span>Возврат</span></div>
          <div class="order-cell order-amount-cell"><span>6250 рублей</span></div>
          <div class="order-cell order-track-cell">
            <span>8665 11 00 1347 2</span>
            <button class="copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
              <img :src="copyIcon" alt="Копировать" class="copy-icon" />
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Мобильная версия заказов -->
    <div class="mobile-order-detail">
      <!-- Поиск по номеру заказа -->
      <div class="mobile-order-search">
        <input 
          type="text"
          v-model="orderSearchQuery"
          class="mobile-order-search-input"
          placeholder="Поиск по номеру заказа"
          @keyup.enter="handleOrderSearch"
        />
        <button 
          type="button"
          class="mobile-order-search-button"
          @click="handleOrderSearch"
          aria-label="Найти заказ"
        >
          <img :src="searchIcon" alt="Поиск" class="mobile-order-search-icon" />
        </button>
      </div>
      
      <!-- Фильтры -->
      <div class="mobile-order-filters">
        <div class="mobile-order-filter-item" @click="toggleDateFilter">
          <span class="mobile-order-filter-text">Дата</span>
          <img :src="arrowIcon" alt="" class="mobile-order-filter-arrow" :class="{ 'arrow-rotated': isDateFilterOpen }" />
          <div v-if="isDateFilterOpen" class="mobile-filter-dropdown mobile-date-filter-dropdown">
            <div class="mobile-filter-option" @click.stop="selectDateFilter('new')">
              <img :src="dateFilter === 'new' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': dateFilter === 'new' }">Сначала новые</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectDateFilter('old')">
              <img :src="dateFilter === 'old' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': dateFilter === 'old' }">Сначала старые</span>
            </div>
          </div>
        </div>
        <div class="mobile-order-filter-item" @click="toggleStatusFilter">
          <span class="mobile-order-filter-text">Статус</span>
          <img :src="arrowIcon" alt="" class="mobile-order-filter-arrow" :class="{ 'arrow-rotated': isStatusFilterOpen }" />
          <div v-if="isStatusFilterOpen" class="mobile-filter-dropdown mobile-status-filter-dropdown">
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('all')">
              <img :src="statusFilter === 'all' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'all' }">Все</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('new')">
              <img :src="statusFilter === 'new' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'new' }">Новый</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('paid')">
              <img :src="statusFilter === 'paid' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'paid' }">Оплачен</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('in-progress')">
              <img :src="statusFilter === 'in-progress' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'in-progress' }">В работе</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('sent')">
              <img :src="statusFilter === 'sent' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'sent' }">Отправлен</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('cancelled')">
              <img :src="statusFilter === 'cancelled' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'cancelled' }">Отменен</span>
            </div>
            <div class="mobile-filter-option" @click.stop="selectStatusFilter('return')">
              <img :src="statusFilter === 'return' ? activeRadioIcon : inactiveRadioIcon" alt="" class="mobile-radio-icon" />
              <span :class="{ 'mobile-filter-option-active': statusFilter === 'return' }">Возврат</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Список заказов -->
      <div class="mobile-orders-list">
        <!-- Заказ 1 - Отправлен -->
        <div class="mobile-order-card mobile-order-card-sent">
          <div class="mobile-order-card-row mobile-order-card-row-top">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Заказ №:</span>
              <div class="mobile-order-card-value-container">
                <span class="mobile-order-card-value">111114532</span>
                <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('111114532')">
                  <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
                </button>
              </div>
            </div>
            <span class="mobile-order-card-value mobile-order-card-date">13.02.2025</span>
          </div>
          <div class="mobile-order-card-row">
            <span class="mobile-order-card-value mobile-order-card-price"><span class="mobile-order-card-value-bold">6250</span> рублей</span>
          </div>
          <div class="mobile-order-card-row mobile-order-card-row-bottom">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Статус:</span>
              <span class="mobile-order-card-value">Отправлен</span>
            </div>
            <div class="mobile-order-card-value-container">
              <span class="mobile-order-card-value">8665 11 00 1347 2</span>
              <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
                <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
              </button>
            </div>
          </div>
        </div>
        
        <!-- Заказ 2 - В работе -->
        <div class="mobile-order-card mobile-order-card-sent">
          <div class="mobile-order-card-row mobile-order-card-row-top">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Заказ №:</span>
              <div class="mobile-order-card-value-container">
                <span class="mobile-order-card-value">111114532</span>
                <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('111114532')">
                  <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
                </button>
              </div>
            </div>
            <span class="mobile-order-card-value mobile-order-card-date">13.02.2025</span>
          </div>
          <div class="mobile-order-card-row">
            <span class="mobile-order-card-value mobile-order-card-price"><span class="mobile-order-card-value-bold">6250</span> рублей</span>
          </div>
          <div class="mobile-order-card-row mobile-order-card-row-bottom">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Статус:</span>
              <span class="mobile-order-card-value">В работе</span>
            </div>
            <div class="mobile-order-card-value-container">
              <span class="mobile-order-card-value">8665 11 00 1347 2</span>
              <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
                <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
              </button>
            </div>
          </div>
        </div>
        
        <!-- Заказ 3 - Оплачен -->
        <div class="mobile-order-card mobile-order-card-sent">
          <div class="mobile-order-card-row mobile-order-card-row-top">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Заказ №:</span>
              <div class="mobile-order-card-value-container">
                <span class="mobile-order-card-value">111114532</span>
                <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('111114532')">
                  <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
                </button>
              </div>
            </div>
            <span class="mobile-order-card-value mobile-order-card-date">13.02.2025</span>
          </div>
          <div class="mobile-order-card-row">
            <span class="mobile-order-card-value mobile-order-card-price"><span class="mobile-order-card-value-bold">6250</span> рублей</span>
          </div>
          <div class="mobile-order-card-row mobile-order-card-row-bottom">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Статус:</span>
              <span class="mobile-order-card-value">Оплачен</span>
            </div>
            <div class="mobile-order-card-value-container">
              <span class="mobile-order-card-value">8665 11 00 1347 2</span>
              <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
                <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
              </button>
            </div>
          </div>
        </div>
        
        <!-- Заказ 4 - Отменен -->
        <div class="mobile-order-card mobile-order-card-cancelled">
          <div class="mobile-order-card-row mobile-order-card-row-top">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Заказ №:</span>
              <div class="mobile-order-card-value-container">
                <span class="mobile-order-card-value">111114532</span>
                <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('111114532')">
                  <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
                </button>
              </div>
            </div>
            <span class="mobile-order-card-value mobile-order-card-date">13.02.2025</span>
          </div>
          <div class="mobile-order-card-row">
            <span class="mobile-order-card-value mobile-order-card-price"><span class="mobile-order-card-value-bold">6250</span> рублей</span>
          </div>
          <div class="mobile-order-card-row mobile-order-card-row-bottom">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Статус:</span>
              <span class="mobile-order-card-value">Отменен</span>
            </div>
            <div class="mobile-order-card-value-container">
              <span class="mobile-order-card-value">8665 11 00 1347 2</span>
              <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
                <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
              </button>
            </div>
          </div>
        </div>
        
        <!-- Заказ 5 - Новый -->
        <div class="mobile-order-card mobile-order-card-new">
          <div class="mobile-order-card-row mobile-order-card-row-top">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Заказ №:</span>
              <div class="mobile-order-card-value-container">
                <span class="mobile-order-card-value">111114532</span>
                <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('111114532')">
                  <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
                </button>
              </div>
            </div>
            <span class="mobile-order-card-value mobile-order-card-date">13.02.2025</span>
          </div>
          <div class="mobile-order-card-row">
            <span class="mobile-order-card-value mobile-order-card-price"><span class="mobile-order-card-value-bold">6250</span> рублей</span>
          </div>
          <div class="mobile-order-card-row mobile-order-card-row-bottom">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Статус:</span>
              <span class="mobile-order-card-value">Новый</span>
            </div>
            <div class="mobile-order-card-value-container">
              <span class="mobile-order-card-value">8665 11 00 1347 2</span>
              <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
                <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
              </button>
            </div>
          </div>
        </div>
        
        <!-- Заказ 6 - Возврат -->
        <div class="mobile-order-card mobile-order-card-cancelled">
          <div class="mobile-order-card-row mobile-order-card-row-top">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Заказ №:</span>
              <div class="mobile-order-card-value-container">
                <span class="mobile-order-card-value">111114532</span>
                <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('111114532')">
                  <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
                </button>
              </div>
            </div>
            <span class="mobile-order-card-value mobile-order-card-date">13.02.2025</span>
          </div>
          <div class="mobile-order-card-row">
            <span class="mobile-order-card-value mobile-order-card-price"><span class="mobile-order-card-value-bold">6250</span> рублей</span>
          </div>
          <div class="mobile-order-card-row mobile-order-card-row-bottom">
            <div class="mobile-order-card-left">
              <span class="mobile-order-card-label">Статус:</span>
              <span class="mobile-order-card-value">Возврат</span>
            </div>
            <div class="mobile-order-card-value-container">
              <span class="mobile-order-card-value">8665 11 00 1347 2</span>
              <button class="mobile-order-copy-button" type="button" @click="copyToClipboard('8665 11 00 1347 2')">
                <img :src="copyIcon" alt="Копировать" class="mobile-order-copy-icon" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import searchIcon from '@/assets/images/icon-search-orders.svg'
import arrowIcon from '@/assets/images/icon-arrow-orders.svg'
import copyIcon from '@/assets/images/icon-copy.svg'
import activeRadioIcon from '@/assets/images/icon-radio-active.svg'
import inactiveRadioIcon from '@/assets/images/icon-radio-inactive.svg'
import deleteIcon from '@/assets/images/icon-delete.svg'

const router = useRouter()

const goBack = () => {
  router.back()
}

const orderSearchQuery = ref('')
const isDateFilterOpen = ref(false)
const isStatusFilterOpen = ref(false)
const dateFilter = ref('new') // 'new' или 'old'
const statusFilter = ref('all') // 'all', 'new', 'paid', 'in-progress', 'sent', 'cancelled', 'return'

const handleOrderSearch = () => {
  // Логика поиска заказов будет добавлена позже
  if (orderSearchQuery.value.trim()) {
    console.log('Поиск заказа:', orderSearchQuery.value)
  }
}

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text)
    // Можно добавить уведомление об успешном копировании
  } catch (err) {
    console.error('Ошибка копирования:', err)
  }
}

const toggleDateFilter = () => {
  isDateFilterOpen.value = !isDateFilterOpen.value
  if (isDateFilterOpen.value) {
    isStatusFilterOpen.value = false
  }
}

const toggleStatusFilter = () => {
  isStatusFilterOpen.value = !isStatusFilterOpen.value
  if (isStatusFilterOpen.value) {
    isDateFilterOpen.value = false
  }
}

const selectDateFilter = (value) => {
  dateFilter.value = value
  // Логика фильтрации будет добавлена позже
}

const selectStatusFilter = (value) => {
  statusFilter.value = value
  // Логика фильтрации будет добавлена позже
}

// Закрытие выпадающих меню при клике вне их
const handleClickOutside = (event) => {
  if (!event.target.closest('.header-date') && !event.target.closest('.header-status') &&
      !event.target.closest('.mobile-order-filter-item')) {
    isDateFilterOpen.value = false
    isStatusFilterOpen.value = false
  }
}

// Добавляем обработчик клика вне меню
if (typeof window !== 'undefined') {
  window.addEventListener('click', handleClickOutside)
}
</script>

<style lang="scss" scoped>
@use '@/assets/styles/breakpoints' as *;

.orders-page {
  width: 100%;
  min-height: 100%;
  background-color: #F6F5EC;
}

/* Скрываем мобильную версию на десктопе */
.mobile-order-detail {
  display: none;
}

/* Показываем десктопную версию на десктопе */
.desktop-orders {
  display: block;
}

.orders-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 160px 32px;
  box-sizing: border-box;
}

.orders-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
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

.order-search-wrapper {
  width: 477px;
  height: 40px;
  border-radius: 10px;
  padding: 8px 16px;
  border: 1px solid #1B1716;
  background-color: #F6F5EC;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
  gap: 10px;
  margin-right: 30px;
}

.order-search-input {
  flex: 1;
  height: 100%;
  border: none;
  outline: none;
  background: transparent;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  padding: 0;
  min-width: 0;
}

.order-search-input::placeholder {
  color: #1B171699;
  opacity: 1;
}

.order-search-button {
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
}

.order-search-icon {
  width: 24px;
  height: 24px;
  object-fit: contain;
  display: block;
}

.orders-table-headers {
  width: 100%;
  max-width: 1216px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 40px;
  align-items: center;
  padding: 0 16px;
  box-sizing: border-box;
  margin-bottom: 16px;
}

.table-header {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ============================================
   ОТСТУПЫ ДЛЯ ЗАГОЛОВКОВ ТАБЛИЦЫ
   ============================================
   Чтобы сдвинуть заголовки вправо/влево, меняйте margin-left:
   - Увеличьте значение = сдвиг вправо
   - Уменьшите значение = сдвиг влево
   ============================================ */

/* Отступ для заголовка "Заказ №" */
.header-order-number > span {
  margin-left: 60px; /* Измените это значение для сдвига */
}

/* Отступ для заголовка "Дата" */
.header-date > span {
  margin-left: 40px; /* Измените это значение для сдвига */
}

.header-date {
  position: relative;
  cursor: pointer;
}

/* Отступ для заголовка "Статус" */
.header-status > span {
  margin-left: 30px; /* Измените это значение для сдвига */
}

.header-status {
  position: relative;
  cursor: pointer;
}

/* Отступ для заголовка "Сумма" */
.header-amount > span {
  margin-left: 18px; /* Измените это значение для сдвига */
}

/* Отступ для заголовка "Трек" */
.header-track > span {
  margin-left: 60px; /* Измените это значение для сдвига */
}

.header-arrow {
  width: 13px;
  height: 6px;
  object-fit: contain;
  display: block;
  transition: transform 0.2s ease;
}

.arrow-rotated {
  transform: rotate(180deg);
}

.filter-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  margin-top: 8px;
  border-radius: 10px;
  padding: 24px 16px;
  border: 2px solid #640000;
  background: #F6F5EC;
  display: flex;
  flex-direction: column;
  gap: 24px;
  box-sizing: border-box;
  z-index: 100;
  animation: slideDown 0.2s ease-out;
  transform-origin: top;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.date-filter-dropdown {
  width: 230px;
  min-height: 120px;
}

.status-filter-dropdown {
  width: 230px;
  min-height: 360px;
}

.filter-option {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.radio-icon {
  width: 24px;
  height: 24px;
  object-fit: contain;
  display: block;
  flex-shrink: 0;
}

.filter-option span {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B171699;
}

.filter-option-active {
  color: #1B1716 !important;
}

.orders-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.order-row {
  width: 100%;
  max-width: 1216px;
  height: 39px;
  border-radius: 10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 40px;
  align-items: center;
  padding: 0 16px;
  box-sizing: border-box;
}

.order-row-sent {
  background: #1C2B8C26;
}

.order-row-in-progress {
  background: #1C2B8C26;
}

.order-row-paid {
  background: #1C2B8C26;
}

.order-row-cancelled {
  background: #64000026;
}

.order-row-new {
  background: #5F8F0026;
}

.order-row-return {
  background: #64000026;
}

.order-cell {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  display: flex;
  align-items: center;
  gap: 8px;
}

.order-number-cell,
.order-track-cell {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ============================================
   ОТСТУПЫ ДЛЯ ЯЧЕЕК В СТРОКАХ ЗАКАЗОВ
   ============================================
   Чтобы сдвинуть данные в строках вправо/влево, меняйте margin-left:
   - Увеличьте значение = сдвиг вправо
   - Уменьшите значение = сдвиг влево
   ============================================ */

/* Отступ для номера заказа в строках */
.order-number-cell > span {
  margin-left: 42px; /* Измените это значение для сдвига */
}

/* Отступ для даты в строках */
.order-date-cell > span {
  margin-left: 25px; /* Измените это значение для сдвига */
}

/* Отступ для статуса в строках */
.order-status-cell > span {
  margin-left: 25px; /* Измените это значение для сдвига */
}

/* Отступ для суммы в строках */
.order-amount-cell > span {
  margin-left: 0px; /* Измените это значение для сдвига */
}

/* Отступ для трека в строках (применяется к span внутри) */
.order-track-cell > span {
  margin-left: 0px; /* Измените это значение для сдвига */
}

.copy-button {
  width: 16px;
  height: 16px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.copy-button:hover {
  opacity: 1;
}

.copy-icon {
  width: 16px;
  height: 16px;
  object-fit: contain;
  display: block;
}

/* Мобильная версия - показываем только на мобильных устройствах */
@media (max-width: 1279px) {
  .is-mobile-device .desktop-orders {
    display: none;
  }

  .is-mobile-device .mobile-order-detail {
    display: block;
    width: 100%;
    padding: 0 16px 80px 16px; /* Отступ для нижней навигационной панели */
    margin-top: 10px;
    box-sizing: border-box;
    background-color: #F6F5EC;
  }

  /* Поиск по номеру заказа */
  .is-mobile-device .mobile-order-search {
    width: 100%;
    max-width: 100%;
    height: 40px;
    border-radius: 10px;
    padding: 8px 16px;
    border: 1px solid #1B1716;
    background: #F6F5EC;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    gap: 10px;
    margin-bottom: 16px;
    margin-top: 0;
    margin-left: 0;
  }

  .is-mobile-device .mobile-order-search-input {
    flex: 1;
    height: 100%;
    border: none;
    outline: none;
    background: transparent;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    padding: 0;
    min-width: 0;
  }

  .is-mobile-device .mobile-order-search-input::placeholder {
    color: #1B171699;
    opacity: 1;
  }

  .is-mobile-device .mobile-order-search-button {
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
  }

  .is-mobile-device .mobile-order-search-icon {
    width: 24px;
    height: 24px;
    object-fit: contain;
    display: block;
  }

  /* Фильтры */
  .is-mobile-device .mobile-order-filters {
    display: flex;
    gap: 16px;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    margin-top: 0;
  }

  .is-mobile-device .mobile-order-filter-item {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    position: relative;
  }

  /* Выпадающие меню фильтров для мобильной версии */
  .is-mobile-device .mobile-filter-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    margin-top: 8px;
    border-radius: 10px;
    padding: 24px 16px;
    border: 2px solid #640000;
    background: #F6F5EC;
    display: flex;
    flex-direction: column;
    gap: 24px;
    box-sizing: border-box;
    z-index: 100;
    animation: slideDown 0.2s ease-out;
    transform-origin: top;
  }

  .is-mobile-device .mobile-date-filter-dropdown {
    width: 230px;
    min-height: 120px;
  }

  .is-mobile-device .mobile-status-filter-dropdown {
    width: 230px;
    min-height: 360px;
  }

  .is-mobile-device .mobile-filter-option {
    display: flex;
    align-items: center;
    gap: 12px;
    cursor: pointer;
  }

  .is-mobile-device .mobile-radio-icon {
    width: 24px;
    height: 24px;
    object-fit: contain;
    display: block;
    flex-shrink: 0;
  }

  .is-mobile-device .mobile-filter-option span {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .is-mobile-device .mobile-filter-option-active {
    color: #1B1716 !important;
  }

  .is-mobile-device .mobile-order-filter-text {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .is-mobile-device .mobile-order-filter-arrow {
    width: 13px;
    height: 6px;
    object-fit: contain;
    display: block;
    transition: transform 0.2s ease;
  }

  .is-mobile-device .mobile-order-filter-arrow.arrow-rotated {
    transform: rotate(180deg);
  }

  /* Список заказов */
  .is-mobile-device .mobile-orders-list {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-top: 16px;
    margin-left: -16px;
    width: calc(100% + 32px);
  }

  .is-mobile-device .mobile-order-card {
    width: 100%;
    min-height: 121px;
    padding: 16px;
    gap: 0;
    border-bottom-width: 1px;
    border-bottom: 1px solid #1B1716;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
    flex-shrink: 0;
    overflow: hidden;
  }

  .is-mobile-device .mobile-order-card-sent {
    background: #1C2B8C26;
  }

  .is-mobile-device .mobile-order-card-new {
    background: #5F8F0026;
  }

  .is-mobile-device .mobile-order-card-cancelled {
    background: #64000026;
  }

  .is-mobile-device .mobile-order-card-row {
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: space-between;
  }

  .is-mobile-device .mobile-order-card-row-top {
    margin-bottom: 0;
  }

  .is-mobile-device .mobile-order-card-row-bottom {
    margin-top: 0;
  }

  .is-mobile-device .mobile-order-card-left {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .is-mobile-device .mobile-order-card-date {
    text-align: right;
  }

  .is-mobile-device .mobile-order-card-price {
    font-weight: 700;
    margin: 4px 0;
    text-align: right;
    width: 100%;
  }

  .is-mobile-device .mobile-order-card-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .is-mobile-device .mobile-order-card-value {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .is-mobile-device .mobile-order-card-value-bold {
    font-weight: 700;
  }

  .is-mobile-device .mobile-order-card-value-container {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .is-mobile-device .mobile-order-copy-button {
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

  .is-mobile-device .mobile-order-copy-icon {
    width: 16px;
    height: 16px;
    display: block;
  }

  /* Кнопка назад */
  .is-mobile-device .mobile-order-back {
    margin-bottom: 24px;
  }

  .is-mobile-device .mobile-back-button {
    display: flex;
    align-items: center;
    gap: 8px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
  }

  .is-mobile-device .mobile-back-arrow {
    width: 6px;
    height: 13px;
    background: transparent;
    position: relative;
  }

  .is-mobile-device .mobile-back-arrow::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%) rotate(45deg);
    width: 2px;
    height: 9px;
    background: #1B171699;
    border-radius: 1px;
  }

  .is-mobile-device .mobile-back-arrow::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%) rotate(-45deg);
    width: 2px;
    height: 9px;
    background: #1B171699;
    border-radius: 1px;
  }

  .is-mobile-device .mobile-back-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
    width: 133px;
    height: 19px;
  }

  /* Информация о заказе */
  .mobile-order-info {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 24px;
  }

  .mobile-info-item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-info-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-info-value {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-info-value-bold {
    font-weight: 700;
  }

  .mobile-info-value-container {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-copy-button {
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

  .mobile-copy-icon {
    width: 16px;
    height: 16px;
    display: block;
  }

  /* Товары в заказе */
  .mobile-order-items {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 16px;
  }

  .mobile-order-item {
    display: flex;
    gap: 16px;
  }

  .mobile-order-item-image {
    width: 128px;
    height: 128px;
    border-radius: 10px;
    background: #CACACA;
    flex-shrink: 0;
  }

  .mobile-order-item-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .mobile-order-item-header {
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }

  .mobile-order-item-title {
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

  .mobile-order-item-delete {
    width: 16px;
    height: 16px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    flex-shrink: 0;
  }

  .mobile-delete-icon {
    width: 16px;
    height: 16px;
    display: block;
  }

  .mobile-order-item-price-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-order-price-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .mobile-order-item-price {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #640000;
  }

  .mobile-order-item-article-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .mobile-order-article-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B171699;
  }

  .mobile-order-item-article {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-order-copy-button {
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

  .mobile-order-item-quantity {
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

  .mobile-order-quantity-button {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .mobile-order-quantity-minus {
    width: 16px;
    height: 3px;
    background: #1B1716;
    opacity: 1;
    border-radius: 0;
    position: relative;
    border: none;
  }

  .mobile-order-quantity-plus {
    width: 16px;
    height: 16px;
    background: #1B171699;
    opacity: 1;
    border-radius: 0;
    position: relative;
    border: none;
  }

  .mobile-order-quantity-plus::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    width: 16px;
    height: 2px;
    background: #F6F5EC;
  }

  .mobile-order-quantity-plus::after {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    width: 2px;
    height: 16px;
    background: #F6F5EC;
  }

  .mobile-order-quantity-value {
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
  .mobile-order-delivery {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }

  .mobile-delivery-label {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .mobile-delivery-price {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  /* Данные для доставки */
  .mobile-delivery-section {
    margin-bottom: 24px;
  }

  .mobile-delivery-section-title {
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
}

/* Десктопная версия - всегда показываем десктопную версию на десктопных устройствах */
@include desktop {
  .desktop-orders {
    display: block;
  }

  .mobile-order-detail {
    display: none;
  }
}

/* Для десктопных устройств всегда применяем десктопные стили даже при масштабировании */
.is-desktop-device .desktop-orders {
  display: block !important;
}

.is-desktop-device .mobile-order-detail {
  display: none !important;
}

/* Адаптация для очень маленьких экранов (до 300px) */
@media (max-width: 300px) {
  .is-mobile-device .mobile-order-detail {
    padding: 0 8px 80px 8px;
  }

  .is-mobile-device .mobile-order-search {
    padding: 6px 12px;
  }

  .is-mobile-device .mobile-order-search-input {
    font-size: 14px;
  }

  .is-mobile-device .mobile-order-filter-text {
    font-size: 14px;
  }

  .is-mobile-device .mobile-order-card {
    padding: 12px;
    min-height: 110px;
  }

  .is-mobile-device .mobile-order-card-label,
  .is-mobile-device .mobile-order-card-value {
    font-size: 14px;
  }

  .is-mobile-device .mobile-order-card-price {
    font-size: 16px;
  }
}
</style>
