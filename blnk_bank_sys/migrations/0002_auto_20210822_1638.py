# Generated by Django 3.2.6 on 2021-08-22 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blnk_bank_sys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.user')),
                ('balance', models.IntegerField()),
                ('type', models.TextField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='amortizationtableforcustomer',
            name='interest',
            field=models.IntegerField(default='12'),
        ),
        migrations.AddField(
            model_name='amortizationtableforcustomer',
            name='principal',
            field=models.BigIntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amortizationtableforprovider',
            name='interest',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amortizationtableforprovider',
            name='principal',
            field=models.BigIntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amortizationtablesforbank',
            name='interest',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amortizationtablesforbank',
            name='principal',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanfundsstatus',
            name='available_fund_amount',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requiredloan',
            name='interest',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requiredloan',
            name='loan_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amortizationtablesforbank',
            name='payment_date',
            field=models.DateTimeField(),
        ),
    ]
