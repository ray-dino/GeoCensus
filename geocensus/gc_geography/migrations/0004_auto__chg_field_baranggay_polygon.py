# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Baranggay.polygon'
        db.alter_column(u'gc_geography_baranggay', 'polygon', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')())

    def backwards(self, orm):

        # Changing field 'Baranggay.polygon'
        db.alter_column(u'gc_geography_baranggay', 'polygon', self.gf('django.contrib.gis.db.models.fields.PolygonField')())

    models = {
        u'gc_geography.baranggay': {
            'Meta': {'object_name': 'Baranggay'},
            'center': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'polygon': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {})
        }
    }

    complete_apps = ['gc_geography']