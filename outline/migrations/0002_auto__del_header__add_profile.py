# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Header'
        db.delete_table(u'outline_header')

        # Removing M2M table for field web on 'Header'
        db.delete_table(db.shorten_name(u'outline_header_web'))

        # Adding model 'Profile'
        db.create_table(u'outline_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('home', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'outline', ['Profile'])

        # Adding M2M table for field web on 'Profile'
        m2m_table_name = db.shorten_name(u'outline_profile_web')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm[u'outline.profile'], null=False)),
            ('web', models.ForeignKey(orm[u'outline.web'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'web_id'])


    def backwards(self, orm):
        # Adding model 'Header'
        db.create_table(u'outline_header', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('home', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'outline', ['Header'])

        # Adding M2M table for field web on 'Header'
        m2m_table_name = db.shorten_name(u'outline_header_web')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('header', models.ForeignKey(orm[u'outline.header'], null=False)),
            ('web', models.ForeignKey(orm[u'outline.web'], null=False))
        ))
        db.create_unique(m2m_table_name, ['header_id', 'web_id'])

        # Deleting model 'Profile'
        db.delete_table(u'outline_profile')

        # Removing M2M table for field web on 'Profile'
        db.delete_table(db.shorten_name(u'outline_profile_web'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'outline.data': {
            'Meta': {'object_name': 'Data'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outline.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'outline.entry': {
            'Meta': {'object_name': 'Entry'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outline.Section']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'outline.profile': {
            'Meta': {'object_name': 'Profile'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'web': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outline.Web']", 'null': 'True', 'symmetrical': 'False'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'outline.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'outline.web': {
            'Meta': {'object_name': 'Web'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['outline']