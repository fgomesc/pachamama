# Generated by Django 3.0.3 on 2020-03-06 14:19

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('estouro_orcamento', '0004_auto_20200305_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroestouroorcamento',
            name='status',
            field=django_fsm.FSMField(choices=[('Criado', 'Criado'), ('Aprovação 1', 'Aprovação 1'), ('Aprovação 2', 'Aprovação 2'), ('Aprovado', 'Aprovado')], default=('Criado', 'Criado'), max_length=50),
        ),
    ]