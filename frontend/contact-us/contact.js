const hamburgerButton = document.querySelector("#hamburger-button");
const navLinks = document.querySelector("#nav-links");
const closeButton = document.querySelector("#close-button");

hamburgerButton.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});

closeButton.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});