function init() {
    resize();
    $(window).resize(resize);
}

function resize() {
    var el = $(".container");
    el.height($(window).height() - el.offset().top - 10);
}


$(window).ready(init);
