# Generated by Django 4.0.5 on 2022-07-01 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('document', models.CharField(blank=True, max_length=20, null=True, verbose_name='Document')),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('label', models.ManyToManyField(to='users.label')),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='DataProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=50, verbose_name='Data')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.label')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.type')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data', to='users.userprofile')),
            ],
            options={
                'verbose_name': 'DataProfile',
                'verbose_name_plural': 'DataProfiles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Ya existe un usuario con este nombre.'}, help_text='Required. 64 characters or fewer.', max_length=64, unique=True, verbose_name='nombre de usuario')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='users.userprofile')),
                ('is_staff', models.BooleanField(default=False, help_text='Indica si el usuario puede entrar en este sitio de administración.', verbose_name='es staff')),
                ('is_active', models.BooleanField(default=True, help_text='Indica si el usuario debe ser tratado como activo. Desmarque esta opción en lugar de borrar la cuenta.', verbose_name='activo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
