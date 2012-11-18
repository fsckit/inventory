(function($){
  // Global constant for key codes used by browser event handler
  window.Keys = { ENTER: 13, TAB: 9, UP: 38, DOWN: 40, ESC: 27 };

  // General page-wide error handler
  $.error = function(error) {
    $.message(error, 'error');
  };

  // General page-wide message handler
  $.success = function(message) {
    $.message(message, 'success');
  };

  $.message = (function(){
    // Fade and lifetime in ms
    var message_fade = 1 * 1000;
    var message_life = 10 * 1000;
    // Queue for messages to be displayed
    var message_queue = [];
    var $navbar = $('.navbar-inner');

    var process_queue = function(){
      if (message_queue.length == 0)
        return;

      // Display next message
      var next = message_queue.shift();
      $('<div>', { class: 'pull-left alert alert-' + next.type })
        // Initially hide
        .hide()
        .text(next.message)
        .appendTo($navbar)
        // Fade in, wait, fade out
        .fadeIn(message_fade)
        .delay(message_life)
        .fadeOut(message_fade, function(){ $(this).trigger('hide'); })
        // When it is hidden, remove it and process next message if there is one
        .on('hide', function(){
          $(this).remove();
          process_queue();
        })
        // When clicked, just hide immediately
        .on('click', function(){
          $(this).stop(true, true).hide().trigger('hide');
        });
    };

    return function(message, type){
      message_queue.push({message: message, type: type || 'info'});
      if (message_queue.length == 1 && $navbar.find('.alert').length == 0) {
        process_queue();
      }
    };
  })();

})(jQuery);
