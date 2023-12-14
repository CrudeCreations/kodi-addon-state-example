# -*- coding: utf-8 -*-
# Author: CrudeCreator
# Created: 2023-12-13
# License: MIT https://goo.gl/5bMj3H

import sys
import xbmcplugin
import xbmcgui
import lib.menu_items as MENU
from lib.globals import Actions
from urllib.parse import parse_qs, urlencode

BASE_URL = sys.argv[0]
ADDON_HANDLE = int(sys.argv[1])
ARGS = parse_qs(sys.argv[2][1:])

def format_url(**kwargs):
    # Filter out None values to avoid url encoding them
    return f"{BASE_URL}?{urlencode({k: v for k, v in kwargs.items() if v is not None})}"

xbmcplugin.setContent(ADDON_HANDLE, "movies")

route = ARGS.get("route", [None])[0]
action = ARGS.get("action", [Actions.Navigate])[0]

def add_menu_item(menu_item, is_folder, is_playable=False):
    list_item = xbmcgui.ListItem(label=menu_item["label"])
    list_item.setArt({"thumb": menu_item["thumb"]})
    if is_playable:
        list_item.setProperty("IsPlayable", "true")

    url = format_url(action=menu_item["action"], video=menu_item.get("video"), route=menu_item.get("route"))
    xbmcplugin.addDirectoryItem(handle=ADDON_HANDLE, url=url, listitem=list_item, isFolder=is_folder)

if action == Actions.Navigate:
    if route is None:
        for menu_item in MENU.MENU_ITEMS_TOP:
            add_menu_item(menu_item, is_folder=True)
    else:
        menu_map = {
            "/animals": MENU.MENU_ITEMS_ANIMALS,
            "/cars": MENU.MENU_ITEMS_CARS,
            "/countries": MENU.MENU_ITEMS_COUNTRIES,
        }
        for menu_item in menu_map.get(route, []):
            add_menu_item(menu_item, is_folder=False, is_playable=True)

elif action == Actions.Play:
    video = ARGS.get("video", [None])[0]
    if video is not None:
        list_item = xbmcgui.ListItem(path=video)
        xbmcplugin.setResolvedUrl(ADDON_HANDLE, True, list_item)

xbmcplugin.endOfDirectory(ADDON_HANDLE)