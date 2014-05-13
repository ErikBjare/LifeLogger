
function cell_onclick(e) {
    e.target = $(e.target);
    var text = e.target.text();
    e.target.text('');
    function save_cell() {
        var newText = $('#curr_input').val();
        e.target.text(newText).parent().find('input').remove();
    }
    textbox = $('<input type="text" class="input" id="curr_input"/>');
    textbox.appendTo(e.target).val(text).select();
    //textbox.blur(save_cell);
    textbox.bind("enterKey", save_cell);
    textbox.keyup(function(e){
        if(e.keyCode == 13) $(this).trigger("enterKey");
    });
}

function init() {
    cells = $("td.cell");
    cells.click(cell_onclick);
}


$(document).ready(init);
