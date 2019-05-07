# Generated by Django 2.2.1 on 2019-05-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.TextField()),
                ('brief_content', models.TextField()),
                ('content', models.TextField()),
                ('acticle_id', models.AutoField(primary_key=True, serialize=False)),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
