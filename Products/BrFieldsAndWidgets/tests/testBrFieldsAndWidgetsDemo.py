import os, sys

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Testing import ZopeTestCase
from Products.BrFieldsAndWidgets.tests.tests import TestCase
from Products.Archetypes.public import *

class TestFields(TestCase):
    """ Unit test cases for BrFieldsAndWidgets fields definition """

    def afterSetUp(self):
        self.loginAsPortalOwner()
        self.portal.invokeFactory('BrFieldsAndWidgetsDemo', 'demo')
        self.demo = self.portal.demo


    def testCpfFill(self):
        """ Test that it is possible to enter data in a Cpf Field"""
        self.demo.setCpf('81057807559')
        self.field = self.demo.getField('cpf')
    
    def testCnpjFill(self):
        """ Test that it is possible to enter data in a CNPJ Field"""
        self.demo.setCnpj('90.656.353/0001-37')
        self.field = self.demo.getField('cnpj')

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestFields))
    return suite

if __name__ == '__main__':
    framework()
