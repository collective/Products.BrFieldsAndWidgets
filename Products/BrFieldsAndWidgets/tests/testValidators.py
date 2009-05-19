from unittest import TestSuite, makeSuite
from Products.Archetypes.tests.atsitetestcase import ATSiteTestCase


class TestValidation(ATSiteTestCase):

    def test_cpf_registration(self):
        from Products.validation import validation
        v = validation.validatorFor('isCPF')
        self.failUnlessEqual(v('81057807559'), 1)
        self.failIfEqual(v('8105780755x'), 1)

    def test_cnpj_registration(self):
        from Products.validation import validation
        v = validation.validatorFor('isCNPJ')
        self.failUnlessEqual(v('90.656.353/0001-37'), 1)
        self.failIfEqual(v('90.656.353/0001-36'), 1)

    def test_cep_registration(self):
        from Products.validation import validation
        v = validation.validatorFor('isCEP')
        self.failUnlessEqual(v('05417-010'), 1)
        self.failIfEqual(v('05417'), 1)
        
    def test_phone_registration(self):
        from Products.validation import validation
        v = validation.validatorFor('isBrPhone')
        self.failUnlessEqual(v('(11)38982121'), 1)
        self.failIfEqual(v('113898-212121'), 1)

def test_suite():
    suite = TestSuite()
    
    suite.addTest(makeSuite(TestValidation))

    return suite