(function($){
  // Converts input fields to searchable fields
  $.fn.search = function() {
    this.each(function(){
      var $this = $(this);

      // Debounce to 500ms of silence to prevent frequent searching
      $this.on('keypress', _.debounce(function(){
        if ($this).val().length < 3)
          return;
        $.get('/search', { q: $this.val(), t: 'json' })
          // Results are piped to autocomplete
          .done(function(results){
            $this.typeahead({source: results});
          });
      }, 500));
    });
  };
})(jQuery);

