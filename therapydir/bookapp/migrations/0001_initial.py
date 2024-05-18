# Generated by Django 3.2.12 on 2024-05-16 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.IntegerField()),
                ('specialization', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('licenseNum', models.CharField(max_length=50)),
                ('tradition', models.CharField(max_length=100)),
                ('priceForSession', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book_A_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateForSession', models.DateTimeField()),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('patient_name', models.CharField(max_length=150)),
                ('therapist_name', models.CharField(max_length=150)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_session', to='bookapp.patient')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist', to='bookapp.therapist')),
            ],
        ),
    ]