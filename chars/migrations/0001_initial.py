# Generated by Django 3.1.7 on 2021-02-23 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supp_mains', to='skills.root')),
                ('other', models.ManyToManyField(blank=True, related_name='supp_others', to='skills.Periphery')),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supp_specials', to='skills.special')),
            ],
        ),
        migrations.CreateModel(
            name='CharMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_mains', to='skills.core')),
                ('other', models.ManyToManyField(blank=True, related_name='char_others', to='skills.Secondary')),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_specials', to='skills.special')),
            ],
        ),
    ]
