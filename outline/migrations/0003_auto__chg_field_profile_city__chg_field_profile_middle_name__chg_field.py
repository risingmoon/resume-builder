# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Profile.city'
        db.alter_column(u'outline_profile', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.middle_name'
        db.alter_column(u'outline_profile', 'middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.address1'
        db.alter_column(u'outline_profile', 'address1', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.address2'
        db.alter_column(u'outline_profile', 'address2', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.fax'
        db.alter_column(u'outline_profile', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'Profile.zipcode'
        db.alter_column(u'outline_profile', 'zipcode', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.cell'
        db.alter_column(u'outline_profile', 'cell', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'Profile.state'
        db.alter_column(u'outline_profile', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.home'
        db.alter_column(u'outline_profile', 'home', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'Profile.region'
        db.alter_column(u'outline_profile', 'region', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Profile.email'
        db.alter_column(u'outline_profile', 'email', self.gf('django.db.models.fields.CharField')(default='', max_length=50))
        # Adding field 'Entry.present'
        db.add_column(u'outline_entry', 'present',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.display'
        db.add_column(u'outline_entry', 'display',
                      self.gf('django.db.models.fields.CharField')(default='L', max_length=1),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Profile.city'
        db.alter_column(u'outline_profile', 'city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.middle_name'
        db.alter_column(u'outline_profile', 'middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.address1'
        db.alter_column(u'outline_profile', 'address1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.address2'
        db.alter_column(u'outline_profile', 'address2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.fax'
        db.alter_column(u'outline_profile', 'fax', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Profile.zipcode'
        db.alter_column(u'outline_profile', 'zipcode', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.cell'
        db.alter_column(u'outline_profile', 'cell', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Profile.state'
        db.alter_column(u'outline_profile', 'state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.home'
        db.alter_column(u'outline_profile', 'home', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Profile.region'
        db.alter_column(u'outline_profile', 'region', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Profile.email'
        db.alter_column(u'outline_profile', 'email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
        # Deleting field 'Entry.present'
        db.delete_column(u'outline_entry', 'present')

        # Deleting field 'Entry.display'
        db.delete_column(u'outline_entry', 'display')


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
            'display': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'present': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outline.Section']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'outline.profile': {
            'Meta': {'object_name': 'Profile'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'web': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outline.Web']", 'symmetrical': 'False', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
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