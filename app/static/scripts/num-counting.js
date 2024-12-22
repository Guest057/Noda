document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".counter h1");

    const observerOptions = {
        threshold: 0.5, // Активується, коли елемент на 50% у полі зору
    };

    const animateCounter = (entry) => {
        const counter = entry.target;
        const targetValue = +counter.getAttribute("data-target");
        let currentValue = 0;
        const duration = 1000; // Тривалість анімації в мілісекундах
        const increment = targetValue / (duration / 16); // Залежно від FPS

        const updateCounter = () => {
            currentValue += increment;
            if (currentValue < targetValue) {
                counter.textContent = Math.ceil(currentValue).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = targetValue.toLocaleString(); // Встановлюємо кінцеве значення з роздільником
            }
        };

        updateCounter();
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                animateCounter(entry);
                observer.unobserve(entry.target); // Припиняє спостереження після досягнення значення
            }
        });
    }, observerOptions);

    counters.forEach((counter) => observer.observe(counter));
});