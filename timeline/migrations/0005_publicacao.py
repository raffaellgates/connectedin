# Generated by Django 3.1 on 2020-11-02 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfis', '0007_delete_publicacao'),
        ('timeline', '0004_delete_publicacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postagem', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfis_pub', to='perfis.perfil')),
            ],
        ),
    ]