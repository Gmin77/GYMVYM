# Generated by Django 5.0.6 on 2024-07-17 06:46

import account.models
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "user",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "nfc_uid",
                    models.CharField(
                        blank=True, editable=False, null=True, unique=True
                    ),
                ),
                ("username", models.CharField(max_length=100, unique=True)),
                ("phone_number", models.CharField(max_length=15, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("detail_address", models.CharField(max_length=255)),
                ("nickname", models.CharField(default="", max_length=100, unique=True)),
                (
                    "user_image",
                    models.ImageField(
                        default="default.png", null=True, upload_to="user_image"
                    ),
                ),
                ("birth", models.DateField()),
                (
                    "usertype",
                    models.IntegerField(
                        choices=[(0, "Owner"), (1, "Trainer"), (2, "Member")], default=2
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("0", "Man"), ("1", "Woman")], max_length=1
                    ),
                ),
                ("is_staff", models.BooleanField(blank=True, null=True)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", account.models.CustomUserManager()),
            ],
        ),
    ]
