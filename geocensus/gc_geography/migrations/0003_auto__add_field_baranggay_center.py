# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Baranggay.center'
        db.add_column(u'gc_geography_baranggay', 'center',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Baranggay.center'
        db.delete_column(u'gc_geography_baranggay', 'center')


    models = {
        u'gc_geography.baranggay': {
            'Meta': {'object_name': 'Baranggay'},
            'center': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'polygon': ('django.contrib.gis.db.models.fields.PolygonField', [], {})
        }
    }

    complete_apps = ['gc_geography']