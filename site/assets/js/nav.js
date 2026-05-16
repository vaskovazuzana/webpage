// nav.js
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const menuToggle = document.querySelector('.menu-toggle');
  const menuClose = document.querySelector('.menu-toggle-close');
  const overlay = document.querySelector('.mobile-nav-overlay');
  
  // Sticky header
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('is-sticky');
    } else {
      header.classList.remove('is-sticky');
    }
  });

  if (menuToggle && overlay && menuClose) {
    menuToggle.addEventListener('click', () => {
      overlay.classList.add('is-open');
    });
    menuClose.addEventListener('click', () => {
      overlay.classList.remove('is-open');
    });
  }
});
