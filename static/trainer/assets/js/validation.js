$(document).ready(function() {
    // validate signup form on keyup and submit
    $("#form1").validate({
        rules: {
            textfield: {
                required: true,
                minlength: 10,
                maxlength: 25,
            },
            textarea: {

                required: true,
                minlength: 25,


            }
          
        }
    });
});
