# Generated by Django 4.2.7 on 2023-11-30 16:12

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=markdownx.models.MarkdownxField(),
        ),
    ]
