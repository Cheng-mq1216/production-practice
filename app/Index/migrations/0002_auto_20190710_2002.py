# Generated by Django 2.2.3 on 2019-07-10 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Index.Category', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Index.User', verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Index.Article', verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Index.User'),
        ),
    ]
