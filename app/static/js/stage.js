$(document).ready(function() {
  // show/hide button click
  $('.toggle').click(function() {
    var $form = $(this).parent().next() ; 
    var $btn = $(this) 
	// toggle visibility of next toggle element
    $form.toggle( function(){
	  // change show/hide text of button
      if ($form.is(':visible')) {
        $btn.val('Hide')
      } else {
        $btn.val('Show')
      }

    });
    });
});   