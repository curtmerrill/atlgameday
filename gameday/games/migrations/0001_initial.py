# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'games_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal(u'games', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'games_game')


    models = {
        u'games.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['games']