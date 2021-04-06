console.log("hiii");
window.onload = function () {
    const user = document.getElementById('name');
    const phone = document.getElementById('phone');
    const email = document.getElementById('email');
    let validEmail = false;
    let validPhone = false;
    let validUser = false;
    $('#success').hide();
    $('#failure').hide();


    user.addEventListener('blur', () => {
        console.log(user);
        let regex = /^[A-Za-z]([0-10A-Za-z]){2,10}$/;
        let str = user.value;
        console.log(str, regex);
        if (regex.test(str)) {
            validUser = true;
            //validate user here
            console.log("name is valid");
            user.classList.remove('is-invalid');

        }
        else {
            console.log("name is not valid");
            user.classList.add('is-invalid');
            validUser = false;

        }
    })

    email.addEventListener('blur', () => {
        //vaidate email here
        let regex1 = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
        let str1 = email.value;
        if (regex1.test(str1)) {
            validEmail = true;
            console.log("email is valid");
            email.classList.remove('is-invalid');

        }
        else {
            console.log("email is not valid");
            email.classList.add('is-invalid');
            validEmail = false;

        }
    })

    phone.addEventListener('blur', () => {
        // validate phone here
        let regex2 = /^([0-9]){10}$/;
        let str2 = phone.value;
        if (regex2.test(str2)) {
            validPhone = true;
            console.log("phone is valid");
            phone.classList.remove('is-invalid');

        }
        else {
            console.log("phone is not valid");
            phone.classList.add('is-invalid');
            validPhone = false;

        }
    })

    let submit = document.getElementById('submit');
    //submit Your form here
    submit.addEventListener('click', (e) => {
        // e.preventDefault();
        console.log("submit button is click");
        console.log(validPhone,validUser,validEmail);
        if (validEmail && validPhone && validUser) {
            console.log("phone,email and user are valid submit the form");
            let success = document.getElementById('success');

            success.classList.add('show');
            //failure.classList.remove('show');
            $('#failure').hide();
            $('#success').show();
        }
        else{
            console.log('one of phone or email or user are not valid.Hence not submitted the form. please correct the error and try again');
            let failure = document.getElementById('failure');
            //success.classList.remove('show');
            failure.classList.add('show');
            $('#success').hide();
            $('#failure').show();



        }
    })

};
