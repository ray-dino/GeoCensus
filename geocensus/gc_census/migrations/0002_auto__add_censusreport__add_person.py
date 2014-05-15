# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CensusReport'
        db.create_table(u'gc_census_censusreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')()),
            ('structure_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('annual_income', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'gc_census', ['CensusReport'])

        # Adding model 'Person'
        db.create_table(u'gc_census_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('census_report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gc_census.CensusReport'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('employment_status', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'gc_census', ['Person'])


    def backwards(self, orm):
        # Deleting model 'CensusReport'
        db.delete_table(u'gc_census_censusreport')

        # Deleting model 'Person'
        db.delete_table(u'gc_census_person')


    models = {
        u'gc_census.censusreport': {
            'Meta': {'object_name': 'CensusReport'},
            'annual_income': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'create_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'structure_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gc_census.person': {
            'Meta': {'object_name': 'Person'},
            'census_report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gc_census.CensusReport']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'employment_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['gc_census']