<template>
  <div class="about-owner-page">
    <div class="mobile-about-owner-content">
      <h1 class="mobile-about-owner-title">О сайте</h1>
      
      <p class="mobile-about-owner-text">
        Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.
      </p>
      
      <div class="mobile-about-owner-image"></div>
      
      <p class="mobile-about-owner-text">
        Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.
        Mauris id ultrices nulla ornare feugiat quis. Nisi mauris pellentesque libero nunc facilisi. Molestie neque nibh id tellus laoreet. Eget erat proin dapibus justo faucibus. Elit lorem urna viverra sed tempor risus orci. Fermentum praesent scelerisque et facilisis libero amet adipiscing pellentesque etiam. Nibh pellentesque bibendum non vulputate felis ac consequat mauris odio.
      </p>
      
      <h2 class="mobile-guide-title">Гайд по сайту</h2>
      
      <div class="mobile-guide-block">
        <p class="mobile-guide-text">
          <span class="mobile-guide-text-bold">Lorem ipsum dolor sit amet consectetur.</span>
          <span class="mobile-guide-text-regular"> Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida.</span>
        </p>
        <div class="mobile-guide-image"></div>
        <p class="mobile-guide-caption">Lorem ipsum</p>
      </div>
      
      <div class="mobile-guide-block">
        <p class="mobile-guide-text">
          <span class="mobile-guide-text-bold">Lorem ipsum dolor sit amet consectetur.</span>
          <span class="mobile-guide-text-regular"> Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida.</span>
        </p>
        <div class="mobile-guide-image"></div>
        <p class="mobile-guide-caption">Lorem ipsum</p>
      </div>
    </div>
    <div class="about-owner-content desktop-about-owner-content">
      <!-- Секция "О сайте" -->
      <section class="about-seller-section">
        <h1 class="section-title">О сайте</h1>
        <div class="about-seller-content">
          <div class="about-seller-text">
            <p>Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.</p>
            <p>Mauris id ultrices nulla ornare feugiat quis. Nisi mauris pellentesque libero nunc facilisi. Molestie neque nibh id tellus laoreet. Eget erat proin dapibus justo faucibus. Elit lorem urna viverra sed tempor risus orci. Fermentum praesent scelerisque et facilisis libero amet adipiscing pellentesque etiam. Nibh pellentesque bibendum non vulputate felis ac consequat mauris odio.</p>
            <p>Nulla rhoncus sem justo ornare. Aenean tristique gravida arcu nibh eu imperdiet purus pharetra. Suscipit leo dui pharetra massa odio et turpis blandit sit. Viverra eu placerat at sit turpis dictum aliquam. Nulla sit penatibus volutpat sit in. Sed mattis netus ac ultricies pharetra. Amet suspendisse volutpat ipsum malesuada bibendum malesuada amet ac convallis. Egestas nisi ligula fermentum et.</p>
          </div>
          <div class="about-seller-image"></div>
        </div>
      </section>

      <!-- Секция "Гайд по сайту" -->
      <section class="site-guide-section">
        <h2 class="guide-title">Гайд по сайту</h2>
        <div class="guide-blocks">
          <div class="guide-block">
            <div class="guide-text-container">
              <p class="guide-text">
                <span class="guide-text-bold">Lorem ipsum dolor sit amet consectetur.</span>
                <span class="guide-text-regular"> Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida.</span>
              </p>
            </div>
            <div class="guide-image"></div>
            <p class="guide-image-caption">Lorem ipsum</p>
          </div>
          <div class="guide-block">
            <div class="guide-text-container">
              <p class="guide-text">
                <span class="guide-text-bold">Lorem ipsum dolor sit amet consectetur.</span>
                <span class="guide-text-regular"> Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida.</span>
              </p>
            </div>
            <div class="guide-image"></div>
            <p class="guide-image-caption">Lorem ipsum</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
// Страница "О сайте"
</script>

<style lang="scss" scoped>
@use '@/assets/styles/breakpoints' as *;

.about-owner-page {
  width: 100%;
  min-height: calc(100vh - 224px);
  background: #F6F5EC;
}

/* Скрываем мобильную версию на десктопе */
.mobile-about-owner-content {
  display: none;
}

/* Показываем десктопную версию на десктопе */
.desktop-about-owner-content {
  display: block;
}

.about-owner-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 240px 32px;
  box-sizing: border-box;
}

/* Секция "О сайте" */
.about-seller-section {
  margin-bottom: 48px;
}

.section-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 24px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 24px 0;
  padding: 0;
}

.about-seller-content {
  display: flex;
  gap: 24px;
  align-items: flex-start;
}

.about-seller-text {
  flex: 1;
}

.about-seller-text p {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 16px 0;
  padding: 0;
}

.about-seller-text p:last-child {
  margin-bottom: 0;
}

.about-seller-image {
  width: 600px;
  height: 343px;
  border-radius: 10px;
  background: #8A8A8A;
  flex-shrink: 0;
}

/* Секция "Гайд по сайту" */
.site-guide-section {
  margin-bottom: 48px;
}

.guide-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 20px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 24px 0;
  padding: 0;
}

.guide-blocks {
  display: flex;
  flex-direction: column;
  gap: 32px;
  align-items: center;
}

.guide-block {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  width: 100%;
}

.guide-text-container {
  width: 846px;
}

.guide-text {
  margin: 0;
  padding: 0;
  text-align: left;
}

.guide-text-bold {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
}

.guide-text-regular {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
}

.guide-image {
  width: 846px;
  height: 300px;
  border-radius: 10px;
  background: #8A8A8A;
  flex-shrink: 0;
}

.guide-image-caption {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  text-align: center;
  color: #1B1716;
  margin: 0;
  padding: 0;
}

/* Мобильная версия - показываем только на мобильных устройствах */
@media (max-width: 1279px) {
  .is-mobile-device .desktop-about-owner-content {
    display: none;
  }

  .is-mobile-device .mobile-about-owner-content {
    display: block;
    width: 100%;
    padding: 16px;
    padding-top: 20px;
    padding-bottom: 80px; /* Отступ для нижней навигационной панели */
    box-sizing: border-box;
  }

  .is-mobile-device .mobile-about-owner-title {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 24px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
    padding: 0;
    margin-bottom: 16px;
  }

  .is-mobile-device .mobile-about-owner-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
    padding: 0;
    margin-bottom: 16px;
  }

  .is-mobile-device .mobile-about-owner-image {
    width: 100%;
    max-width: 100%;
    height: 208px;
    border-radius: 10px;
    background: #8A8A8A;
    margin-bottom: 16px;
  }

  .is-mobile-device .mobile-guide-title {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 20px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
    padding: 0;
    margin-bottom: 16px;
    margin-top: 16px;
  }

  .is-mobile-device .mobile-guide-text {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
    margin: 0;
    padding: 0;
  }

  .is-mobile-device .mobile-guide-text-bold {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .is-mobile-device .mobile-guide-text-regular {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 100%;
    letter-spacing: -0.01em;
    color: #1B1716;
  }

  .is-mobile-device .mobile-guide-block {
    margin-bottom: 24px;
  }

  .is-mobile-device .mobile-guide-image {
    width: 100%;
    max-width: 100%;
    height: 208px;
    border-radius: 10px;
    background: #8A8A8A;
    margin-top: 16px;
    margin-bottom: 8px;
  }

  .is-mobile-device .mobile-guide-caption {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 10px;
    line-height: 100%;
    letter-spacing: -0.01em;
    text-align: center;
    color: #1B1716;
    margin: 0;
    padding: 0;
  }
}

/* Десктопная версия - всегда показываем десктопную версию на десктопных устройствах */
@include desktop {
  .desktop-about-owner-content {
    display: block;
  }

  .mobile-about-owner-content {
    display: none;
  }
}

/* Для десктопных устройств всегда применяем десктопные стили даже при масштабировании */
.is-desktop-device .desktop-about-owner-content {
  display: block !important;
}

.is-desktop-device .mobile-about-owner-content {
  display: none !important;
}

/* Адаптация для очень маленьких экранов (до 300px) */
@media (max-width: 300px) {
  .is-mobile-device .mobile-about-owner-content {
    padding: 0 8px 80px 8px;
  }

  .is-mobile-device .mobile-about-owner-title {
    font-size: 20px;
  }

  .is-mobile-device .mobile-about-owner-text,
  .is-mobile-device .mobile-guide-text,
  .is-mobile-device .mobile-guide-text-bold,
  .is-mobile-device .mobile-guide-text-regular {
    font-size: 14px;
  }

  .is-mobile-device .mobile-about-owner-image,
  .is-mobile-device .mobile-guide-image {
    height: 180px;
  }
}
</style>

