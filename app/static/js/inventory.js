(function($){
  // Events
  $(function(){
    // View tabs trigger load events
    ['customer', 'item'].forEach(function(type){
      $('#stage').on('show', '#' + type + ' .view', function(e) {
        $(e.target.hash).load('/' + type + '/index');
      });
    });

    // Load initial history
    $('#transaction-history').load('/transaction/index');

    // Set up search/autocomplete fields
    $(':input.search').search();

    // Set up create buttons
    $('.tab-pane.create form').on('submit', function(e){
      var $this = $(this);
      e.preventDefault();

      // Post the form data to the endpoint described in the form
      $.ajax({
        type: 'POST',
        url: $this.attr('action'),
        data: new FormData($this.get(0)),
        dataType: 'json',
        contentType: false,
        processData: false,
      })
      .done(function(result){
        if (result.success) {
          // Reset the form and focus the transaction form
          $this.get(0).reset();
          $('#transaction :input:first').focus();
        } else if (result.errors) {
          // Display errors inline
          for (var field in result.errors) {
            var errors = result.errors[field];
            if (field == '__all__') {
              $this.trigger('errors', errors);
            } else {
              $this.find('[name=' + field + ']').trigger('errors', errors);
            }
          }
        }
      });
    });

    // Set up cancel buttons on update forms
    $('input.btn.cancel').on('click', function(e){
      e.preventDefault();
      document.location = '/';
    });
  });
})(jQuery);
