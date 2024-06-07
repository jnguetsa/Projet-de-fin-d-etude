# Generated by Django 4.2.11 on 2024-05-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_lot', models.IntegerField(verbose_name='Numéro de lot')),
                ('date_peremption', models.DateField(verbose_name='Date de péremption')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Code')),
                ('conditionnement', models.CharField(choices=[('Blister', 'Blister'), ('Flacon', 'Flacon'), ('Tube', 'Tube'), ('Boite', 'Boite'), ('Sachet', 'Sachet')], max_length=255, verbose_name='Conditionnement')),
                ('dosage', models.CharField(max_length=255, verbose_name='Dosage')),
                ('forme_galenique', models.CharField(choices=[('Capsules', 'Capsules'), ('Suspensions', 'Suspensions'), ('Poudres pour reconstitution', 'Poudres pour reconstitution'), ('Granulés', 'Granulés'), ('Implants', 'Implants'), ('Collyres', 'Collyres')], max_length=255, verbose_name='Forme galénique')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProduitVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.PositiveIntegerField(verbose_name='Quantité')),
                ('prix_unitaire', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Prix unitaire')),
                ('annulees', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegistresDesEntrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entree', models.DateField(verbose_name="Date d'entrée")),
                ('num_pvr', models.IntegerField(verbose_name='Numéro PVR')),
                ('num_bl', models.IntegerField(verbose_name='Numéro BL')),
                ('qte_recue', models.PositiveIntegerField(default=0, verbose_name='Quantité reçue')),
                ('prix_unitaire', models.PositiveBigIntegerField(verbose_name='Prix unitaire')),
            ],
        ),
    ]