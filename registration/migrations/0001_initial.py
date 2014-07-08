# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'registration_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('skill', self.gf('django.db.models.fields.IntegerField')()),
            ('wants_shirt', self.gf('django.db.models.fields.BooleanField')()),
            ('wants_frisbee', self.gf('django.db.models.fields.BooleanField')()),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'registration', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'registration_player')


    models = {
        u'registration.player': {
            'Meta': {'object_name': 'Player'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'skill': ('django.db.models.fields.IntegerField', [], {}),
            'wants_frisbee': ('django.db.models.fields.BooleanField', [], {}),
            'wants_shirt': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['registration']