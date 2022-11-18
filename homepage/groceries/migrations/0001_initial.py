# Generated by Django 4.1.1 on 2022-09-10 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_name', models.CharField(max_length=200)),
                ('when_needed', models.DateField(verbose_name='date needed')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('when_cooking', models.DateField(verbose_name='date of the meal')),
                ('whos_cooking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.chef')),
            ],
        ),
        migrations.CreateModel(
            name='WhenNeeded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_needed_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('grocery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.grocery')),
                ('what_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.meal')),
            ],
        ),
    ]
