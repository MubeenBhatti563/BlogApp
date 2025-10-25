// navbar.js
const hamburger = document.querySelector('.hamburger');
const navContent = document.querySelector('.nav-content');
const overlay = document.querySelector('.mobile-overlay');
const closeButton = document.querySelector('.sidebar-close');
const searchBtn = document.querySelector('.search-btn');
const searchBar = document.querySelector('.search-bar');
const overlaySearchBar = document.querySelector('.overlay-search-bar');

// Toggle menu on hamburger click
hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleMenu();
});

// Close menu on close button click
closeButton.addEventListener("click", (e) => {
    e.stopPropagation();
    closeMenu();
});

// Close menu when clicking outside (on overlay)
overlay.addEventListener("click", () => {
    closeMenu();
});

// Close menu with Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navContent.classList.contains("active")) {
        closeMenu();
    }
});

function toggleMenu() {
    hamburger.classList.toggle('active');
    navContent.classList.toggle('active');
    overlay.classList.toggle('active');
}

function closeMenu() {
    hamburger.classList.remove('active');
    navContent.classList.remove('active');
    overlay.classList.remove('active');
}

function rmMsg() {
    const messages = document.querySelectorAll('.messages-container');

    messages.forEach(message => {
        const rmBtn = message.querySelector('.rm-msg');

        // Add click event to remove button
        rmBtn.addEventListener("click", () => {
            message.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(() => {
                if (message.parentNode) {
                    message.remove();
                }
            }, 300);
        });

        // Auto-remove after 2 seconds
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(() => {
                if (message.parentNode) {
                    message.remove();
                }
            }, 300);
        }, 2000);
    });
}

// Search Button function
const searchBarAdd = () => {
    searchBtn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (!searchBar.classList.contains('show')) {
            overlaySearchBar.classList.add('show');
            searchBar.classList.add('show');
        }
    })

    document.addEventListener("click", (e) => {
        const target = e.target;

        if (!searchBar.contains(target) && target !== searchBtn) {
            overlaySearchBar.classList.remove('show');
            searchBar.classList.remove('show');
        }
    })
}

document.addEventListener("DOMContentLoaded", searchBarAdd);
document.addEventListener('DOMContentLoaded', rmMsg);