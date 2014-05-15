# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Baranggay'
        db.create_table(u'gc_geography_baranggay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('polygon', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
        ))
        db.send_create_signal(u'gc_geography', ['Baranggay'])


    def backwards(self, orm):
        # Deleting model 'Baranggay'
        db.delete_table(u'gc_geography_baranggay')


    models = {
        u'gc_geography.baranggay': {
            'Meta': {'object_name': 'Baranggay'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'polygon': ('django.contrib.gis.db.models.fields.PolygonField', [], {})
        }
    }

    complete_apps = ['gc_geography']