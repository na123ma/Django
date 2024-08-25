# Generated by Django 5.0.6 on 2024-07-05 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchNo', models.CharField(max_length=8)),
                ('batchId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=4)),
                ('courseId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examId', models.IntegerField()),
                ('examType', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PaperMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperCode', models.CharField(max_length=20)),
                ('papertype', models.CharField(max_length=15)),
                ('paperShtName', models.CharField(max_length=10)),
                ('paperName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SemMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=3)),
                ('semId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studRegNo', models.IntegerField()),
                ('studName', models.CharField(max_length=20)),
                ('batchNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.batchmaster')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.coursemaster')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.semmaster')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInternalTransMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfTheStudent', models.CharField(max_length=25)),
                ('marks', models.IntegerField()),
                ('batchNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.batchmaster')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.coursemaster')),
                ('examType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.exammaster')),
                ('paperCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.papermaster')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.semmaster')),
                ('studRegNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.studentmaster')),
            ],
        ),
    ]
