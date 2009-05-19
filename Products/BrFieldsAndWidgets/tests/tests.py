import unittest
import doctest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import Products.BrFieldsAndWidgets

ztc.installProduct('BrFieldsAndWidgets')

@onsetup
def setup_product():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', Products.BrFieldsAndWidgets)
    fiveconfigure.debug_mode = False

setup_product()

ptc.setupPloneSite(extension_profiles=['Products.BrFieldsAndWidgets:default',
                                       'Products.BrFieldsAndWidgets:example',])

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):

        @classmethod
        def tearDown(cls):
            pass
    

def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='Products.BrFieldsAndWidgets',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='Products.BrFieldsAndWidgets.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'validators.txt', package='Products.BrFieldsAndWidgets.tests',
            test_class=TestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | 
                        doctest.NORMALIZE_WHITESPACE | 
                        doctest.ELLIPSIS),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
