# Generated by Django 4.2.2 on 2023-07-15 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('birth', models.DateField(null=True)),
                ('comment', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('contents_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=200)),
                ('posting_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MumChaApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('follow_id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='do_follow_user', to='MumChaApp.user')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accept_follow_user', to='MumChaApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('fav_id', models.IntegerField(primary_key=True, serialize=False)),
                ('contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MumChaApp.posting')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MumChaApp.user')),
            ],
        ),
    ]
