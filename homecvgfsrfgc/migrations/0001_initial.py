# Generated by Django 2.2.12 on 2020-05-07 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dgfhdf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ffghu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dgfwrs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ffghu_dgfwrs', to='dgfhdf.Ffgjy')),
            ],
        ),
    ]
