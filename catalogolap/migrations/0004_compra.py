# Generated by Django 4.2 on 2024-08-17 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogolap', '0003_categoria_alter_cliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogolap.categoria')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogolap.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogolap.producto')),
            ],
        ),
    ]
