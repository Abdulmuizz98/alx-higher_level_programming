$(function()
{
    $('input#btn_translate').bind('click', function() {
        let lang = $('input#language_code').val();
        $.get(`https://stefanbohacek.com/hellosalut/?lang=${lang}`, function(data, res){
            $('div#hello').text(data.hello);
        });
    })
});