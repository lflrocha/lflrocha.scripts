# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
import datetime
import DateTime

from plone.app.textfield.value import RichTextValue



vet = [
  { "id": "03-02-17-a-voz.mp3"},
]


app.radio


for item in vet:

    id = item['id']

    result = app.radio.portal_catalog(Type="File",  id=id)

    if len(result)>0:
        obj = result[0].getObject()

        data = datetime.datetime(2017, 02, 03, 19, 30)

        obj.creation_date = data
        obj.setModificationDate(data)
        obj.reindexObject()

    else:
        print data


# Commit transaction
import transaction; transaction.commit()
# Perform ZEO client synchronization (if running in clustered mode)
app._p_jar.sync()
