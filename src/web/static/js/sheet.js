var SheetModel = Backbone.Model.extend({
    idAttribute: "_id"
});

var SheetView = Backbone.View.extend({
  tagName: "table",
  className: "table",

//  template: _.template(),

  events: {
    "click td.cell":    "editCell"
  },

  initialize: function() {
    this.on("open", this.open, this)
    //this.listenTo(this.model, "change", this.render);
  },

  render: function() {
    this.$el.html("<div>Nothing to see here!</div>")
    return this;
  },

  editCell: function(e) {
      target = $(e.target);
      var text = target.text();
      target.text('');
      function save_cell() {
          var newText = $('#curr_input').val();
          target.text(newText).parent().find('input').remove();
      }
      textbox = $('<input type="text" class="input" id="curr_input"/>');
      textbox.appendTo(target).val(text).select();
      textbox.blur(save_cell);
      textbox.bind("enterKey", save_cell);
      textbox.keyup(function(e){
          if(e.keyCode == 13) $(this).trigger("enterKey");
      });
  }
});


function cell_onclick(e) {
}

function init() {
    cells = $("td.cell");
    cells.click(cell_onclick);
    var sheet = new SheetView({id: "sheet", el: document.getElementById("sheet")});
    console.log(sheet.$el)
}


$(document).ready(init);
