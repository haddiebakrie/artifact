# Generated by Django 5.1.2 on 2025-01-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objektgattung', models.CharField(max_length=100)),
                ('sphaere', models.CharField(max_length=50)),
                ('datierung', models.CharField(max_length=100)),
                ('anbringungsort', models.CharField(max_length=200)),
                ('aufbewahrungsort', models.CharField(max_length=200)),
                ('kultempfaenger', models.CharField(max_length=100)),
                ('amunsikonographie', models.TextField()),
                ('namen_und_beiwoerter', models.TextField()),
                ('uebersetzung', models.TextField()),
                ('kommentar', models.TextField()),
                ('literatur', models.TextField()),
                ('bild_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
