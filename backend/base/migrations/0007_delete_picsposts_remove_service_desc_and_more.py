# Generated by Django 5.0.4 on 2024-04-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_rename_description_service_desc"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PicsPosts",
        ),
        migrations.RemoveField(
            model_name="service",
            name="desc",
        ),
        migrations.RemoveField(
            model_name="service",
            name="kind",
        ),
        migrations.RemoveField(
            model_name="service",
            name="price",
        ),
        migrations.AddField(
            model_name="service",
            name="cost",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="service",
            name="image",
            field=models.ImageField(
                default="default_image.jpg", upload_to="service_images/"
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
