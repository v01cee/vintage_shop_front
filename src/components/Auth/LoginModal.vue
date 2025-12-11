<template>
  <div v-if="isOpen" class="login-modal-overlay" @click="closeModal">
    <div class="login-modal" @click.stop>
      <button class="login-modal-close" @click="closeModal" aria-label="Закрыть">
        <span class="login-modal-close-icon">×</span>
      </button>
      
      <!-- Переключатель Войти/Регистрация -->
      <div class="login-modal-tabs">
        <button 
          class="login-tab-button" 
          :class="{ active: activeTab === 'login' }"
          @click="activeTab = 'login'"
        >
          Войти
        </button>
        <button 
          class="login-tab-button" 
          :class="{ active: activeTab === 'register' }"
          @click="activeTab = 'register'"
        >
          Регистрация
        </button>
      </div>

      <!-- Форма входа -->
      <form v-if="activeTab === 'login'" class="login-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label class="form-label">Номер телефона или электронная почта</label>
          <input
            v-model="loginForm.phoneOrEmail"
            type="text"
            class="form-input"
            placeholder="Введите номер телефона или электронную почту"
            required
          />
        </div>
        
        <div class="form-group">
          <label class="form-label">Пароль</label>
          <input
            v-model="loginForm.password"
            type="password"
            class="form-input"
            placeholder="Введите пароль"
            required
          />
        </div>

        <button type="submit" class="form-submit-button">
          Войти
        </button>
      </form>

      <!-- Форма регистрации -->
      <form v-if="activeTab === 'register'" class="login-form" @submit.prevent="handleRegister">
        <div class="form-group">
          <label class="form-label">Номер телефона или электронная почта</label>
          <input
            v-model="registerForm.phoneOrEmail"
            type="text"
            class="form-input"
            placeholder="Введите номер телефона или электронную почту"
            required
          />
        </div>
        
        <div class="form-group">
          <label class="form-label">Пароль</label>
          <input
            v-model="registerForm.password"
            type="password"
            class="form-input"
            placeholder="Введите пароль"
            required
          />
        </div>

        <div class="form-group">
          <label class="form-label">Подтверждение пароля</label>
          <input
            v-model="registerForm.confirmPassword"
            type="password"
            class="form-input"
            placeholder="Повторите пароль"
            required
          />
        </div>

        <button type="submit" class="form-submit-button">
          Зарегистрироваться
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close', 'login', 'register'])

const activeTab = ref('login')

const loginForm = ref({
  phoneOrEmail: '',
  password: ''
})

const registerForm = ref({
  phoneOrEmail: '',
  password: '',
  confirmPassword: ''
})

const closeModal = () => {
  emit('close')
}

const handleLogin = () => {
  emit('login', {
    phoneOrEmail: loginForm.value.phoneOrEmail,
    password: loginForm.value.password
  })
  // Пока просто закрываем модальное окно
  closeModal()
}

const handleRegister = () => {
  if (registerForm.value.password !== registerForm.value.confirmPassword) {
    alert('Пароли не совпадают')
    return
  }
  emit('register', {
    phoneOrEmail: registerForm.value.phoneOrEmail,
    password: registerForm.value.password
  })
  // Пока просто закрываем модальное окно
  closeModal()
}

// Сброс форм при закрытии модального окна
watch(() => props.isOpen, (newValue) => {
  if (!newValue) {
    loginForm.value = {
      phoneOrEmail: '',
      password: ''
    }
    registerForm.value = {
      phoneOrEmail: '',
      password: '',
      confirmPassword: ''
    }
    activeTab.value = 'login'
  }
})

// Закрытие модального окна по ESC
const handleEscape = (event) => {
  if (event.key === 'Escape' && props.isOpen) {
    closeModal()
  }
}

onMounted(() => {
  if (typeof window !== 'undefined') {
    window.addEventListener('keydown', handleEscape)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('keydown', handleEscape)
  }
})
</script>

<style lang="scss" scoped>
@use '@/assets/styles/breakpoints' as *;

.login-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  box-sizing: border-box;
}

.login-modal {
  position: relative;
  width: 100%;
  max-width: 500px;
  background-color: #F6F5EC;
  border: 2px solid #640000;
  border-radius: 10px;
  padding: 40px 32px;
  box-sizing: border-box;
}

.login-modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  font-size: 32px;
  line-height: 1;
  color: #1B1716;
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.login-modal-close:hover {
  opacity: 1;
}

.login-modal-close-icon {
  display: block;
  line-height: 1;
}

.login-modal-tabs {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
  border-bottom: 2px solid #640000;
}

.login-tab-button {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  background: none;
  border: none;
  padding: 0 0 12px 0;
  cursor: pointer;
  opacity: 0.6;
  transition: opacity 0.2s ease;
  position: relative;
}

.login-tab-button::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #640000;
  transition: width 0.2s ease;
}

.login-tab-button.active {
  opacity: 1;
  font-weight: 600;
}

.login-tab-button.active::after {
  width: 100%;
}

.login-tab-button:hover {
  opacity: 1;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
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
}

.form-input {
  width: 100%;
  height: 48px;
  padding: 12px 16px;
  border: 2px solid #640000;
  border-radius: 10px;
  background-color: #F6F5EC;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.2s ease;
}

.form-input::placeholder {
  color: #1B1716;
  opacity: 0.4;
}

.form-input:focus {
  border-color: #7a0000;
}

.form-submit-button {
  width: 100%;
  height: 48px;
  border-radius: 10px;
  padding: 12px 24px;
  background: #640000;
  border: none;
  cursor: pointer;
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
  margin-top: 8px;
}

.form-submit-button:hover {
  background-color: #7a0000;
  opacity: 0.9;
}

/* Мобильная адаптация */
@media (max-width: 1279px) {
  .login-modal-overlay {
    padding: 16px;
    align-items: flex-start;
    padding-top: 20px;
  }

  .login-modal {
    max-width: 100%;
    padding: 32px 16px;
    margin-top: 0;
    border-radius: 10px;
  }

  .login-modal-close {
    top: 12px;
    right: 12px;
    width: 28px;
    height: 28px;
    font-size: 28px;
  }

  .login-modal-tabs {
    gap: 12px;
    margin-bottom: 24px;
  }

  .login-tab-button {
    font-size: 16px;
    padding-bottom: 10px;
  }

  .login-form {
    gap: 20px;
  }

  .form-group {
    gap: 6px;
  }

  .form-label {
    font-size: 14px;
  }

  .form-input {
    height: 44px;
    padding: 10px 14px;
    font-size: 14px;
  }

  .form-submit-button {
    height: 44px;
    font-size: 14px;
    margin-top: 4px;
  }
}

/* Адаптация для очень маленьких экранов (до 300px) */
@media (max-width: 300px) {
  .login-modal-overlay {
    padding: 8px;
    padding-top: 12px;
  }

  .login-modal {
    padding: 24px 12px;
  }

  .login-modal-close {
    top: 8px;
    right: 8px;
    width: 24px;
    height: 24px;
    font-size: 24px;
  }

  .login-tab-button {
    font-size: 14px;
  }

  .form-label {
    font-size: 12px;
  }

  .form-input {
    height: 40px;
    padding: 8px 12px;
    font-size: 12px;
  }

  .form-submit-button {
    height: 40px;
    font-size: 12px;
  }
}
</style>

