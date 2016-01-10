import xbmcaddon, os
from xbmc import translatePath

addonID = 'plugin.video.xstream'
addon = xbmcaddon.Addon(id = addonID)
addonPath = translatePath(addon.getAddonInfo('path')).decode('utf-8')
profilePath = translatePath(addon.getAddonInfo('profile')).decode('utf-8')
settings_file = os.path.join(addonPath, 'resources', 'settings.xml')
