__author__  = '''Simples Consultoria'''
__docformat__ = 'plaintext'

# Python imports
import StringIO
from cStringIO import StringIO
import string

from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import ManagePortal
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.Archetypes import listTypes

# Config

def install(self):
    out=StringIO()
    
    setup_tool = getToolByName(self, 'portal_setup')
    
    setup_tool.runAllImportStepsFromProfile("profile-Products.BrFieldsAndWidgets:default", purge_old=False)

    out.write('Installation completed.\n')
    return out.getvalue()

def uninstall(self):
    out=StringIO()
    return out.getvalue()

