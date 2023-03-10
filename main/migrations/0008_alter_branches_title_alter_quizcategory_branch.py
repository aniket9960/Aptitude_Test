# Generated by Django 4.1.5 on 2023-02-04 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_quizcategory_branch_alter_branches_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quizcategory',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branches'),
        ),
    ]
