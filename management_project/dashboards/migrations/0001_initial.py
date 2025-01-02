# Generated by Django 5.1.4 on 2025-01-02 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(limit_choices_to={'role__role_name': 'Admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='created_courses', to='authentication.user')),
                ('employees', models.ManyToManyField(blank=True, limit_choices_to={'role__role_name': 'Employee'}, related_name='enrolled_courses', to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('resource_link', models.URLField(blank=True, max_length=1024, null=True)),
                ('file_upload', models.FileField(blank=True, null=True, upload_to='module_resources/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='dashboards.course')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('recipients', models.ManyToManyField(related_name='notifications', to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('course_duration', models.PositiveIntegerField(help_text='Duration in days')),
                ('employee_count', models.PositiveIntegerField(help_text='Number of employees involved')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account_manager', models.ForeignKey(limit_choices_to={'role__role_name': 'Manager'}, on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_percentage', models.FloatField(default=0.0)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='dashboards.course')),
                ('employee', models.ForeignKey(limit_choices_to={'role__role_name': 'Employee'}, on_delete=django.db.models.deletion.CASCADE, related_name='course_progress', to='authentication.user')),
            ],
            options={
                'unique_together': {('employee', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboards.course')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('rating__gte', 1), ('rating__lte', 5)), name='rating_between_1_and_5')],
            },
        ),
        migrations.CreateModel(
            name='ModuleCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboards.module')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'unique_together': {('user', 'module')},
            },
        ),
    ]
