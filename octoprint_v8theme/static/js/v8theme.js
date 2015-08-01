$(window).load(function(){
    /* combine temp and control tabs */
    $("#temp_link").remove();
    $("#control_link").addClass("active");
    $("#control").prepend($("#temp").contents());
    $("#control").addClass("active");
});
