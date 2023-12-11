# Generated by Django 4.2.7 on 2023-12-11 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('authr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
                ('category', models.ManyToManyField(to='categories.category')),
            ],
        ),
    ]
