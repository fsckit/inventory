$(function(){
  // View tabs
  ['customer', 'item'].forEach(function(type){
    $('#stage').on('show', '#' + type + ' .view', function(e) {
      $(e.target.hash).load('/' + type + '/index');
    });
  });

  // Load history
  $('#transaction-history').load('/transaction/index');
});
