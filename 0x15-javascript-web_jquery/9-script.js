$(function()
{
    $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data, res){
        $('div#hello').text(data.hello);
    });
});