import xbmcaddon
import os
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
ADDONTITLE = '[COLOR limegreen][B]Chef[/B][/COLOR]Wizard'
BUILDERNAME = 'ChefWizard'
EXCLUDES = []
BUILDFILE = 'https://raw.githubusercontent.com/Witty11444/kodibuild_arctic/refs/heads/main/builds.txt'
UPDATECHECK = 0
APKFILE = 'http://'
YOUTUBETITLE = ''
YOUTUBEFILE = 'http://'
ADDONFILE = 'http://'
ADVANCEDFILE = 'http://'
ICONBUILDS = os.path.join(ART, 'builds.png')
HIDESPACERS = 'No'
SPACER = '='
COLOR1 = 'limegreen'
COLOR2 = 'white'
THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]Chef[/B][/COLOR][COLOR {color2}]Wizard[COLOR {color1}])[/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
HIDECONTACT = 'No'
CONTACT = 'Thank you for choosing ChefWizard.'
AUTOUPDATE = 'No'
AUTOINSTALL = 'No'
ENABLE = 'No'
