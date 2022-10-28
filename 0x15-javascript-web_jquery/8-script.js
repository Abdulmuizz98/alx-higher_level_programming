$(function()
{
    let result
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data, res){
        data.results.forEach(e => {
            $('ul#list_movies').append(`<li>${e.title}</li>`);
        });
     });
});