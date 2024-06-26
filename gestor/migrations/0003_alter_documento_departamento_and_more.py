# Generated by Django 5.0.2 on 2024-04-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_remove_departamento_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='departamento',
            field=models.CharField(choices=[('Contabilidad', 'Contabilidad'), ('Administracion', 'Administracion'), ('Secreataria', 'Secretaria'), ('RRHH', 'RRHH'), ('Informatica', 'Informatica'), ('Finanzas', 'Finanzas'), ('Sistemas', 'Sistemas'), ('Educacion', 'Educacion')], default='Informatica', max_length=20),
        ),
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.CharField(choices=[('General', 'General'), ('Resolucion', 'Resolucion'), ('Circular', 'Circular'), ('Minuta', 'Minuta'), ('Nota', 'Nota'), ('Oficio', 'Oficio')], default='General', max_length=20),
        ),
    ]
