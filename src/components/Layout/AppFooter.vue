<template>
  <footer class="app-footer">
    <div class="footer-wrapper">
      <div class="footer-logo">
        <img :src="logoSvg" alt="Винтажчик магазин" class="logo-image" />
      </div>
      <div class="footer-links">
        <a href="#" class="footer-link">Контакты</a>
        <router-link to="/about-owner" class="footer-link">О сайте</router-link>
        <router-link to="/terms" class="footer-link">Условия</router-link>
        <a href="#" class="footer-link">Офферта</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import logoSvg from '@/assets/images/logo-footer.svg'
</script>

<style scoped>
.app-footer {
  width: 100vw;
  display: block;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  margin-top: auto;
  background: rgba(27, 23, 22, 0.6);
  min-height: 224px;
}

/* Скрываем футер на мобильных и планшетах (до 1279px) */
@media (max-width: 1279px) {
  .app-footer {
    display: none;
  }
}

.footer-wrapper {
  width: 100%;
  max-width: 3000px;
  min-height: 224px;
  background: transparent;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 32px;
  box-sizing: border-box;
  opacity: 1;
  position: relative;
}

/* Адаптивность для разных масштабов */
@media (max-width: 1920px) {
  .footer-wrapper {
    max-width: 1920px;
  }
}

@media (max-width: 1600px) {
  .footer-wrapper {
    max-width: 1600px;
  }
}

@media (max-width: 1280px) {
  .footer-wrapper {
    max-width: 1280px;
  }
}

@media (max-width: 768px) {
  .footer-wrapper {
    flex-direction: column;
    gap: 24px;
    padding: 24px 16px;
    min-height: auto;
    max-width: 100%;
  }
  
  .footer-logo {
    margin-top: 0;
  }
  
  .footer-links {
    position: static;
    width: auto;
    height: auto;
    align-items: center;
  }
}

.footer-logo {
  display: flex;
  align-items: center;
  margin-top: -100px;
}

.logo-image {
  height: auto;
  display: block;
  max-height: 70px;
  width: auto;
  max-width: 100%;
}

@media (max-width: 768px) {
  .logo-image {
    max-height: 50px;
  }
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: flex-end;
  width: 125px;
  height: 144px;
  position: absolute;
  top: 40px;
  right: 32px;
  opacity: 1;
}

.footer-link {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #F6F5EC;
  text-decoration: none;
  opacity: 1;
  white-space: nowrap;
  cursor: pointer;
  display: inline-block;
}

.footer-link:hover {
  opacity: 0.8;
}
</style>

