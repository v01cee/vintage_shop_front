<template>
  <div class="terms-page">
    <div class="mobile-terms-content">
      <h1 class="mobile-terms-title">Условия</h1>
      
      <p class="mobile-terms-text">
        Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.
      </p>
      
      <div class="mobile-terms-images">
        <div class="mobile-terms-image-placeholder"></div>
        <div class="mobile-terms-image-placeholder"></div>
        <div class="mobile-terms-image-placeholder"></div>
        <div class="mobile-terms-image-placeholder"></div>
      </div>
      
      <p class="mobile-terms-text">
        Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.
        Mauris id ultrices nulla ornare feugiat quis. Nisi mauris pellentesque libero nunc facilisi. Molestie neque nibh id tellus laoreet. Eget erat proin dapibus justo faucibus. Elit lorem urna viverra sed tempor risus orci. Fermentum praesent scelerisque et facilisis libero amet adipiscing pellentesque etiam. Nibh pellentesque bibendum non vulputate felis ac consequat mauris odio.
        Nulla rhoncus sem justo ornare. Aenean tristique gravida arcu nibh eu imperdiet purus pharetra. Suscipit leo dui pharetra massa odio et turpis blandit sit. Viverra eu placerat at sit turpis dictum aliquam. Nulla sit penatibus volutpat sit in. Sed mattis netus ac ultricies pharetra. Amet suspendisse volutpat ipsum malesuada bibendum malesuada amet ac convallis. Egestas nisi ligula fermentum et.
      </p>
    </div>
    <div class="terms-content desktop-terms-content">
      <h1 class="terms-title">Условия</h1>
      
      <p class="terms-text">
        Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.
        Mauris id ultrices nulla ornare feugiat quis. Nisi mauris pellentesque libero nunc facilisi. Molestie neque nibh id tellus laoreet. Eget erat proin dapibus justo faucibus. Elit lorem urna viverra sed tempor risus orci. Fermentum praesent scelerisque et facilisis libero amet adipiscing pellentesque etiam. Nibh pellentesque bibendum non vulputate felis ac consequat mauris odio.
        Nulla rhoncus sem justo ornare. Aenean tristique gravida arcu nibh eu imperdiet purus pharetra. Suscipit leo dui pharetra massa odio et turpis blandit sit. Viverra eu placerat at sit turpis dictum aliquam. Nulla sit penatibus volutpat sit in. Sed mattis netus ac ultricies pharetra. Amet suspendisse volutpat ipsum malesuada bibendum malesuada amet ac convallis. Egestas nisi ligula fermentum et.
      </p>
      
      <div class="terms-images">
        <div class="terms-image-placeholder"></div>
        <div class="terms-image-placeholder"></div>
        <div class="terms-image-placeholder"></div>
        <div class="terms-image-placeholder"></div>
      </div>
      
      <p class="terms-text">
        Lorem ipsum dolor sit amet consectetur. Libero duis amet luctus lacus. Posuere enim lorem sed in morbi. Fringilla ultrices sit tortor cursus sagittis enim gravida. Turpis porta malesuada mauris viverra massa. Pellentesque erat facilisi adipiscing vestibulum gravida elit in. Erat vulputate maecenas at venenatis.
        Mauris id ultrices nulla ornare feugiat quis. Nisi mauris pellentesque libero nunc facilisi. Molestie neque nibh id tellus laoreet. Eget erat proin dapibus justo faucibus. Elit lorem urna viverra sed tempor risus orci. Fermentum praesent scelerisque et facilisis libero amet adipiscing pellentesque etiam. Nibh pellentesque bibendum non vulputate felis ac consequat mauris odio.
        Nulla rhoncus sem justo ornare. Aenean tristique gravida arcu nibh eu imperdiet purus pharetra. Suscipit leo dui pharetra massa odio et turpis blandit sit. Viverra eu placerat at sit turpis dictum aliquam. Nulla sit penatibus volutpat sit in. Sed mattis netus ac ultricies pharetra. Amet suspendisse volutpat ipsum malesuada bibendum malesuada amet ac convallis. Egestas nisi ligula fermentum et.
      </p>
    </div>
  </div>
</template>

<script setup>
// Страница "Условия"
</script>

<style scoped>
.terms-page {
  width: 100%;
  min-height: calc(100vh - 224px);
  background: #F6F5EC;
}

.terms-content {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 16px 20px 60px 32px;
  box-sizing: border-box;
}

.terms-title {
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

.terms-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-style: normal;
  font-size: 16px;
  line-height: 100%;
  letter-spacing: -0.01em;
  color: #1B1716;
  margin: 0 0 24px 0;
  padding: 0;
}

.terms-images {
  display: flex;
  gap: 16px;
  margin: 0 0 24px 0;
}

.terms-image-placeholder {
  width: 292px;
  height: 120px;
  border-radius: 10px;
  background: #8A8A8A;
  flex-shrink: 0;
}

.mobile-terms-content {
  display: none;
}

@media (max-width: 390px) {
  .desktop-terms-content {
    display: none;
  }

  .mobile-terms-content {
    display: block;
    width: 100%;
    padding: 16px;
    padding-top: 50px;
    padding-bottom: 80px;
    box-sizing: border-box;
  }

  .mobile-terms-title {
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

  .mobile-terms-text {
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

  .mobile-terms-images {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    margin-bottom: 16px;
  }

  .mobile-terms-image-placeholder {
    width: 175px;
    height: 88px;
    border-radius: 10px;
    background: #8A8A8A;
  }
}
</style>

