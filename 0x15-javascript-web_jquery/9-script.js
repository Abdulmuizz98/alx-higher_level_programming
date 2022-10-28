$(function()
{
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data, res){
        $('div#hello').text(data.hello);
    });
});