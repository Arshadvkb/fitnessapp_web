$(document).ready(function() {

    $('#form1').validate({
        rules: {
            textfield: {
                required: true,
                minlength: 5
            },
            textfield5: {
                required: true,
                email: true
            },
            textfield2: {
                required: true,
                minlength: 8
            },
            textfield6: {
                required: true,
                minlength: 8
            },
            textfield3: {
                required: true,
                minlength: 10,
                maxlength: 10,
                digits: true
            },
            textfield7: {
                required: true,
            },
            textfield4: {
                required: true,
                minlength: 10,
                maxlength: 50,
            },
            pin: {
                required: true,
                minlength: 6,
                maxlength: 6,
                digits: true
            },
            radiobutton: {
                required: true
            },
            file: {
                required: true
            }
        }
    });
});