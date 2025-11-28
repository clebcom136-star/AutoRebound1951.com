// Smooth page transitions and performance optimizations
document.addEventListener('DOMContentLoaded', function() {
    // Add will-change to interactive elements for smoother animations
    const interactiveElements = document.querySelectorAll('a, button, input, .transition-all');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', function() {
            this.style.willChange = 'transform, opacity';
        });
        el.addEventListener('mouseleave', function() {
            this.style.willChange = 'auto';
        });
    });

    // Smooth page fade-in on load
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.3s ease-in-out';
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 10);

    // Smooth page transitions on navigation
    const links = document.querySelectorAll('a[href^="/"], a[href^="./"], a[href^="../"], a:not([href^="http"]):not([href^="#"]):not([target="_blank"])');
    links.forEach(link => {
        if (!link.href.includes('logout') && !link.href.includes('#')) {
            link.addEventListener('click', function(e) {
                const href = this.href;
                // Skip if it's a download link or has download attribute
                if (this.hasAttribute('download') || href.includes('download')) {
                    return;
                }

                e.preventDefault();
                document.body.style.transition = 'opacity 0.2s ease-in-out';
                document.body.style.opacity = '0';
                setTimeout(() => {
                    window.location.href = href;
                }, 200);
            });
        }
    });

    // Optimize image loading
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        if (!img.hasAttribute('loading')) {
            img.setAttribute('loading', 'lazy');
        }
    });

    // Debounce scroll events for better performance
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(function() {
            // Handle scroll events here if needed
        });
    }, { passive: true });

    // Optimize hover effects
    document.addEventListener('mouseover', function(e) {
        if (e.target.matches('button, a, .hover\\:scale-105')) {
            e.target.style.transform = 'translateZ(0)'; // Enable hardware acceleration
        }
    });
});

// Preload next page on hover for instant navigation
let preloadTimer;
document.addEventListener('mouseover', function(e) {
    const link = e.target.closest('a');
    if (link && link.href && !link.href.includes('#') && !link.href.includes('logout')) {
        clearTimeout(preloadTimer);
        preloadTimer = setTimeout(() => {
            const preloader = document.createElement('link');
            preloader.rel = 'prefetch';
            preloader.href = link.href;
            document.head.appendChild(preloader);
        }, 200);
    }
});

document.addEventListener('mouseout', function(e) {
    if (e.target.matches('a')) {
        clearTimeout(preloadTimer);
    }
});