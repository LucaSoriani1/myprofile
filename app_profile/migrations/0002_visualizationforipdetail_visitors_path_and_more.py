# Generated by Django 4.2 on 2023-05-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualizationForIpDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('path', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Visualization for IP',
                'verbose_name_plural': 'Visualizations for IP',
            },
        ),
        migrations.AddField(
            model_name='visitors',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='VisualizationForIp',
        ),
    ]