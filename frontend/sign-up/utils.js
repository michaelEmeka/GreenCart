//Variables Initialization(DOM)
const form = document.getElementById("sign-upForm");
const inp = form.querySelectorAll("input");
const send = document.getElementById("submitBtn");

const navButton = document.getElementsByClassName("form-nav"), contentPages = document.getElementsByTagName("form");

//Variable Initialization(Local)
let firstName = inp[0], email = inp[2], passw = inp[3], passwConfirm = inp[4];

let validN, validE, validP, validP2, validPass;
validE, validN, validP, validP2, validPass = false;


//TOGGLE DETAIL-OTP FORMS

window.addEventListener("DOMContentLoaded", () => {
    initPage();
});

function initPage() {
    //page setup
    navButton[0].click();
    send.disabled = true;
    send.style.backgroundColor = "grey";
    for (let b = 0; b < navButton.length; b++) {
        navButton[b].style.display = "none";
    }
}


function changeTab(evt, val) {
    //Switches form tabs

    for (let i = 0; i < contentPages.length; i++) {
        contentPages[i].style.display = "none";
        //Setup appropriate form navigation buttons as visible
        if (i < 2)
            navButton[i].style.display = "block";
            navButton[i].style.visibility = "visible";
    }
    //Hide unwanted form nav button
    evt.target.style.visibility = "hidden";
    document.getElementById(val).style.display = "block";
}


//VALIDATE FORMS

email.addEventListener("input", function () {
    if (!RegexpValidate(this)) {
        validE = false;
        this.style.border = "2px solid red";
        validateAll();
    } else {
        validE = true;
        this.style.border = "2px solid #217103";
        validateAll();
    }
});

firstName.addEventListener("input", function () {
    validN = NullValidate(this);
    validateAll();
});

passw.addEventListener("input", function () {
    validP = NullValidate(this);
    validPass = PassEqual(this, passwConfirm);
    validateAll();
});

passwConfirm.addEventListener("input", function () {
    validP2 = NullValidate(this);
    validPass = PassEqual(passw, this);
    validateAll();
});

//VALIADATE FUNCTIONS
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

let PassEqual = (pass1, pass2) => {
    if (pass1.value === pass2.value) {
        pass1.style.border = "2px solid #217103";
        pass2.style.border = "2px solid #217103";
        return true;
    }
    else {
        pass1.style.border = "2px solid red";
        pass2.style.border = "2px solid red";
        return false;
    }
    
}

let validateAll = () => {
    if (validE && validN && validP && validP2 && validPass) {
        send.disabled = false;
        send.style.background = "#217103";
    } else {
        send.disabled = true;
        send.style.background = "grey";
    }
};