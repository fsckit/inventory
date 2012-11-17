(function($){
  $.fn.search = function() {
    this.each(function(){
      var $this = $(this);

      $this.on('keypress', _.debounce(function(){
        $.get('/search', { q: $this.val() })
          .done(function(results){
            $this.autocomplete(results);
          })
          .fail($.error);
      }, 500));
    });
  };
})(jQuery);

