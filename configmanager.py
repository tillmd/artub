# Glumol - An adventure game creator
# Copyright (C) 1998-2008  Sylvain Baubeau & Alexis Contour

# This file is part of Glumol.

# Glumol is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# Glumol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Glumol.  If not, see <http://www.gnu.org/licenses/>.

import wx
from log import log

class ConfigManager:
    def __init__(self):
        log("Loading configuration")
        self.config = wx.FileConfig("artub", "bnc", "artub.conf")
        
    def __getitem__(self, key):
        if type(key) != str:
            raise KeyError
        if not self.config.Exists(key):
            raise IndexError
        try:
           val = self.config.Read(key)
        except:
           return ''
        return val
    
    def __setitem__(self, key, item):
        if type(key) != str:
            raise KeyError
        self.config.Write(key, str(item))
    
config = ConfigManager()       