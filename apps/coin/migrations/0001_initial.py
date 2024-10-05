# Generated by Django 3.2.25 on 2024-10-05 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(help_text='Código de la moneda, por ejemplo, USD, EUR', max_length=3, unique=True)),
                ('name', models.CharField(help_text='Nombre completo de la moneda, por ejemplo, Dólar Estadounidense', max_length=100)),
                ('symbol', models.CharField(blank=True, help_text='Símbolo de la moneda, por ejemplo, $ o €', max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Indica si la moneda está activa o no')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default='', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rate', models.FloatField(default=1, help_text='Tasa de cambio entre la moneda base y la moneda objetivo', null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default='', max_length=250, null=True)),
                ('base_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_currency', to='coin.currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_currency', to='coin.currency')),
            ],
            options={
                'unique_together': {('base_currency', 'target_currency')},
            },
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('commission_percentage', models.FloatField(help_text='Porcentaje de comisión aplicado al intercambio de moneda')),
                ('reverse_commission', models.FloatField(help_text='Comisión inversa para el intercambio de moneda en dirección opuesta')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default='', max_length=250, null=True)),
                ('base_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission_base_currency', to='coin.currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission_target_currency', to='coin.currency')),
            ],
            options={
                'unique_together': {('base_currency', 'target_currency')},
            },
        ),
    ]