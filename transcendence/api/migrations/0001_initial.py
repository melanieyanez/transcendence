# Generated by Django 5.1.4 on 2025-01-22 10:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tournament_name", models.CharField(max_length=100)),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pseudo", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PongMatch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sets_to_win", models.IntegerField(default=1)),
                ("points_per_set", models.IntegerField(default=3)),
                ("player1_sets_won", models.IntegerField(default=0)),
                ("player2_sets_won", models.IntegerField(default=0)),
                ("winner", models.CharField(blank=True, max_length=100)),
                ("date_played", models.DateTimeField(auto_now_add=True)),
                ("is_tournament_match", models.BooleanField(default=False)),
                (
                    "player1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches_as_player1",
                        to="api.player",
                    ),
                ),
                (
                    "player2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches_as_player2",
                        to="api.player",
                    ),
                ),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="initiated_matches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="opponent_matches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches",
                        to="api.tournament",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PongSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("set_number", models.IntegerField()),
                ("player1_score", models.IntegerField(default=0)),
                ("player2_score", models.IntegerField(default=0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sets",
                        to="api.pongmatch",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TournamentPlayer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.player"
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.tournament"
                    ),
                ),
            ],
        ),
    ]
