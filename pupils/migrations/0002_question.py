# Generated by Django 2.2.16 on 2022-04-26 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20220426_2024'),
        ('pupils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='Slug')),
                ('question', models.TextField(max_length=300, verbose_name='Question')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('rejected', 'rejected')], max_length=10, verbose_name='status')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pupils.Subjects')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.User')),
            ],
        ),
    ]
