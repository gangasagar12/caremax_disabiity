// Force Clean UI by removing any saved Dark Mode settings from Jazzmin/AdminLTE
document.addEventListener("DOMContentLoaded", function() {
    // Clear Jazzmin's saved theme from local storage
    localStorage.removeItem("theme");
    localStorage.removeItem("dark_mode");
    
    // Forcibly remove dark-mode classes from the body
    document.body.classList.remove('dark-mode');
    document.documentElement.removeAttribute('data-theme');
    document.documentElement.removeAttribute('data-bs-theme');
    
    // Find any elements with navbar-dark or sidebar-dark and flip them to light
    var navs = document.querySelectorAll('.navbar-dark');
    navs.forEach(function(nav) {
        nav.classList.remove('navbar-dark');
        nav.classList.add('navbar-light');
        nav.classList.add('navbar-white');
    });

    var sidebars = document.querySelectorAll('.sidebar-dark-primary');
    sidebars.forEach(function(sidebar) {
        sidebar.classList.remove('sidebar-dark-primary');
        sidebar.classList.add('sidebar-light-primary');
    });
});
