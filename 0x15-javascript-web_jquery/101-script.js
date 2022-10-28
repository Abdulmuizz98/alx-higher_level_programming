$(function()
{
    $('div#add_item').bind('click', function(){
        $('ul.my_list').append('<li>Item</li>');
    });
    $('div#remove_item').bind('click', function(){
        $('ul.my_list li:last-child').remove();
    });
    $('div#clear_list').bind('click', function(){
        $('ul.my_list').empty();
    });s
});