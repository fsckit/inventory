(function($){
  var Autocomplete = (function(){
    var handlers = { };

    function Autocomplete(field) {
      this.$el = $('<ul>', { class: 'autocomplete' });
      this.selected = 0;
      this.tracking = field;

      this.tracking.on('keypress', _.bind(this.change, this));
    }

    Autocomplete.prototype.show = function(options){
      if (options)
        this.options = options;
    };

    Autocomplete.prototype.hide = function(){
      this.$el.hide();
    };

    Autocomplete.prototype.change = function(e){
      if (typeof handlers[e.keyCode] === 'function')
        handlers[e.keyCode].call(this, e);
      else
        this.render();
    };

    Autocomplete.prototype.choose = function() {
      this.tracking.data('value', this.options[this.selected].value);
      this.hide();
    };

    Autocomplete.prototype.render = function() {
      if (!this.$el.is(':visible'))
        this.show();
    };

    handlers[Keys.TAB] = function() {
      this.choose();
    };
    handlers[Keys.ENTER] = handlers[Keys.TAB];
    handlers[Keys.UP] = function() {
      this.selected = Math.max(this.selected + 1, this.options.length - 1);
      this.render();
    };
    handlers[Keys.DOWN] = function() {
      this.selected = Math.min(this.selected - 1, 0);
      this.render();
    };
    handlers[Keys.ESC] = function() {
      this.hide();
    };

    return Autocomplete;
  });
  
  $.fn.autocomplete = function(options) {
    this.each(function(){
      var $this = $(this);

      if (!$this.data('autocomplete')) {
        $this.data('autocomplete', new Autocomplete($this));
      }
      $this.data('autocomplete').show(options);
    });
  };
})(jQuery);
