/* -- Sign In Form - Check Email Format -------------------------------------------------------------------- */
(function($) {
  "use strict";
  var input = $('.validate-input .input100');
  $('.validate-form').on('submit', function() {
    var check = true;
    for (var i = 0; i < input.length; i++) {
      if (validate(input[i]) == false) {
        showValidate(input[i]);
        check = false;
      }
    }
    return check;
  });
  $('.validate-form .input100').each(function() {
    $(this).focus(function() {
      hideValidate(this);
    });
  });

  function validate(input) {
    if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
      if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
        return false;
      }
    } else {
      if ($(input).val().trim() == '') {
        return false;
      }
    }
  }

  function showValidate(input) {
    var thisAlert = $(input).parent();

    $(thisAlert).addClass('alert-validate');
  }

  function hideValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).removeClass('alert-validate');
  }
})(jQuery);
/* -- End Sign In Form - Check Email Format -------------------------------------------------------------------- */


/* -- Sign In Form - Check Number Format -------------------------------------------------------------------- */
(function($) {
  "use strict";
  var input = $('.validate-input .input100');
  $('.validate-form').on('submit', function() {
    var check = true;
    for (var i = 0; i < input.length; i++) {
      if (validate(input[i]) == false) {
        showValidate(input[i]);
        check = false;
      }
    }
    return check;
  });
  $('.validate-form .input100').each(function() {
    $(this).focus(function() {
      hideValidate(this);
    });
  });

  function validate(input) {
    if ($(input).attr('type') == 'number' || $(input).attr('name') == 'n_telephone') {
      if ($(input).val().trim().match(/([0-9]{10})/) == null) {
        return false;
      }
    } else {
      if ($(input).val().trim() == '') {
        return false;
      }
    }
  }

  function showValidate(input) {
    var thisAlert = $(input).parent();

    $(thisAlert).addClass('alert-validate');
  }

  function hideValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).removeClass('alert-validate');
  }
})(jQuery);
/* -- End Sign In Form - Check Number Format -------------------------------------------------------------------- */


/* -- Sign In Form - Check CCP Number Format -------------------------------------------------------------------- */
(function($) {
  "use strict";
  var input = $('.validate-input .input100');
  $('.validate-form').on('submit', function() {
    var check = true;
    for (var i = 0; i < input.length; i++) {
      if (validate(input[i]) == false) {
        showValidate(input[i]);
        check = false;
      }
    }
    return check;
  });
  $('.validate-form .input100').each(function() {
    $(this).focus(function() {
      hideValidate(this);
    });
  });

  function validate(input) {
    if ($(input).attr('type') == 'number' || $(input).attr('name') == 'ccp') {
      if ($(input).val().trim().match(/(([0-9]{7})+(\ )+(\-)+(\ )+([0-9]{2}))/) == null) {
        return false;
      }
    } else {
      if ($(input).val().trim() == '') {
        return false;
      }
    }
  }

  function showValidate(input) {
    var thisAlert = $(input).parent();

    $(thisAlert).addClass('alert-validate');
  }

  function hideValidate(input) {
    var thisAlert = $(input).parent();
    $(thisAlert).removeClass('alert-validate');
  }
})(jQuery);
/* -- End Sign In Form - Check CCP Number Format -------------------------------------------------------------------- */
