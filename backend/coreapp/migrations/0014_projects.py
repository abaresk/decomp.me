# Generated by Django 3.2.6 on 2022-01-05 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0013_scratch_name_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('repo', models.CharField(max_length=100)),
                ('branch', models.CharField(default='master', max_length=100)),
                ('is_pulling', models.BooleanField(default=False)),
                ('last_pulled', models.DateTimeField(blank=True, null=True)),
                ('gh_user', models.ForeignKey(help_text='Must have admin permission on the repo', on_delete=django.db.models.deletion.PROTECT, to='coreapp.githubuser')),
            ],
            options={
                'verbose_name': 'GitHub repo',
                'verbose_name_plural': 'GitHub repos',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('icon_url', models.URLField()),
                ('repo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='coreapp.githubrepo')),
            ],
        ),
        migrations.AlterModelOptions(
            name='scratch',
            options={'ordering': ['-creation_time'], 'verbose_name_plural': 'Scratches'},
        ),
        migrations.CreateModel(
            name='ProjectFunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.project')),
                ('scratch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='coreapp.scratch')),
            ],
        ),
        migrations.AddConstraint(
            model_name='projectfunction',
            constraint=models.UniqueConstraint(fields=('slug', 'project'), name='unique_project_function'),
        ),
    ]
