# -*- coding: utf-8 -*-
# Author: CrudeCreator
# Created: 2023-12-13
# License: MIT https://goo.gl/5bMj3H

import sys
import xbmc
import xbmcplugin
import xbmcgui
import lib.menu_items as MENU
from lib.actions import Actions
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
query = ARGS.get("query", [None])[0]

def add_menu_item(menu_item, is_folder, is_playable=False):
    list_item = xbmcgui.ListItem(label=menu_item["label"])

    if "thumb" in menu_item:
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
        menu_items = menu_map.get(route, [])
        filtered_menu_items = [menu_item for menu_item in menu_items if query.lower() in menu_item["label"].lower()] if query else menu_items
        if len(filtered_menu_items) > 1:
            add_menu_item({"label": "Search...", "action": Actions.Search, "route": route}, is_folder=True)

        for menu_item in filtered_menu_items:
            add_menu_item(menu_item, is_folder=False, is_playable=True)

    
    xbmcplugin.endOfDirectory(ADDON_HANDLE, updateListing=query is not None)

elif action == Actions.Play:
    video = ARGS.get("video", [None])[0]
    if video is not None:
        list_item = xbmcgui.ListItem(path=video)
        xbmcplugin.setResolvedUrl(ADDON_HANDLE, True, list_item)

elif action == Actions.Search:
    keyboard = xbmc.Keyboard('', 'Search', False)
    keyboard.doModal()
    query = keyboard.getText().strip() if keyboard.isConfirmed() else None
    if query:
        url = format_url(action=Actions.Navigate, route=route, query=query)
        xbmcplugin.endOfDirectory(ADDON_HANDLE)
        xbmc.executebuiltin('Container.Update(%s)' % url)