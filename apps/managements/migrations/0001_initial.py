# Generated by Django 4.0.5 on 2022-07-07 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=1024, null=True, verbose_name='field data')),
                ('data_boolean', models.BooleanField(blank=True, help_text='Attribute that is used only when the field is checkbox type.', null=True)),
            ],
            options={
                'verbose_name': 'DataField',
                'verbose_name_plural': 'DataFields',
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('metadata', models.TextField(help_text='Data about the data originated only in telephony management.')),
                ('status', models.CharField(choices=[('in_process', 'In process'), ('finished', 'Finished')], max_length=15, verbose_name='management status')),
            ],
            options={
                'verbose_name': 'Management',
                'verbose_name_plural': 'Managements',
            },
        ),
        migrations.CreateModel(
            name='TypeManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'TypeManagement',
                'verbose_name_plural': 'TypesManagement',
            },
        ),
        migrations.CreateModel(
            name='OriginManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='managements.typemanagement')),
            ],
            options={
                'verbose_name': 'Origin',
                'verbose_name_plural': 'Origins',
            },
        ),
    ]
