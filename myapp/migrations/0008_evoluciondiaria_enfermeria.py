# Generated migration for EvolucionDiariaEnfermeria model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_crear_grupo_enfermeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvolucionDiariaEnfermeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('paso_el_dia', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], default='B', max_length=1)),
                ('alimentacion', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], default='B', max_length=1)),
                ('elimina', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], default='B', max_length=1)),
                ('exonera', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], default='B', max_length=1)),
                ('medicamentos', models.CharField(choices=[('1', 'Sí'), ('0', 'No')], default='1', max_length=1)),
                ('frecuencia_cardiaca', models.CharField(blank=True, max_length=10, null=True, verbose_name='F.C.')),
                ('presion_arterial', models.CharField(blank=True, max_length=10, null=True, verbose_name='P.A.')),
                ('temperatura', models.CharField(blank=True, max_length=10, null=True, verbose_name='T')),
                ('frecuencia_respiratoria', models.CharField(blank=True, max_length=10, null=True, verbose_name='F.R.')),
                ('novedad', models.CharField(choices=[('1', 'Sí'), ('0', 'No')], default='0', max_length=1)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('nombre_profesional', models.CharField(max_length=255, verbose_name='Nombre de quien atiende')),
                ('identificacion_profesional', models.CharField(max_length=50, verbose_name='Identificación')),
                ('firma', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evoluciones_enfermeria', to='myapp.identificacion')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='evoluciones_registradas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evolución Diaria de Enfermería',
                'verbose_name_plural': 'Evoluciones Diarias de Enfermería',
                'ordering': ['-fecha', '-fecha_registro'],
            },
        ),
    ]
