document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('header');

    // ✅ Cambia el color del encabezado si no está en la página principal
    if (window.location.pathname !== "/") {
        header.classList.add('active');
    }

    // ✅ Activa el carrusel con una velocidad de transición
    new bootstrap.Carousel(document.querySelector('#carouselExampleIndicators'), {
        interval: 3000, // Cambia cada 3 segundos
        wrap: true
    });
});
