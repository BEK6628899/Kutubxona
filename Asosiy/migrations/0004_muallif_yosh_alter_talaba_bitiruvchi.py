# Generated by Django 4.1.5 on 2023-01-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0003_alter_admin_ish_vaqti_alter_record_olingan_sana_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='muallif',
            name='yosh',
            field=models.SmallIntegerField(default=70),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='bitiruvchi',
            field=models.CharField(choices=[('ha', 'ha'), ('yo`q', 'yo`q')], max_length=10),
        ),
    ]