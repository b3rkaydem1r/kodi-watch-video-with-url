import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


kb = xbmc.Keyboard('default', 'heading', True)
kb.setDefault('')
kb.setHeading('Type URL')
kb.setHiddenInput(False)
kb.doModal()
if (kb.isConfirmed()):
  video_url = kb.getText()
  xbmc.Player().play(video_url)