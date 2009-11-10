## Script (Python) "lstDDD"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=obj=None
##title=
##

lstCodArea = [11, # Grande Sao Paulo
          12, 
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          21,
          22, # Interior do RJ
          24,
          27,
          28, # Interior do ES
          31,
          32,
          33,
          34,
          35,
          37,
          38,
          41,
          42,
          43,
          44,
          45,
          46,
          47,
          48,
          49,
          51,
          53,
          54,
          55,
          61,
          62,
          63,
          64, # Interior de GO
          65,
          66, # Interior do MT
          67,
          68,
          69,
          71,
          73,
          74,
          75,
          77,
          79,
          81,
          82,
          83,
          84,
          85,
          86,
          87,
          88,
          89, # Interior do PI
          91,
          92,
          93, # Interior do PA
          94, # Interior do PA
          95,
          96,
          97, # Interior do AM
          98,
          99, # Interior do MA
          '0300',
          '0500',
          '0800',]
         
lstTupCodArea = [(item, item) for item in lstCodArea]     
lstReturn = [('','--')]

return lstReturn + lstTupCodArea