# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from Products.BrFieldsAndWidgets.testing import INTEGRATION_TESTING

PROJECTNAME = 'Products.BrFieldsAndWidgets'


class BaseTestCase(unittest.TestCase):
    """base test case to be used by other tests"""

    layer = INTEGRATION_TESTING

    def setUpUser(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Editor', 'Reviewer'])
        login(self.portal, TEST_USER_NAME)

    def setUp(self):
        portal = self.layer['portal']
        self.portal = portal
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.pp = getattr(self.portal, 'portal_properties')
        self.st = getattr(self.portal, 'portal_setup')
        self.skins = getattr(self.portal, 'portal_skins')
        self.setUpUser()


class TestInstall(BaseTestCase):
    """ensure product is properly installed"""

    def test_installed(self):
        PROJECTNAME = 'BrFieldsAndWidgets'
        self.failUnless(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_skin_layer_installed(self):
        self.failUnless('BrF_images' in self.skins.objectIds())
        self.failUnless('BrF_templates' in self.skins.objectIds()) 


class TestUninstall(BaseTestCase):
    """ensure product is properly uninstalled"""

    def setUp(self):
        BaseTestCase.setUp(self)
        PROJECTNAME = 'BrFieldsAndWidgets'
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        PROJECTNAME = 'BrFieldsAndWidgets'
        self.failIf(self.qi.isProductInstalled(PROJECTNAME))

    def test_skin_layer_uninstalled(self):
        self.failIf('BrF_images' in self.skins.objectIds())
        self.failIf('BrF_templates' in self.skins.objectIds()) 


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
