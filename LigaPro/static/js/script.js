document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");
    const currentPath = window.location.pathname.toLowerCase().replace(/\/+$/, ''); // quitar slashes al final
    const navLinks = document.querySelectorAll(".nav-link");

    // Cambia el estilo del encabezado si no estás en la página principal
    if (currentPath !== "") { // la raíz es cadena vacía tras quitar slash
        header.classList.add("active");
    } else {
        header.classList.remove("active");
    }

    // Inicializar carrusel solo si existe el elemento
    const carouselElement = document.querySelector("#carouselExampleIndicators");
    if (carouselElement) {
        new bootstrap.Carousel(carouselElement, {
            interval: 3000,
            wrap: true
        });
    }

    // Quitar clase active de todos
    navLinks.forEach(link => link.classList.remove("active"));

    // Marcar el enlace activo basado en la ruta actual
    navLinks.forEach(link => {
        let href = link.getAttribute("href").toLowerCase().replace(/\/+$/, '');

        // Caso raíz / o ''
        if ((currentPath === "" && href === "") || (currentPath === "/" && href === "")) {
            link.classList.add("active");
        }
        else if (href !== "" && currentPath.startsWith(href)) {
            link.classList.add("active");
        }
    });
});
