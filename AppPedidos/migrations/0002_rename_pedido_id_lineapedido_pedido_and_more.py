# Generated by Django 4.1.5 on 2023-03-13 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='producto_id',
            new_name='product',
        ),
    ]
