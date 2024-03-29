# Generated by Django 4.2.9 on 2024-03-08 08:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('flake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retweets', related_query_name='retweet', to='dao.flake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dao.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='retweet',
            constraint=models.UniqueConstraint(models.F('user'), models.F('flake'), name='unique_retweet'),
        ),
    ]
