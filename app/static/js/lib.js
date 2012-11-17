(function($){
  // Global constant for key codes used by browser event handler
  window.Keys = { ENTER: 13, TAB: 9, UP: 38, DOWN: 40, ESC: 27 };

  // General page-wide error handler
  $.error = function(err_string) {
    console.error(err_string);
  };

  // General page-wide message handler
  $.success = function(message) {
    console.log(message);
  };

})(jQuery);
