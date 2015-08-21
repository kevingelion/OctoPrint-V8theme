$(function() {
    function V8ThemeViewModel(parameters) {
        var self = this;

        self.onAllBound = function() {
            // Everything is added to the Temperature tab because the graph is
            // wired to redraw when it is selected.
            $("#control_link").remove();
            $("#temp_link").addClass("active");
            $("#temp_link").text("Control");
            $("#temp").append($("#control").contents());
            $("#temp").addClass("active");
        };
    }

    OCTOPRINT_VIEWMODELS.push([
        V8ThemeViewModel,
        [],
        ""
    ]);
});
