$(function() {
    function V8ThemeViewModel(parameters) {
        var self = this;
        self.temp = parameters[0]

        self.onAllBound = function() {
            $("#temp_link").remove();
            $("#control_link").addClass("active");
            $("#control").prepend($("#temp").contents());
            $("#control").addClass("active");
        };

        self.onAfterTabChange = function(current, previous) {
            if (current != "#control") {
                return;
            }
            self.temp.updatePlot();
        }

    }

    OCTOPRINT_VIEWMODELS.push([
        V8ThemeViewModel,
        ["temperatureViewModel"],
        ""
    ]);
});
