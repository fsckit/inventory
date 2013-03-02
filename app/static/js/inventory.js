(function($){
  // Subscribe via socket.io
  var socket = io.connect('/subscribe', {transports: ['xhr-polling']});
  socket.on('update', function(data){
    $('#transaction-history').trigger('update');
  });

  // Events
  $(function(){
    // View tabs trigger load events
    ['customer', 'item'].forEach(function(type){
      $('#stage').on('show', '#' + type + ' .view', function(e) {
        $(e.target.hash).text('Refreshing...').load('/' + type + '/index', function(){
          $(this).find('table.sortable').tablesorter();
        });
      });
    });

    // Load initial history
    $('#transaction-history').on('update', function(){
      $(this).load('/transaction/index');
    }).trigger('update');

    // History timer
    setInterval(function(){
      $('#transaction-history td.time').each(function(){
        $(this).text(new Date($(this).data('time') * 1000).time_since());
      });
    }, 1000);

    // Set up search/autocomplete fields
    $(':input.search').search();

    // Set up create buttons
    $('.tab-pane.create form').on('submit', function(e){
      var $this = $(this);
      e.preventDefault();

      // Clear all current errors
      $this.add(':input', $this).trigger('errors', null);

      // Build form data and replace internal .data() values
      var formData = new FormData($this.get(0));
      $this.find(':input.search').each(function(){
        if ($(this).data('value'))
          formData.append($(this).attr('name'), $(this).data('value'));
      });

      // Post the form data to the endpoint described in the form
      $.ajax({
        type: 'POST',
        url: $this.attr('action'),
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
      })
      .done(function(result){
        if (result.success) {
          // Reset the form and focus the transaction form
          if (result.message)
            $.success(result.message);
          $this.get(0).reset();
          $('#transaction :input:first').focus();
          // Also reload the transaction list -- this could use some cleaning up
          // in the future.
          $('#transaction-history').trigger('update');
          // Force everyone else's update
          socket.emit('transaction');
        } else if (result.errors) {
          // Display errors inline
          for (var field in result.errors) {
            var errors = result.errors[field];
            if (field == '__all__') {
              $this.trigger('errors', [errors]);
            } else {
              $this.find('[name=' + field + ']').trigger('errors', [errors]);
            }
          }
        }
      });
    });

    $('form[action]').each(function(){
      var $this = $(this);

      // Create error display
      var $err = $('<div>', {class: 'alert alert-error'}).prependTo($this.find('fieldset')).hide();

      // Error handler on form
      $this.on('errors', function(e, errors) {
        // Temporarily dump in error handler
        if (errors) {
          $err.text(errors[0]).show();
        } else {
          $err.text('').hide();
        }
      });
    });

    // Error handlers on fields
    $('form fieldset :input').each(function(){
      var $this = $(this);

      // Create error display
      var $err = $('<div>', {class: 'error'}).insertAfter($this).hide();

      // Bind event listener
      var $group = $this.closest('.control-group');
      $this.on('errors', function(e, errors) {
        e.stopPropagation();
        if (errors) {
          $err.tooltip('destroy');
          $err.tooltip({
            placement: $.tip_direction,
            trigger: 'hover',
            title: errors.join('\n'),
          }).show();
          $group.addClass('error');
        } else {
          $err.hide();
          $group.removeClass('error');
        }
      });
    });

    // Set up cancel buttons on update forms
    $('input.btn.cancel').on('click', function(e){
      e.preventDefault();
      document.location = '/';
    });

    // Index view tables
    $(document).on('click', 'table.index a, .popover-show', function(e){
      var $this = $(this);
      e.preventDefault();
      e.stopPropagation();
      // Load data
      $.get($this.attr('href'))
        .done(function(contents){
          var $contents = $(contents);

          // Close all other popovers
          $(document).trigger('click');

          $this.popover({
            html: true,
            trigger: 'manual',
            title: $contents.find('legend').remove().text(),
            content: $contents.html(),
            placement: $.tip_direction,
          }).popover('show');

          // Register one time close when you click outside of the popover; and
          // manually destroy because if the element was removed (modal link)
          // then we lose reference to the popover data object.
          var popover = $this.data('popover');
          $(document).one('click', function(e) {
            popover.destroy();
          });
        })
    });
    // Catch clicks on popovers so we don't close them
    $(document).on('click', '.popover', function(e){
      e.stopPropagation();
    });

    // Summaries
    $('#item-summary').on('click', function(e){
      e.preventDefault();
      // Load into temporary div
      $('<div>').load(e.target.href, function(){
        $.modal('Item Summary', this);
      }).remove();
    });
    $('#customer-summary').on('click', function(e){
      e.preventDefault();
      // Load into temporary div
      $('<div>').load(e.target.href, function(){
        $.modal('Customer Summary', this);
      }).remove();
    });

    // Resize window
    $(window).on('resize', function(){
      var height = $(this).height();
      $("#stage .index-scroll").css('max-height', (height - 200) / 2);
    }).trigger('resize');

    // Auto select for physical id
    $('#id_label_id').keyup(function(){
      var type = $(this).val().charAt(0).toLowerCase();

      var $select = $('#id_type').val(type);
      if (!$select.val() && type)
        $(this).trigger('errors', [["Invalid id letter: '" + type.toUpperCase() + "'"]]);
      else
        $(this).trigger('errors', null);
    });
  });
})(jQuery);
