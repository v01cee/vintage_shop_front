/**
 * Определяет тип устройства пользователя
 * @returns {boolean} true если это мобильное устройство, false если десктоп
 */
export function isMobileDevice() {
  if (typeof window === 'undefined') {
    return false
  }

  // Проверяем User-Agent для мобильных устройств
  const userAgent = navigator.userAgent || navigator.vendor || window.opera
  
  // Список признаков мобильных устройств
  const mobileRegex = /android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini|mobile|tablet/i
  
  if (mobileRegex.test(userAgent)) {
    return true
  }

  // Дополнительная проверка через поддержку touch events
  // На мобильных устройствах обычно есть поддержка touch
  const hasTouchScreen = 'ontouchstart' in window || 
                         navigator.maxTouchPoints > 0 || 
                         navigator.msMaxTouchPoints > 0

  // Проверяем реальную ширину экрана (не viewport, а физический экран)
  // Мобильные устройства обычно имеют ширину экрана <= 768px
  const screenWidth = window.screen.width
  const isSmallScreen = screenWidth <= 768

  // Если есть touch И маленький экран - это мобильное устройство
  // Если нет touch И большой экран - это десктоп
  if (hasTouchScreen && isSmallScreen) {
    return true
  }

  // Если только один признак - используем более строгую проверку
  // На десктопе может быть touch поддержка (например, планшет в режиме десктопа)
  // Но если нет touch И экран маленький - это может быть старый десктоп с маленьким монитором
  // В этом случае полагаемся на User-Agent
  if (mobileRegex.test(userAgent)) {
    return true
  }

  // По умолчанию считаем десктопом
  return false
}

/**
 * Инициализирует класс на documentElement для CSS
 */
export function initDeviceClass() {
  if (typeof window === 'undefined') {
    return
  }

  const isMobile = isMobileDevice()
  document.documentElement.classList.toggle('is-mobile-device', isMobile)
  document.documentElement.classList.toggle('is-desktop-device', !isMobile)
}

