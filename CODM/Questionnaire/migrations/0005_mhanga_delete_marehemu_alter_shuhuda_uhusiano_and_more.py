# Generated by Django 4.1.7 on 2023-05-03 07:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Questionnaire', '0004_auto_20230503_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mhanga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jina_kwanza', models.CharField(default='default_value', max_length=255)),
                ('jina_pili', models.CharField(max_length=255)),
                ('jina_mwisho', models.CharField(max_length=255)),
                ('jinsia', models.CharField(choices=[('mume', 'mwanaume'), ('mke', 'mwanamke')], max_length=255)),
                ('ndoa', models.CharField(choices=[('ndoa', 'ndoa'), ('hajafunga ndoa', 'hajafunga ndoa'), ('mjane', 'mjane'), ('mgane', 'mgane'), ('talaka', 'talaka'), ('kutengana', 'kutengana')], max_length=255)),
                ('kuzaliwa', models.DateField(default=django.utils.timezone.now)),
                ('kufa', models.DateField(default=django.utils.timezone.now)),
                ('mahali', models.CharField(choices=[('nyumbani', 'nyumbani'), ('hospitali', 'hospitali'), ('kituo cha afya', 'kituo cha afya'), ('sijui', 'sijui')], max_length=255)),
                ('maelezo', models.TextField()),
                ('sababu1', models.CharField(max_length=255)),
                ('sababu2', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='marehemu',
        ),
        migrations.AlterField(
            model_name='shuhuda',
            name='uhusiano',
            field=models.CharField(choices=[('Baba', 'Baba'), ('Mama', 'Mama'), ('ndugu', 'ndugu'), ('Hakuna Uhusiano', 'Hakuna Uhusiano'), ('Nyingine', 'nyingine')], max_length=255),
        ),
        migrations.AddField(
            model_name='mhanga',
            name='shuhuda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questionnaire.shuhuda'),
        ),
    ]