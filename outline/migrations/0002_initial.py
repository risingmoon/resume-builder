# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Web'
        db.create_table(u'outline_web', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'outline', ['Web'])

        # Adding model 'Header'
        db.create_table(u'outline_header', (
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
        db.send_create_signal(u'outline', ['Header'])

        # Adding M2M table for field webs on 'Header'
        m2m_table_name = db.shorten_name(u'outline_header_webs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('header', models.ForeignKey(orm[u'outline.header'], null=False)),
            ('web', models.ForeignKey(orm[u'outline.web'], null=False))
        ))
        db.create_unique(m2m_table_name, ['header_id', 'web_id'])

        # Adding model 'Section'
        db.create_table(u'outline_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'outline', ['Section'])

        # Adding model 'Entry'
        db.create_table(u'outline_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['outline.Section'])),
        ))
        db.send_create_signal(u'outline', ['Entry'])

        # Adding model 'Data'
        db.create_table(u'outline_data', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['outline.Entry'])),
        ))
        db.send_create_signal(u'outline', ['Data'])


    def backwards(self, orm):
        # Deleting model 'Web'
        db.delete_table(u'outline_web')

        # Deleting model 'Header'
        db.delete_table(u'outline_header')

        # Removing M2M table for field webs on 'Header'
        db.delete_table(db.shorten_name(u'outline_header_webs'))

        # Deleting model 'Section'
        db.delete_table(u'outline_section')

        # Deleting model 'Entry'
        db.delete_table(u'outline_entry')

        # Deleting model 'Data'
        db.delete_table(u'outline_data')


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
        u'outline.header': {
            'Meta': {'object_name': 'Header'},
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
            'webs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outline.Web']", 'symmetrical': 'False'}),
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