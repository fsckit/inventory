(function($){
  // Autocomplete class: includes drop down UI and event handlers for different
  // keys that may be input on a searchable text field
  var Autocomplete = (function(){
    var handlers = { };

    // Constructor creates ui element and binds event handlers
    function Autocomplete(field) {
      this.$el = $('<ul>', { class: 'autocomplete' });
      this.selected = 0;
      this.tracking = field;

      this.tracking.on('keypress', _.bind(this.change, this));
    }

    // Show the autocomplete dropdown with certain options
    Autocomplete.prototype.show = function(options){
      if (options)
        this.options = options;
    };

    // Hide the dropdown
    Autocomplete.prototype.hide = function(){
      this.$el.hide();
    };

    // Event handler for keypresses
    Autocomplete.prototype.change = function(e){
      if (typeof handlers[e.keyCode] === 'function')
        // If the special handler is defined below, use it
        handlers[e.keyCode].call(this, e);
      else
        // Otherwise they are just typing a basic character, typically
        this.render();
    };

    // When choosing an item via TAB or ENTER. Should also trigger when focus is lost
    Autocomplete.prototype.choose = function() {
      this.tracking.data('value', this.options[this.selected].value);
      this.hide();
    };

    // Updates the display of the dropdown, sorting by relevency and highlighted
    // typed parts
    Autocomplete.prototype.render = function() {
      if (!this.$el.is(':visible'))
        this.show();
    };

    // TAB and ENTER choose
    handlers[Keys.TAB] = function() {
      this.choose();
    };
    handlers[Keys.ENTER] = handlers[Keys.TAB];
    // UP and DOWN rotate selection
    handlers[Keys.UP] = function() {
      this.selected = Math.max(this.selected + 1, this.options.length - 1);
      this.render();
    };
    handlers[Keys.DOWN] = function() {
      this.selected = Math.min(this.selected - 1, 0);
      this.render();
    };
    // ESC closes
    handlers[Keys.ESC] = function() {
      this.hide();
    };

    return Autocomplete;
  });
  
  // jQuery extension that adds or updates an autocomplete class for each field
  $.fn.autocomplete = function(options) {
    this.each(function(){
      var $this = $(this);

      // Create if we have not yet and store in the data attribute
      if (!$this.data('autocomplete')) {
        $this.data('autocomplete', new Autocomplete($this));
      }
      $this.data('autocomplete').show(options);
    });
  };
})(jQuery);
