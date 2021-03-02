# Generated by Django 3.0.4 on 2020-04-25 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0007_delete_dick'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=240)),
                ('value', models.CharField(db_index=True, max_length=240)),
            ],
        ),
        migrations.RemoveField(
            model_name='keyvaluepair',
            name='container',
        ),
        migrations.RemoveField(
            model_name='sperm',
            name='container',
        ),
        migrations.RenameModel(
            old_name='Balls',
            new_name='Dict',
        ),
        migrations.DeleteModel(
            name='Dictionary',
        ),
        migrations.DeleteModel(
            name='KeyValuePair',
        ),
        migrations.DeleteModel(
            name='Sperm',
        ),
        migrations.AddField(
            model_name='dictobj',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialists.Dict'),
        ),
    ]