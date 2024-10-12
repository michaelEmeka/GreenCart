const hambugerMenu = document.querySelector(".hambugerbtn");
const navList = document.querySelector(".nav-list");
const closeBtn = document.querySelector(".closebtn");

hambugerMenu.addEventListener("click", () => {
    navList.classList.toggle("active");
    console.log("Hi");
    //navList.style.display = "None"
});

closeBtn.addEventListener("click", () => {
    navList.classList.toggle("active");
    console.log("Hi");
});
