# -*- coding: utf-8 -*-
import unittest2 as unittest

from Products.BrFieldsAndWidgets.testing import INTEGRATION_TESTING

PROJECTNAME = 'Products.BrFieldsAndWidgets'


class TestValidorsRegistration(unittest.TestCase):

    layer = INTEGRATION_TESTING

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
        self.failUnlessEqual(v('11987772121'), 1)
        self.failIfEqual(v('11887772121'), 1)
        self.failIfEqual(v('21987772121'), 1)


class TestCPFValidator(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        from Products.validation import validation
        portal = self.layer['portal']
        self.portal = portal
        self.v = validation.validatorFor('isCPF')

    def test_cpf_unformatted(self):
        self.failUnlessEqual(self.v('81057807559'), 1)
        self.failIfEqual(self.v('81057807554'), 1)
        self.failIfEqual(self.v('810578075xx'), 1)

    def test_cpf_formatted(self):
        self.failUnlessEqual(self.v('810.578.075-59'), 1)
        self.failUnlessEqual(self.v('810.578.075/59'), 1)
        self.failIfEqual(self.v('810.578.075-54'), 1)
        self.failIfEqual(self.v('810.578.075/xx'), 1)

    def test_cpf_wrong_size(self):
        self.failIfEqual(self.v('8105780755'), 1)
        self.failIfEqual(self.v('810.5782075/59'), 1)
        self.failIfEqual(self.v('810.578.075-542'), 1)
        self.failIfEqual(self.v('8103578.075399'), 1)


class TestCNPJValidator(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        from Products.validation import validation
        portal = self.layer['portal']
        self.portal = portal
        self.v = validation.validatorFor('isCNPJ')

    def test_cnpj_unformatted(self):
        self.failUnlessEqual(self.v('90656353000137'), 1)
        self.failUnlessEqual(self.v('00000000000191'), 1)
        self.failIfEqual(self.v('90656353000134'), 1)
        self.failIfEqual(self.v('10000000000191'), 1)

    def test_cnpj_formatted(self):
        self.failUnlessEqual(self.v('90.656.353/0001-37'), 1)
        self.failUnlessEqual(self.v('00.000.000/0001-91'), 1)
        self.failIfEqual(self.v('90.656.353/0001-34'), 1)
        self.failIfEqual(self.v('10.000.000/0001-91'), 1)

    def test_cnpj_wrong_size(self):
        self.failIfEqual(self.v('9065635300017'), 1)
        self.failIfEqual(self.v('90.656.35300001-37'), 1)
        self.failIfEqual(self.v('000000000000191'), 1)
        self.failIfEqual(self.v('00.000.0000001-911'), 1)
        self.failIfEqual(self.v('90.656.3530/000134'), 1)
        self.failIfEqual(self.v('10.000.000/0001-921'), 1)


class TestCEPValidator(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        from Products.validation import validation
        portal = self.layer['portal']
        self.portal = portal
        self.v = validation.validatorFor('isCEP')

    def test_cep_unformatted(self):
        self.failUnlessEqual(self.v('05421001'), 1)
        self.failUnlessEqual(self.v('03087000'), 1)
        self.failIfEqual(self.v('0308700x'), 1)
        self.failIfEqual(self.v('0542100x'), 1)

    def test_cep_formatted(self):
        self.failUnlessEqual(self.v('05421-001'), 1)
        self.failUnlessEqual(self.v('03087-000'), 1)
        self.failIfEqual(self.v('03087-00x'), 1)
        self.failIfEqual(self.v('05421-00x'), 1)


class TestPhoneValidator(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        from Products.validation import validation
        portal = self.layer['portal']
        self.portal = portal
        self.v = validation.validatorFor('isBrPhone')

    def test_phone_unformatted(self):
        self.failUnlessEqual(self.v('1138982121'), 1)
        self.failUnlessEqual(self.v('1120953000'), 1)
        self.failUnlessEqual(self.v('08007764832'), 1)
        self.failUnlessEqual(self.v('03007897771'), 1)
        self.failIfEqual(self.v('38982121'), 1)
        self.failIfEqual(self.v('2920953000'), 1)
        self.failIfEqual(self.v('18007764832'), 1)
        self.failIfEqual(self.v('33007897771'), 1)

    def test_phone_formatted(self):
        self.failUnlessEqual(self.v('(11)3898.2121'), 1)
        self.failUnlessEqual(self.v('(11)2095.3000'), 1)
        self.failUnlessEqual(self.v('0800-776-4832'), 1)
        self.failUnlessEqual(self.v('0300-789-7771'), 1)
        self.failIfEqual(self.v('3898-2121'), 1)
        self.failIfEqual(self.v('(29)2095.3000'), 1)
        self.failIfEqual(self.v('1800-776-4832'), 1)
        self.failIfEqual(self.v('3300-789-7771'), 1)

    def test_phone_with_international_codes(self):
        self.failIfEqual(self.v('+55(11)3898.2121'), 1)
        self.failIfEqual(self.v('+55(11)2095.3000'), 1)
        self.failIfEqual(self.v('+550800-776-4832'), 1)
        self.failIfEqual(self.v('+550300-789-7771'), 1)
        self.failIfEqual(self.v('+553898-2121'), 1)
        self.failIfEqual(self.v('+55(29)2095.3000'), 1)
        self.failIfEqual(self.v('+551800-776-4832'), 1)
        self.failIfEqual(self.v('+553300-789-7771'), 1)

    def test_phone_with_letters(self):
        self.failIfEqual(self.v('(11)3333PORTO'), 1)
        self.failIfEqual(self.v('113333PORTO'), 1)
        self.failIfEqual(self.v('11-3333-PORTO'), 1)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
