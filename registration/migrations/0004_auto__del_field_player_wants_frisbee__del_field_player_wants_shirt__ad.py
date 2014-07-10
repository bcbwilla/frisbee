# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Player.wants_frisbee'
        db.delete_column(u'registration_player', 'wants_frisbee')

        # Deleting field 'Player.wants_shirt'
        db.delete_column(u'registration_player', 'wants_shirt')

        # Adding field 'Player.want_shirt'
        db.add_column(u'registration_player', 'want_shirt',
                      self.gf('django.db.models.fields.BooleanField')(default=''),
                      keep_default=False)

        # Adding field 'Player.want_frisbee'
        db.add_column(u'registration_player', 'want_frisbee',
                      self.gf('django.db.models.fields.BooleanField')(default=''),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Player.wants_frisbee'
        raise RuntimeError("Cannot reverse this migration. 'Player.wants_frisbee' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Player.wants_frisbee'
        db.add_column(u'registration_player', 'wants_frisbee',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Player.wants_shirt'
        raise RuntimeError("Cannot reverse this migration. 'Player.wants_shirt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Player.wants_shirt'
        db.add_column(u'registration_player', 'wants_shirt',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)

        # Deleting field 'Player.want_shirt'
        db.delete_column(u'registration_player', 'want_shirt')

        # Deleting field 'Player.want_frisbee'
        db.delete_column(u'registration_player', 'want_frisbee')


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
            'want_frisbee': ('django.db.models.fields.BooleanField', [], {}),
            'want_shirt': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['registration']