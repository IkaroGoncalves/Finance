# Generated by Django 4.2.3 on 2023-07-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("perfil", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conta",
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
                ("apelido", models.CharField(max_length=50)),
                (
                    "banco",
                    models.CharField(
                        choices=[
                            ("NU", "NUBANK"),
                            ("CX", "CAIXA ECONOMICA"),
                            ("BD", "BRADESCO"),
                            ("IT", "ITAU"),
                            ("OT", "OUTROS"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("pf", "Pessoa fisica"), ("pj", "Pessoa juridica")],
                        max_length=2,
                    ),
                ),
                ("Valor", models.FloatField()),
                ("icone", models.ImageField(upload_to="icones")),
            ],
        ),
    ]
