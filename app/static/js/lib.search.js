(function($){
  // Converts input fields to searchable fields
  $.fn.search = function() {
    this.each(function(){
      var $this = $(this),
          results = {},
          classes = $this.attr('class').split(/\s+/);

      $this.typeahead({
        source: _.debounce(function(query, next){
          $.get('/search', { q: query, t: 'json' })
            .done(function(res){
              // If there is some overlap between the keys in the return and our
              // class names, use those keys only. Otherwise, we use all keys.
              var limit = _.intersection(classes, _.keys(res));
              if (limit.length > 0)
                res = _.pick(res, limit);

              results = _.flatten(_.values(res));
              next(_.keys(results));
            });
        }, 200),
        minLength: 1,
        matcher: function(item) {
          // Reset internal value
          $this.data('value', null);
          return this.constructor.prototype.matcher.call(this, results[item].name);
        },
        sorter: function(items) {
          // This is a idempotent sorter right now, TODO
          return items;
        },
        updater: function(item) {
          // Set internal value
          $this.data('value', results[item].key);
          return results[item].name;
        },
        highlighter: function(item) {
          // The html returned here will be output in each cell in the chooser
          return this.constructor.prototype.highlighter.call(this, results[item].name);
        },
      });

      $this.on('blur', function(e){
        // If we don't have an internal value set, we need to find it based on
        // our value
        // TODO
      });
    });
  };
})(jQuery);

