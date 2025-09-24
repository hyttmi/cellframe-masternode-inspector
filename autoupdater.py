from utils import utils
import os, json
from packaging import version
from logconfig import logger

class Autoupdater():
    def __init__(self):
        self._current_plugin_version = self.get_current_plugin_version()

    def get_current_plugin_version(self):
        try:
            with open(os.path.join(utils.get_current_script_path(), 'manifest.json'), 'r') as f:
                data = json.load(f)
                return data.get('version') # Get the version from manifest.json
        except Exception as e:
            print(f"Error reading manifest.json: {e}")
            return None

    def get_latest_plugin_version(self):
        return

    def compare_versions(self, current_version, latest_version):
        return