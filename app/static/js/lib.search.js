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

              // Map type onto each result
              results = _.flatten(_.map(res, function(v, k){
                return _.map(v, function(i){
                  return _.extend(i, {type: k.slice(0, -1)});
                });
              }));
              next(_.keys(results));
            });
        }, 200),
        minLength: 1,
        matcher: function(item) {
          // Reset internal value
          $this.data('value', null);
          for (var key in results[item])
            if (results[item][key].toString().toLowerCase().indexOf(this.query.toLowerCase()) >= 0)
              return true;
          return false;
        },
        sorter: function(items) {
          // Prioritize name, and prioritize begins-with
          var query = this.query.toLowerCase(),
              sorters = [ [], [], [], [] ];

          // Sorter index is calculated through boolean logic
          // 2 bit (00, 01, 10, 11)
          // least significant bit is key != name
          // most significant bit is contains > 0
          while (item = items.shift()) {
            // Start out out-of-index
            var index = sorters.length;
            for (var key in results[item]) {
              var contains = results[item][key].toString().toLowerCase().indexOf(query);
              if (contains >= 0)
                index = Math.min(index, (key != 'name') + ((contains > 0) << 1));
            }
            sorters[index].push(item);
          }
          return [].concat.apply([], sorters);
        },
        updater: function(item) {
          // Set internal value
          $this.data('value', results[item].key);
          $this.trigger('errors'); // Clear
          return results[item].name;
        },
        highlighter: function(item) {
          // The html returned here will be output in each cell in the chooser
          return $.render('search_result', results[item]);
        },
      });

      $this.on('blur', function(e){
        setTimeout(function(){
          // If we don't have an internal value set, we need to warn user
          if ($this.val() && !$this.data('value'))
            $this.trigger('errors', [["You must select an option from the search drop-down"]]);
        }, 500);
      });
    });
  };
})(jQuery);

