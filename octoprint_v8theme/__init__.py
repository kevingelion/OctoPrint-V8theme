# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class V8themePlugin(octoprint.plugin.AssetPlugin):
    def get_assets(self):
        return dict(
            #js=['js/my_file.js', 'js/my_other_file.js'],
            css=['css/main.css'],
            #less=['less/my_styles.less']
        )

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "V8theme Plugin"


def get_update_information(self, *args, **kwargs):
    return dict(
        v8theme_plugin=dict(
            type="github_commit",
            user="Voxel8",
            repo="OctoPrint-V8theme",
            branch='master',
            pip="https://github.com/Voxel8/OctoPrint-V8theme/archive/{target_version}.zip",
        )
    )

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = V8themePlugin()

    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": get_update_information,
    }
