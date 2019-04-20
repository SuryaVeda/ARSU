# Generated by Django 2.1.7 on 2019-04-16 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='sideHeading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ebooks_pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('lectures_pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('papers_pdf', models.FileField(blank=True, null=True, upload_to='pdf/%Y/%m/$D/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('heading', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/$D/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sideheading',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.subject'),
        ),
        migrations.AddField(
            model_name='sideheading',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
