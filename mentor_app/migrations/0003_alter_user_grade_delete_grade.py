# Generated by Django 4.1.5 on 2023-01-27 11:58

from django.db import migrations
import django_enum.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentor_app', '0002_grade_user_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=django_enum.fields.EnumCharField(choices=[('J', 'Junior'), ('J+', 'Junior+'), ('M', 'Middle'), ('M+', 'Middle+'), ('S', 'Senior')], default=None, max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]