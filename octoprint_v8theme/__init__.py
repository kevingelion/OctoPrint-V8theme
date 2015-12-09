# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask

class V8themePlugin(octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.SimpleApiPlugin,
                    octoprint.plugin.StartupPlugin):
    def get_assets(self):
        return dict(
            js=['js/v8theme.js'],
            css=['css/main.css']
            #less=['less/my_styles.less']
        )

    def get_settings_defaults(self):
        return dict(
            printer_name=""
        )

    def on_after_startup(self):
        self.printer_name = self._settings.get(["printer_name"])

    def on_api_get(self, request):
        if self.printer_name:
            return flask.jsonify(printerName=self.printer_name)
        else:
            return flask.jsonify(printerName="")

def get_update_information(*args, **kwargs):
    return dict(
        v8theme=dict(
            type="github_commit",
            user="Voxel8",
            repo="OctoPrint-V8theme",
            branch='master',
            pip="https://github.com/Voxel8/OctoPrint-V8theme/archive/{target_version}.zip",
        )
    )

def __plugin_load__():
    global __plugin_implementation__
    global __plugin_hooks__
    __plugin_implementation__ = V8themePlugin()

    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": get_update_information,
    }
