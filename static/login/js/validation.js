$(document).ready(function() {
    // validate login form on keyup and submit
    $("#loginForm").validate({
        rules: {
            textfield2: {
                required: true,
            
            },
            password: {
                required: true,
                minlength: 5
            }
        },
        messages: {
            email: {
                required: "Please enter a valid email address",
                email: "Please enter a valid email address"
            },
            password: {
                required: "Please enter a valid password",
                minlength: "Your password must be at least 5 characters long"
            }
        }
    });
}