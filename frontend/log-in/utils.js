const form = document.getElementById("log-inForm");
const inp = form.querySelectorAll("input");
const send = document.getElementById("subitBtn");

let validE, validP;
validE = validP = false;

let email = inp[0], passw = inp[1];

window.addEventListener("DOMContentLoaded", () => {
    send.disabled = true;
    send.style.backgroundColor = "grey";
});

email.addEventListener("input", function () {
    if (!RegexpValidate(this)) {
        validE = false;
        this.style.border = "2px solid red";
        ValidateAll();
    } else {
        validE = true;
        this.style.border = "2px solid #217103";
        ValidateAll();
    }
});
passw.addEventListener("input", function () {
    validP = NullValidate(this);
    ValidateAll();
});

let RegexpValidate = (obj) => {
    RGEX =
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    let res = obj.value.match(RGEX);
    return res;
};

let NullValidate = (obj) => {
    if (obj.value == "") {
        obj.style.border = "2px solid red";
        return false;
    } else {
        obj.style.border = "2px solid #217103";
        return true;
    }
};

let ValidateAll = () => {
    if (validE && validP) {
        send.disabled = false;
        send.style.background = "#217103";
    } else {
        send.disabled = true;
        send.style.background = "grey";
    }
};