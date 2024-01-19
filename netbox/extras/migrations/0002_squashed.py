from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_squashed'),
        ('extras', '0001_initial'),
        ('virtualization', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dcim', '0003_squashed'),
        ('tenancy', '0001_initial'),
    ]

    replaces = [
        ('extras', '0002_custom_fields'),
        ('extras', '0003_exporttemplate_add_description'),
        ('extras', '0004_topologymap_change_comma_to_semicolon'),
        ('extras', '0005_useraction_add_bulk_create'),
        ('extras', '0006_add_imageattachments'),
        ('extras', '0007_unicode_literals'),
        ('extras', '0008_reports'),
        ('extras', '0009_topologymap_type'),
        ('extras', '0010_customfield_filter_logic'),
        ('extras', '0011_django2'),
        ('extras', '0012_webhooks'),
        ('extras', '0013_objectchange'),
        ('extras', '0014_configcontexts'),
        ('extras', '0015_remove_useraction'),
        ('extras', '0016_exporttemplate_add_cable'),
        ('extras', '0017_exporttemplate_mime_type_length'),
        ('extras', '0018_exporttemplate_add_jinja2'),
        ('extras', '0019_tag_taggeditem'),
        ('extras', '0020_tag_data'),
        ('extras', '0021_add_color_comments_changelog_to_tag'),
        ('extras', '0022_custom_links'),
        ('extras', '0023_fix_tag_sequences'),
        ('extras', '0024_scripts'),
        ('extras', '0025_objectchange_time_index'),
        ('extras', '0026_webhook_ca_file_path'),
        ('extras', '0027_webhook_additional_headers'),
        ('extras', '0028_remove_topology_maps'),
        ('extras', '0029_3569_customfield_fields'),
        ('extras', '0030_3569_objectchange_fields'),
        ('extras', '0031_3569_exporttemplate_fields'),
        ('extras', '0032_3569_webhook_fields'),
        ('extras', '0033_graph_type_template_language'),
        ('extras', '0034_configcontext_tags'),
        ('extras', '0035_deterministic_ordering'),
        ('extras', '0036_contenttype_filters_to_q_objects'),
        ('extras', '0037_configcontexts_clusters'),
        ('extras', '0038_webhook_template_support'),
        ('extras', '0039_update_features_content_types'),
        ('extras', '0040_standardize_description'),
        ('extras', '0041_tag_description'),
        ('extras', '0042_customfield_manager'),
        ('extras', '0043_report'),
        ('extras', '0044_jobresult'),
        ('extras', '0045_configcontext_changelog'),
        ('extras', '0046_update_jsonfield'),
        ('extras', '0047_tag_ordering'),
        ('extras', '0048_exporttemplate_remove_template_language'),
        ('extras', '0049_remove_graph'),
        ('extras', '0050_customfield_changes'),
        ('extras', '0051_migrate_customfields'),
        ('extras', '0052_customfield_cleanup'),
        ('extras', '0053_rename_webhook_obj_type'),
        ('extras', '0054_standardize_models'),
        ('extras', '0055_objectchange_data'),
        ('extras', '0056_extend_configcontext'),
        ('extras', '0057_customlink_rename_fields'),
        ('extras', '0058_journalentry'),
        ('extras', '0059_exporttemplate_as_attachment'),
        ('extras', '0060_customlink_button_class'),
        ('extras', '0061_extras_change_logging'),
        ('extras', '0062_clear_secrets_changelog'),
        ('extras', '0063_webhook_conditions'),
        ('extras', '0064_configrevision'),
        ('extras', '0065_imageattachment_change_logging'),
        ('extras', '0066_customfield_name_validation'),
        ('extras', '0067_customfield_min_max_values'),
        ('extras', '0068_configcontext_cluster_types'),
        ('extras', '0069_custom_object_field'),
        ('extras', '0070_customlink_enabled'),
        ('extras', '0071_standardize_id_fields'),
        ('extras', '0072_created_datetimefield'),
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('extras', '0074_customfield_extensions'),
        ('extras', '0075_configcontext_locations'),
        ('extras', '0076_tag_slug_unicode'),
        ('extras', '0077_customlink_extend_text_and_url'),
        ('extras', '0078_unique_constraints'),
        ('extras', '0079_scheduled_jobs'),
        ('extras', '0080_customlink_content_types'),
        ('extras', '0081_exporttemplate_content_types'),
        ('extras', '0082_savedfilter'),
        ('extras', '0083_search'),
        ('extras', '0084_staging'),
        ('extras', '0085_synced_data'),
        ('extras', '0086_configtemplate'),
        ('extras', '0087_dashboard'),
        ('extras', '0088_jobresult_webhooks'),
        ('extras', '0089_customfield_is_cloneable'),
        ('extras', '0090_objectchange_index_request_id'),
        ('extras', '0091_create_managedfiles'),
        ('extras', '0092_delete_jobresult'),
        ('extras', '0093_configrevision_ordering'),
        ('extras', '0094_tag_object_types'),
        ('extras', '0095_bookmarks'),
        ('extras', '0096_customfieldchoiceset'),
        ('extras', '0097_customfield_remove_choices'),
        ('extras', '0098_webhook_custom_field_data_webhook_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='configcontext',
            name='cluster_groups',
            field=models.ManyToManyField(blank=True, related_name='+', to='virtualization.clustergroup'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='cluster_types',
            field=models.ManyToManyField(blank=True, related_name='+', to='virtualization.clustertype'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='clusters',
            field=models.ManyToManyField(blank=True, related_name='+', to='virtualization.cluster'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='data_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.datafile'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.datasource'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='device_types',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.devicetype'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='locations',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.location'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='platforms',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.platform'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='regions',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.region'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.devicerole'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='site_groups',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.sitegroup'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='sites',
            field=models.ManyToManyField(blank=True, related_name='+', to='dcim.site'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='+', to='extras.tag'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='tenant_groups',
            field=models.ManyToManyField(blank=True, related_name='+', to='tenancy.tenantgroup'),
        ),
        migrations.AddField(
            model_name='configcontext',
            name='tenants',
            field=models.ManyToManyField(blank=True, related_name='+', to='tenancy.tenant'),
        ),
        migrations.AddField(
            model_name='cachedvalue',
            name='object_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='branch',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='object_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='webhook',
            constraint=models.UniqueConstraint(fields=('payload_url', 'type_create', 'type_update', 'type_delete'), name='extras_webhook_unique_payload_url_types'),
        ),
        migrations.AddIndex(
            model_name='taggeditem',
            index=models.Index(fields=['content_type', 'object_id'], name='extras_tagg_content_717743_idx'),
        ),
        migrations.AddConstraint(
            model_name='bookmark',
            constraint=models.UniqueConstraint(fields=('object_type', 'object_id', 'user'), name='extras_bookmark_unique_per_object_and_user'),
        ),
    ]
