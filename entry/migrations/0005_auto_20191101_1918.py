# Generated by Django 2.2.5 on 2019-11-02 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entry', '0004_auto_20191026_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee_str',
            name='Total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stud_pd',
            name='added_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Apti_1_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Book_3_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Conf_10_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Date_Paid',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='IndP_4_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='IndV_5_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Inte_6_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Libr_7_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Semi_8_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Soft_9_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Spor_12_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Subj_11_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Tech_2_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Tran_13_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Tuti_14_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stud_fees',
            name='Volu_15_Paid',
            field=models.IntegerField(default=0),
        ),
    ]
