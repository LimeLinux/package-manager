#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file

from PyQt5.QtCore import QVariant, QSettings

defaults = {
            "SystemTray" : False,
            "UpdateCheck" : False,
            "InstallUpdatesAutomatically" : False,
            "UpdateCheckInterval" : 60,
           }

DATA_DIR = '/usr/share/package-manager/data/'

try:
    import appinfo
except ImportError:
    USE_APPINFO = False
else:
    USE_APPINFO = True

class Config:
    def __init__(self, organization, product):
        self.config = QSettings(organization, product)

    def setValue(self, option, value):
        if type(value) == bool:
            value = int(value)
            self.config.setValue(option, value)
        
    def value(self, option):
        return self.config.value(option)

    def getBoolValue(self, option):
        default = self._initValue(option, False)
        return True if (self.config.value(option, QVariant(default)) == "true" or self.config.value(option, QVariant(default)) == "True")  else False

    def getNumValue(self, option):
        default = self._initValue(option, 0)
        return int(self.config.value(option, QVariant(default)))#[0]

    def _initValue(self, option, value):
        if defaults.has_key(option):
            return defaults[option]
        return value

class PMConfig(Config):
    def __init__(self):
        Config.__init__(self, "Pisi", "Package-Manager")

    def showOnlyGuiApp(self):
        return int(self.value("ShowOnlyGuiApp") or 0)

    def showComponents(self):
        return int(self.value("ShowComponents") or 0)

    def showIsA(self):
        return int(self.value("ShowIsA") or 0)

    def updateCheck(self):
        return int(self.value("UpdateCheck") or 0)

    def installUpdatesAutomatically(self):
        return int(self.value("InstallUpdatesAutomatically") or 0)

    def updateCheckInterval(self):
        return self.getNumValue("UpdateCheckInterval") or 60

    def hideTrayIfThereIsNoUpdate(self):
        return int(self.value("HideTrayIfThereIsNoUpdate") or 0)

    def systemTray(self):
        return int(self.value("SystemTray") or 0)

    def setHideTrayIfThereIsNoUpdate(self, enabled):
        self.setValue("HideTrayIfThereIsNoUpdate", enabled)

    def setSystemTray(self, enabled):
        self.setValue("SystemTray", enabled)

    def setUpdateCheck(self, enabled):
        self.setValue("UpdateCheck", enabled)

    def setInstallUpdatesAutomatically(self, enabled):
        self.setValue("InstallUpdatesAutomatically", enabled)

    def setUpdateCheckInterval(self, value):
        self.setValue("UpdateCheckInterval", value)

    def setShowOnlyGuiApp(self, enabled):
        self.setValue("ShowOnlyGuiApp", enabled)

    def setShowComponents(self, enabled):
        self.setValue("ShowComponents", enabled)

    def setShowIsA(self, enabled):
        self.setValue("ShowIsA", enabled)
    
    def sync(self):
        self.config.sync()
