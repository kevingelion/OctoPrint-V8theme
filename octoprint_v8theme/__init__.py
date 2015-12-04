# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class V8themePlugin(octoprint.plugin.AssetPlugin):
    def get_assets(self):
        return dict(
            js=['js/v8theme.js'],
            css=['css/main.css']
            #less=['less/my_styles.less']
        )


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
