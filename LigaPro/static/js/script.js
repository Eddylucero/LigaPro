document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");
    const currentPath = window.location.pathname.toLowerCase().trim();
    const navLinks = document.querySelectorAll(".nav-link");

    // Cambia el estilo del encabezado si no estás en la página principal
    if (currentPath !== "/") {
        header.classList.add("active");
    }

    // Activa el carrusel con una velocidad de transición
    new bootstrap.Carousel(document.querySelector("#carouselExampleIndicators"), {
        interval: 3000,
        wrap: true
    });

    // Elimina la clase "active" de todos los enlaces antes de volver a aplicarla
    navLinks.forEach(link => link.classList.remove("active"));

    // Marcar el enlace activo basado en la ruta actual
    navLinks.forEach(link => {
        const href = link.getAttribute("href").toLowerCase().trim();

        // Si la ruta es la raíz y el enlace es "Inicio"
        if (currentPath === "/" && href === "/") {
            link.classList.add("active");
        }
        // Para los demás enlaces: solo marcar si la ruta actual inicia con el href (y no es la raíz)
        else if (href !== "/" && currentPath.startsWith(href)) {
            link.classList.add("active");
        }
    });
});
