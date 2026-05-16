// theme.js
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('theme-toggle');
  
  if (toggleBtn) {
    const updateIcon = () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      toggleBtn.textContent = isDark ? '☀' : '☾';
    };
    
    updateIcon();
    
    toggleBtn.addEventListener('click', () => {
      const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateIcon();
    });
  }
});
