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

    $('#select-date #year').on('change',function(){ changeTransactionDate(); });
    $('#select-date #month').on('change',function(){ changeTransactionDate(); });

    function changeTransactionDate(){
        var yearInput = $('#select-date #year'),
            mothSelect = $('#select-date #month'),
            link = $('#select-date #date-link');

        link.attr('href', link.attr('link') + mothSelect.val() + '.' + yearInput.val() )
    }

});