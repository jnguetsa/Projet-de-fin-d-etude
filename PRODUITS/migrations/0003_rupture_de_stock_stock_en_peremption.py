# Generated by Django 4.2.11 on 2024-06-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUITS', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rupture_de_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rup', models.DateField(null=True)),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Code')),
                ('conditionnement', models.CharField(choices=[('Blister', 'Blister'), ('Flacon', 'Flacon'), ('Tube', 'Tube'), ('Boite', 'Boite'), ('Sachet', 'Sachet')], max_length=255, verbose_name='Conditionnement')),
                ('dosage', models.CharField(max_length=255, verbose_name='Dosage')),
                ('forme_galenique', models.CharField(choices=[('Capsules', 'Capsules'), ('Suspensions', 'Suspensions'), ('Poudres pour reconstitution', 'Poudres pour reconstitution'), ('Granulés', 'Granulés'), ('Implants', 'Implants'), ('Collyres', 'Collyres')], max_length=255, verbose_name='Forme galénique')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_en_peremption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_peremp', models.DateField(blank=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom')),
                ('conditionnement', models.CharField(blank=True, choices=[('Blister', 'Blister'), ('Flacon', 'Flacon'), ('Tube', 'Tube'), ('Boite', 'Boite'), ('Sachet', 'Sachet')], max_length=255, null=True, verbose_name='Conditionnement')),
                ('dosage', models.CharField(max_length=255, verbose_name='Dosage')),
                ('forme_galenique', models.CharField(blank=True, choices=[('Capsules', 'Capsules'), ('Suspensions', 'Suspensions'), ('Poudres pour reconstitution', 'Poudres pour reconstitution'), ('Granulés', 'Granulés'), ('Implants', 'Implants'), ('Collyres', 'Collyres')], max_length=255, null=True, verbose_name='Forme galénique')),
                ('num_lot', models.IntegerField(blank=True, null=True)),
                ('qte', models.PositiveIntegerField(null=True, verbose_name='Quantité')),
                ('prix_unitaire', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Prix unitaire')),
                ('prix_perte', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
