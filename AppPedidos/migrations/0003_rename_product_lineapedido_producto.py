# Generated by Django 4.1.5 on 2023-03-13 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPedidos', '0002_rename_pedido_id_lineapedido_pedido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='product',
            new_name='producto',
        ),
    ]