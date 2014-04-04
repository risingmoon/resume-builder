$(document).ready(function(){
    $('.add').on('click', function () {
        var number = +$("#id_web_set-TOTAL_FORMS").val()
       $("#id_web_set-TOTAL_FORMS").val(number+1);
        $('.web').append('<div class="form-group">' +
            '<div class="col-sm-offset-4 col-sm-4">' +
            '<label for="id_web_set-'  + number + '-account">Account:</label>' +
            '<input class="col-sm-4 form-control" id="id_web_set-' + number + '-account" '+
            'maxlength="50" name="web_set-' + number + '-account" placeholder="Account" type="text">' +
            '<label for="id_web_set-' + number + '-DELETE">Delete:</label>' +
            '<input id="id_web_set-' + number + '-DELETE" name="web_set-' + number + '-DELETE" type="checkbox">' +
            '<input id="id_web_set-' + number + '-profile" name="web_set-' + number + '-profile" type="hidden" value="3">' +
            '<input id="id_web_set-' + number + '-id" name="web_set-' + number + '-id" type="hidden"></div></div>');
    });
});