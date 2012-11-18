(function($){
  // Converts input fields to searchable fields
  $.fn.search = function() {
    this.each(function(){
      var $this = $(this);

      // Debounce to 500ms of silence to prevent frequent searching
      $this.on('keypress', _.debounce(function(){
        $.get('/search', { q: $this.val() })
          // Results are piped to autocomplete
          .done($this.autocomplete);
      }, 500));
    });
  };
})(jQuery);

