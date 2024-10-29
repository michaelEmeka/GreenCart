const hamburgerButton = document.querySelector("#hamburger-button");
const userMenu = document.querySelector("#user-menu");

hamburgerButton.addEventListener("click", () => {
    userMenu.classList.toggle("active");
    hamburgerButton.classList.toggle("active");
});