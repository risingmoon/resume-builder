# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resume_Web'
        db.create_table(u'resume_storage_resume_web', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resume_storage.Resume'])),
        ))
        db.send_create_signal(u'resume_storage', ['Resume_Web'])

        # Deleting field 'Resume.header'
        db.delete_column(u'resume_storage_resume', 'header_id')

        # Adding field 'Resume.first_name'
        db.add_column(u'resume_storage_resume', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='legacy', max_length=50),
                      keep_default=False)

        # Adding field 'Resume.middle_name'
        db.add_column(u'resume_storage_resume', 'middle_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.last_name'
        db.add_column(u'resume_storage_resume', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='legacylast', max_length=50),
                      keep_default=False)

        # Adding field 'Resume.cell'
        db.add_column(u'resume_storage_resume', 'cell',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True),
                      keep_default=False)

        # Adding field 'Resume.home'
        db.add_column(u'resume_storage_resume', 'home',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True),
                      keep_default=False)

        # Adding field 'Resume.fax'
        db.add_column(u'resume_storage_resume', 'fax',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True),
                      keep_default=False)

        # Adding field 'Resume.address1'
        db.add_column(u'resume_storage_resume', 'address1',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.address2'
        db.add_column(u'resume_storage_resume', 'address2',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.city'
        db.add_column(u'resume_storage_resume', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.state'
        db.add_column(u'resume_storage_resume', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.zipcode'
        db.add_column(u'resume_storage_resume', 'zipcode',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.email'
        db.add_column(u'resume_storage_resume', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Resume.region'
        db.add_column(u'resume_storage_resume', 'region',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Resume_Web'
        db.delete_table(u'resume_storage_resume_web')

        # Adding field 'Resume.header'
        db.add_column(u'resume_storage_resume', 'header',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2014, 4, 1, 0, 0), to=orm['outline.Header'], unique=True),
                      keep_default=False)

        # Deleting field 'Resume.first_name'
        db.delete_column(u'resume_storage_resume', 'first_name')

        # Deleting field 'Resume.middle_name'
        db.delete_column(u'resume_storage_resume', 'middle_name')

        # Deleting field 'Resume.last_name'
        db.delete_column(u'resume_storage_resume', 'last_name')

        # Deleting field 'Resume.cell'
        db.delete_column(u'resume_storage_resume', 'cell')

        # Deleting field 'Resume.home'
        db.delete_column(u'resume_storage_resume', 'home')

        # Deleting field 'Resume.fax'
        db.delete_column(u'resume_storage_resume', 'fax')

        # Deleting field 'Resume.address1'
        db.delete_column(u'resume_storage_resume', 'address1')

        # Deleting field 'Resume.address2'
        db.delete_column(u'resume_storage_resume', 'address2')

        # Deleting field 'Resume.city'
        db.delete_column(u'resume_storage_resume', 'city')

        # Deleting field 'Resume.state'
        db.delete_column(u'resume_storage_resume', 'state')

        # Deleting field 'Resume.zipcode'
        db.delete_column(u'resume_storage_resume', 'zipcode')

        # Deleting field 'Resume.email'
        db.delete_column(u'resume_storage_resume', 'email')

        # Deleting field 'Resume.region'
        db.delete_column(u'resume_storage_resume', 'region')


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
        u'outline.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'resume_storage.resume': {
            'Meta': {'object_name': 'Resume'},
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'resume_storage.resume_web': {
            'Meta': {'object_name': 'Resume_Web'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_storage.Resume']"})
        },
        u'resume_storage.saved_entry': {
            'Meta': {'object_name': 'Saved_Entry'},
            'dataset': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outline.Data']", 'symmetrical': 'False'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outline.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_storage.Saved_Section']"})
        },
        u'resume_storage.saved_section': {
            'Meta': {'object_name': 'Saved_Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resume_storage.Resume']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outline.Section']"})
        }
    }

    complete_apps = ['resume_storage']