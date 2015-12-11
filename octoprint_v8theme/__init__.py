# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask

class V8themePlugin(octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.SimpleApiPlugin,
                    octoprint.plugin.StartupPlugin):

    printer_name = ""
    def get_assets(self):
        return dict(
            js=['js/v8theme.js'],
            css=['css/main.css']
            #less=['less/my_styles.less']
        )

    def get_api_commands(self):
        return dict(
            update_printer_name=[]
        )

    def on_api_command(self, command, data):
        if command == "update_printer_name":
            self.printer_name = data.get("printer_name")
            self._plugin_manager.send_plugin_message(self._identifier, dict(printer_name=self.printer_name))

    def on_api_get(self, request):
        return flask.jsonify(printer_name=self.printer_name)

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
