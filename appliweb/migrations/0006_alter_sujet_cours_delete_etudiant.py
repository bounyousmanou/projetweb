# Generated by Django 5.0.4 on 2024-04-26 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliweb', '0005_alter_sujet_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujet',
            name='cours',
            field=models.CharField(default='Cours', max_length=100),
        ),
        migrations.DeleteModel(
            name='Etudiant',
        ),
    ]