# Generated by Django 2.2.6 on 2020-08-28 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20200828_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='p_library.Publisher', verbose_name='Издатель'),
        ),
    ]
