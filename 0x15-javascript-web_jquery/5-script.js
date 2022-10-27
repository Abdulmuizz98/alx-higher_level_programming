$(function()
{
    $('#add_item').bind('click', function(){
        $('ul.my_list').append('<li>Item</li>');
    });
});