# Generated by Django 4.1.5 on 2023-02-04 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_branches_delete_usercategoryattempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizcategory',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.branches'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='title',
            field=models.CharField(default='?', max_length=100),
        ),
    ]