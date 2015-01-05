# -*- coding: utf-8 -*-

from module.common.json_layer import json_loads
from module.plugins.internal.MultiHook import MultiHook


class RPNetBiz(MultiHook):
    __name__    = "RPNetBiz"
    __type__    = "hook"
    __version__ = "0.13"

    __config__ = [("mode", "all;listed;unlisted", "Use for hosters (if supported):", "all"),
                  ("pluginlist", "str", "Hoster list (comma separated)", ""),
                  ("revertfailed", "bool", "Revert to standard download if download fails", False),
                  ("interval", "int", "Reload interval in hours (0 to disable)", 24)]

    __description__ = """RPNet.biz hook plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Dman", "dmanugm@gmail.com")]


    def getHosters(self):
        # Get account data
        user, data = self.account.selectAccount()

        res = self.getURL("https://premium.rpnet.biz/client_api.php",
                     get={'username': user, 'password': data['password'], 'action': "showHosterList"})
        hoster_list = json_loads(res)

        # If account is not valid thera are no hosters available
        if 'error' in hoster_list:
            return []

        # Extract hosters from json file
        return hoster_list['hosters']
