# Generated by Django 3.2.4 on 2021-06-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_fullname_certificates_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='certificate',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='student.certificate_type'),
        ),
    ]