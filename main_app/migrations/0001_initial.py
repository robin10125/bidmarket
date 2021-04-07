# Generated by Django 3.1.7 on 2021-04-07 14:35

import datetime
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
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(choices=[('Home', 'Home'), ('Fashion', 'Fashion'), ('Tech', 'Tech'), ('Sporting', 'Sporting'), ('Books', 'Books')], max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('min_bid_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('buy_now_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('current_highest_bid', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.listing')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
                ('datetime', models.DateTimeField()),
                ('parent_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.thread')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.listing')),
            ],
        ),
    ]
