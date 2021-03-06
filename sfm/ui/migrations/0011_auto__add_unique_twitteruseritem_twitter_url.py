# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'TwitterUserItem', fields ['twitter_url']
        db.create_unique('ui_twitteruseritem', ['twitter_url'])

    def backwards(self, orm):
        # Removing unique constraint on 'TwitterUserItem', fields ['twitter_url']
        db.delete_unique('ui_twitteruseritem', ['twitter_url'])

    models = {
        'ui.rule': {
            'Meta': {'object_name': 'Rule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'locations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'people': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'words': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'ui.status': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Status'},
            'avatar_url': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rule_match': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'rule_tag': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'status_id': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'ui.trenddaily': {
            'Meta': {'ordering': "['-date', 'name']", 'object_name': 'TrendDaily'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'events': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'promoted_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {})
        },
        'ui.trendweekly': {
            'Meta': {'ordering': "['-date', 'name']", 'object_name': 'TrendWeekly'},
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'events': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'promoted_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {})
        },
        'ui.twitteruser': {
            'Meta': {'object_name': 'TwitterUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        },
        'ui.twitteruseritem': {
            'Meta': {'object_name': 'TwitterUserItem'},
            'date_published': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_json': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'item_text': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'place': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'twitter_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ui.TwitterUser']"})
        }
    }

    complete_apps = ['ui']