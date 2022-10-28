$(function()
{
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data, res){
        $('#character').text(data.name);
    });
});