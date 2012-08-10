# -*- coding: utf-8 -*-
__author__ = '''Simples Consultoria'''
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.component import queryUtility

from Products.validation.interfaces import ivalidator
from zope.schema.interfaces import IVocabularyFactory

from Products.validation.config import validation
from Products.validation.interfaces.IValidator import IValidator

from Products.BrFieldsAndWidgets import MessageFactory as _
from Products.BrFieldsAndWidgets.config import USE_BBB_VALIDATORS

listValidators = []


class ValidadorCPF:
    """
    Validador para verificar se o CPF informado e valido
    Baseado em http://www.pythonbrasil.com.br/moin.cgi/VerificadorDeCPF .
    """

    if USE_BBB_VALIDATORS:
        __implements__ = (ivalidator, )
    else:
        implements(IValidator)

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kw):
        cpf = value
        cpf = ''.join([c for c in value if c.isdigit()])

        if len(cpf) != 11:
            return _(u"CPF precisa ter 11 dígitos.")
        elif len(cpf)==11:
            vtemp = [int(cpf[:1]) for i in list(cpf)]
            cpf2 = [int(i) for i in list(cpf)]
            if cpf2 == vtemp:
                return _(u"CPF inválido.")

            tmp = cpf[:9]
            ltmp = [int(i) for i in list(tmp)]

            while len(ltmp) < 11:
                R = sum(map(lambda(i, v): (len(ltmp)+1-i)*v,
                                         enumerate(ltmp))) % 11

                if R > 1:
                    f = 11 - R
                else:
                    f = 0
                ltmp.append(f)

            if cpf2 != ltmp:
                return _(u"O dígito verificador do CPF não confere.")
        return True


listValidators.append(ValidadorCPF('isCPF',
                                   title=_(u'Validator de CPF'),
                                   description=''))


class ValidadorCNPJ:
    """
    Validador para verificar se o CNPJ informado e valido.
    Baseado em http://www.pythonbrasil.com.br/moin.cgi/VerificadorDeCnpj
    """

    if USE_BBB_VALIDATORS:
        __implements__ = (ivalidator, )
    else:
        implements(IValidator)

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kw):
        digits = [int(c) for c in value if c.isdigit()]
        if len(digits) != 14:
            return _(u"O CNPJ deve ter 14 dígitos.")
        cnpj = digits[:12]
        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        while len(cnpj) < 14:
            r = sum([x*y for (x, y) in zip(cnpj, prod)])%11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            cnpj.append(f)
            prod.insert(0, 6)
        return ((cnpj == digits) and True) or \
                _(u"O CNPJ informado é inválido.")


listValidators.append(ValidadorCNPJ('isCNPJ',
                                    title=_(u'Validator de CNPJ'),
                                    description=''))


class ValidadorCEP:
    """
    Validador para informar se o CEP informado is valido. Sao aceitos codigos
    de enderecamento postal em duas formas:Oito digitos consecutivos ou cinco
    digitos, hifen, tres digitos, ou seja, XXXXXXXX ou XXXXX-XXX, onde cada X
    pode ser qualquer digito entre 0 e 9.
    """

    if USE_BBB_VALIDATORS:
        __implements__ = (ivalidator, )
    else:
        implements(IValidator)

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kw):
        cep = ''.join([c for c in value if c.isdigit()])

        if not(len(cep)==8):
            return _(u"O cep informado é inválido.")
        return True

listValidators.append(ValidadorCEP('isCEP',
                                   title=_(u'Validator de CEP'),
                                   description=''))


class ValidadorBrPhone:
    """
    Validador para telefones brasileiros. Suportando os formatos:
        XXXXXXXXXX (11955553211) - Novos celulares
        XXXXXXXXXX (1155553211) - Novos telefones
        XXXXXXXXX  (115552133) - Antigos telefones
        0n00XXXXXXX (n sendo 3 ou 8)
        0n00XXXXXX (n sendo 3 ou 8)
    """

    if USE_BBB_VALIDATORS:
        __implements__ = (ivalidator, )
    else:
        implements(IValidator)

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kw):

        if value.startswith('+'):
            return _(u"Telefone inválido")
        phone = ''.join([c for c in value if c.isdigit()])
        len_phone = len(phone)
        status = False
#        import pdb;pdb.set_trace()
        if phone.startswith('0'):
            if self.validate_cng(phone[:4]) and (len_phone in [10, 11]):
                status = True
        elif self.validate_ddd(phone[:2]) and (len_phone in [9, 10]):
            status = True
        elif (self.validate_ddd(phone[:2])) and (phone[:2] == '11'):
            if (len_phone == 11) and  (phone[2] == '9'):
                # validate new cellphones
                status = True

        return status or _(u"Telefone inválido")

    def validate_ddd(self, value):
        util = queryUtility(IVocabularyFactory, 'brasil.ddd')
        ddd = util()
        try:
            item = ddd.by_token[value]
            return item
        except KeyError:
            return False

    def validate_cng(self, value):
        util = queryUtility(IVocabularyFactory, 'brasil.cng')
        cng = util()
        try:
            item = cng.by_token[value]
            return item
        except KeyError:
            return False


listValidators.append(ValidadorBrPhone('isBrPhone',
                                       title=_(u'Validator de Telefone'),
                                       description=''))


for validador in listValidators:
    validation.register(validador)
