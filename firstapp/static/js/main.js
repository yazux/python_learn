$(document).ready(function(){
    $('.nav-tabs a').click(function (e) {
      e.preventDefault();

      $('.nav-tabs li').removeClass('active');
      $(this.parentNode).addClass('active');

      $('.tab-content').find('.tab-pane').hide();
      $('.tab-content').find('.tab-pane').removeClass('active');

      $('.tab-content').find( $(this).attr('href') ).show();
      $('.tab-content').find( $(this).attr('href') ).addClass('active');
    });
});