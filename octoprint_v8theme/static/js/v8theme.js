$(function() {
    function V8ThemeViewModel(parameters) {
        var self = this;

        self.onAllBound = function() {
            $("#temp_link").remove();
            $("#control_link").addClass("active");
            $("#control").prepend($("#temp").contents());
            $("#control").addClass("active");
        };
    }

    OCTOPRINT_VIEWMODELS.push([
        V8ThemeViewModel,
        [],
        ""
    ]);
});
