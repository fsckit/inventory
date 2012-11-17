(function($){
  // Events
  $(function(){
    // View tabs
    ['customer', 'item'].forEach(function(type){
      $('#stage').on('show', '#' + type + ' .view', function(e) {
        $(e.target.hash).load('/' + type + '/index');
      });
    });

    // Load history
    $('#transaction-history').load('/transaction/index');

    // Set up search/autocomplete fields
    $(':input.search').search();

    // Set up create buttons
    $('.tab-pane.create form').on('submit', function(e){
      var $this = $(this);
      e.preventDefault();

      $.ajax({
        type: 'POST',
        url: $this.attr('action'),
        data: new FormData($this.get(0)),
        dataType: 'json',
        contentType: false,
        processData: false,
      })
      .done(function(){
        $this.get(0).reset();
        $('#transaction :input:first').focus();
      })
      .fail($.err);
    });
  });
})(jQuery);
