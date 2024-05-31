# Generated by Django 5.0.6 on 2024-05-25 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_projet_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='type_projet',
            field=models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='ProjetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projets/images/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dashboard.projet')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageProjet',
        ),
    ]
