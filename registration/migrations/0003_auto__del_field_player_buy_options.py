# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Player.buy_options'
        db.delete_column(u'registration_player', 'buy_options')


    def backwards(self, orm):
        # Adding field 'Player.buy_options'
        db.add_column(u'registration_player', 'buy_options',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1),
                      keep_default=False)


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