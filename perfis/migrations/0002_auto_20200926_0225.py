# Generated by Django 3.1 on 2020-09-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('nome_empresa', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfis',
            name='contatos',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comentarios',
        ),
        migrations.RemoveField(
            model_name='post',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='post',
            name='reaction',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='timeline',
            name='postagens',
        ),
        migrations.RemoveField(
            model_name='user',
            name='perfis',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Perfis',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Reaction',
        ),
        migrations.DeleteModel(
            name='TimeLine',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]