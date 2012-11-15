# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from labgeeks_chronos.models import Location
from labgeeks_horae.models import TimePeriod


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShiftType.location'
        db.delete_column('labgeeks_horae_shifttype', 'location_id')

        # Deleting field 'ShiftType.timeperiod'
        db.delete_column('labgeeks_horae_shifttype', 'timeperiod_id')

    def backwards(self, orm):

        # Adding field 'ShiftType.location'
        db.add_column('labgeeks_horae_shifttype', 'location', self.gf('django.db.models.fields.related.ForeignKey')(default=Location.objects.create(name='PartyPlace'), to=orm['labgeeks_chronos.Location']), keep_default=False)

        # Adding field 'ShiftType.timeperiod'
        db.add_column('labgeeks_horae_shifttype', 'timeperiod', self.gf('django.db.models.fields.related.ForeignKey')(default=TimePeriod.objects.create(name='TimeToParty', slug='timetoparty'), to=orm['labgeeks_horae.TimePeriod']), keep_default=False)

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'labgeeks_chronos.location': {
            'Meta': {'object_name': 'Location'},
            'active_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'labgeeks_horae.baseshift': {
            'Meta': {'object_name': 'BaseShift'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'shift_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.ShiftType']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'labgeeks_horae.closedhour': {
            'Meta': {'object_name': 'ClosedHour'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.TimePeriod']"})
        },
        'labgeeks_horae.defaultshift': {
            'Meta': {'object_name': 'DefaultShift'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_time': ('django.db.models.fields.TimeField', [], {}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'out_time': ('django.db.models.fields.TimeField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'timeperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_horae.TimePeriod']", 'null': 'True', 'blank': 'True'})
        },
        'labgeeks_horae.shifttype': {
            'Meta': {'object_name': 'ShiftType'},
            'allowed_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'labgeeks_horae.timeperiod': {
            'Meta': {'object_name': 'TimePeriod'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 8, 16)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2012, 8, 16)'})
        },
        'labgeeks_horae.workshift': {
            'Meta': {'object_name': 'WorkShift'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['labgeeks_chronos.Location']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'scheduled_in': ('django.db.models.fields.DateTimeField', [], {}),
            'scheduled_out': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['labgeeks_horae']
