
document.addEventListener('DOMContentLoaded', function () {
    console.log("Dashboard JS loaded successfully 🚀");

    // Light animation effect on page load
    const header = document.querySelector('header');
    if (header) {
        header.style.opacity = 0;
        header.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            header.style.transition = 'all 0.8s ease';
            header.style.opacity = 1;
            header.style.transform = 'translateY(0)';
        }, 100);
    }

   
});
