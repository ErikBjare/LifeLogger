
function cell_onclick(e) {
    e.target = $(e.target);
    console.log(e.target);
    var text = e.target.text();
    e.target.text('');
    $('<input type="text" id="curr_input" style="width: 50px"/>').appendTo(e.target).val(text).select().blur(
        function(){
            var newText = $('#curr_input').val();
            console.log(newText)
            e.target.text(newText).find('input').remove();
        });
    console.log("lol")
}

function init() {
    cells = $("td.cell");
    cells.click(cell_onclick);
}


$(document).ready(init);
