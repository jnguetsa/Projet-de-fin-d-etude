# Generated by Django 4.2.11 on 2024-05-30 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PRODUITS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registresdesentrer',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='registresdesentrer',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUITS.produit', verbose_name='Produit'),
        ),
        migrations.AddField(
            model_name='produitvente',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='produitvente',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUITS.produit', verbose_name='Produit'),
        ),
        migrations.AddField(
            model_name='produit',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
