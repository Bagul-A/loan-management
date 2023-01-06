# Generated by Django 4.1.5 on 2023-01-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('loan_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='repayment_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='aadhar_id',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
