$(function() {
    function V8ThemeViewModel(parameters) {
        var self = this;
        self.temp = parameters[0]

        self.onAllBound = function() {
            // Merge Temperature and Control tabs
            $("#temp_link").remove();
            $("#control_link").addClass("active");
            $("#control").prepend($("#temp").contents());
            $("#control").addClass("active");
            $("#temperature-graph").closest(".row").css('padding-left', '0px');
            $("#temperature-graph").closest(".row").attr('class', 'row-fluid');

            $("#settings_dialog_label").text("Settings");
            document.title = "Voxel8 DevKit";
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
