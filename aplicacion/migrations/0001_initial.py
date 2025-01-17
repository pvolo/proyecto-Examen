# Generated by Django 5.0.6 on 2024-07-06 20:10

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=20)),
                ('region', models.CharField(choices=[('MAGALLANES', 'Región de Magallanes'), ('AYSEN', 'Región de Aysén'), ('MAULE', 'Región del Maule'), ('LOS_LAGOS', 'Región de Los Lagos'), ('ATACAMA', 'Región de Atacama'), ('ARAUCANIA', 'Región de La Araucanía'), ('METROPOLITANA', 'Región Metropolitana'), ('O_HIGGINS', "Región de O'Higgins"), ('ARICA_PARINACOTA', 'Región de Arica y Parinacota'), ('COQUIMBO', 'Región de Coquimbo'), ('ÑUBLE', 'Región de Ñuble'), ('BIOBIO', 'Región del Biobío'), ('ANTOFAGASTA', 'Región de Antofagasta'), ('LOS_RIOS', 'Región de Los Ríos'), ('TARAPACA', 'Región de Tarapacá'), ('VALPARAISO', 'Región de Valparaíso')], default='CONCEPCION', max_length=25)),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('boleta', models.CharField(choices=[('sin_boleta', 'Sin boleta'), ('con_boleta', 'Con boleta')], max_length=15)),
                ('estado', models.CharField(choices=[('cancelado', 'Cancelado'), ('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado')], default='en_proceso', max_length=20)),
                ('adicional', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cod_persona', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999999)])),
                ('pnombre', models.CharField(max_length=20)),
                ('snombre', models.CharField(max_length=20, null=True)),
                ('apellidop', models.CharField(max_length=20)),
                ('apellidom', models.CharField(max_length=20)),
                ('correo', models.EmailField(error_messages='El correo', max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('celular', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999)], verbose_name='Fono')),
                ('region', models.CharField(choices=[('MAGALLANES', 'Región de Magallanes'), ('AYSEN', 'Región de Aysén'), ('MAULE', 'Región del Maule'), ('LOS_LAGOS', 'Región de Los Lagos'), ('ATACAMA', 'Región de Atacama'), ('ARAUCANIA', 'Región de La Araucanía'), ('METROPOLITANA', 'Región Metropolitana'), ('O_HIGGINS', "Región de O'Higgins"), ('ARICA_PARINACOTA', 'Región de Arica y Parinacota'), ('COQUIMBO', 'Región de Coquimbo'), ('ÑUBLE', 'Región de Ñuble'), ('BIOBIO', 'Región del Biobío'), ('ANTOFAGASTA', 'Región de Antofagasta'), ('LOS_RIOS', 'Región de Los Ríos'), ('TARAPACA', 'Región de Tarapacá'), ('VALPARAISO', 'Región de Valparaíso')], default='CONCEPCION', max_length=25)),
                ('info_adicional', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='personas')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_producto', models.CharField(choices=[('ROPA', 'Ropa')], default='OTRO PRODUCTO', max_length=10)),
                ('precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(999999999)])),
                ('stock', models.IntegerField(default=0)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('usuario', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombusuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=250)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.usuario'),
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('idcompra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField(auto_now_add=True, verbose_name='Fecha de compra')),
                ('estado', models.CharField(choices=[('CANCELADO', 'Cancelado'), ('ENTREGADO', 'Entregado'), ('PENDIENTE', 'Pendiente')], default='PENDIENTE', max_length=100)),
                ('imagenenvio', models.ImageField(null=True, upload_to='imagenenvios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('envio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.envio')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to='aplicacion.usuario')),
            ],
            options={
                'verbose_name_plural': 'Carritos',
            },
        ),
    ]
