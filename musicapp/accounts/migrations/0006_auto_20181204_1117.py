# Generated by Django 2.1.1 on 2018-12-04 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('commentUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='album',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='artist',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='song',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
