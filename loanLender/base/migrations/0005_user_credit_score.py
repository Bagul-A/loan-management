# Generated by Django 4.1.5 on 2023-01-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_userloan_loan_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit_score',
            field=models.IntegerField(default=0),
        ),
    ]