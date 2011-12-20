PROJECTNAME = "BrFieldsAndWidgets"
SKINS_DIR = 'skins'
GLOBALS = globals()

try:
    from Products.CMFCore.permissions import AddPortalContent
except:
    from Products.CMFCore.CMFCorePermissions import AddPortalContent

ADD_CONTENT_PERMISSION = AddPortalContent

try:
    # Plone 4 and higher
    import plone.app.upgrade
    USE_BBB_VALIDATORS = False
except ImportError:
    # BBB Plone 3
    USE_BBB_VALIDATORS = True
