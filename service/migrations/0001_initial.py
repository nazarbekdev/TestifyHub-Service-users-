# Generated by Django 4.2.1 on 2024-12-25 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_code', models.IntegerField()),
                ('answers', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('telegram_id', models.BigIntegerField()),
                ('limit', models.IntegerField(default=5)),
                ('checked_file', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckSheetResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='check_file/outputfile')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatabaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenerateTestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(max_length=50)),
                ('subject2', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('number_books', models.IntegerField()),
                ('user', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('AB', 'AB')], default='AB', max_length=2)),
                ('keys', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.IntegerField()),
                ('subject_category_id', models.IntegerField()),
                ('language_id', models.IntegerField()),
                ('database_type_id', models.IntegerField()),
                ('question', models.TextField()),
                ('answers', models.TextField()),
                ('answer', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('limit', models.IntegerField(default=50)),
                ('status', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subject')),
            ],
            options={
                'verbose_name': 'Subject Category',
                'verbose_name_plural': 'Subject Categories',
            },
        ),
        migrations.CreateModel(
            name='TitulUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('file', models.FileField(upload_to='userfile/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenerateTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_books', models.IntegerField()),
                ('database_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.databasetype')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='service.language')),
                ('subject1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_1', to='service.subject')),
                ('subject2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_2', to='service.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tests', to='service.serviceuser')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='document/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('database_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.databasetype')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.language')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subject')),
                ('subject_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subjectcategory')),
            ],
        ),
        migrations.CreateModel(
            name='CheckSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(blank=True, max_length=20, null=True)),
                ('file', models.FileField(upload_to='check_file/inputfile')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.serviceuser')),
            ],
        ),
        migrations.CreateModel(
            name='TestControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_limit', models.IntegerField(default=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subjectcategory')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subject')),
            ],
            options={
                'verbose_name': 'Test Control',
                'verbose_name_plural': 'Test Controls',
                'unique_together': {('subject', 'category')},
            },
        ),
    ]
