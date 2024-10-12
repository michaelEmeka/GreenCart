

var form = document.getElementById("sign-upForm");
var inp = form.querySelectorAll("input");
var send = document.getElementById("submitBtn");

let busName = inp[0], email = inp[1], passw = inp[2], passwConfirm = inp[3];

let validN, validE, validM;
validE = validM = validN = false;

window.addEventListener("load", () => {
    console.log(send);
    send.disabled = true;
    send.style.backgroundColor = "grey";

});

email.addEventListener("input", function () {
    if (!RegexpValidate(this)) {
        validE = false;
        this.style.border = "0.5px solid red";
        validateAll();
    } else {
        validE = true;
        this.style.border = "None";
        validateAll();
    }
});

busName.addEventListener("input", function () {
    validN = NullValidate(this);
    validateAll();
});

passw.addEventListener("input", function () {
    validM = NullValidate(this);
    validateAll();
});

passwConfirm.addEventListener("input", function () {
    validM = NullValidate(this);
    validateAll();
});

let RegexpValidate = (obj) => {
    RGEX =
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    let res = obj.value.match(RGEX);
    return res;
};

let NullValidate = (obj) => {
    let inpt = obj.value;
    if (inpt == "") {
        obj.style.border = "0.5px solid red";
        return false;
    } else {
        obj.style.border = "None";
        return true;
    }
};

let validateAll = () => {
    if (validE && validM && validN) {
        send.disabled = false;
        send.style.background = " rgb(75, 33, 173)";
    } else {
        send.disabled = true;
        send.style.background = " rgb(44, 44, 44)";
    }
};
