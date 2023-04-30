from django.db import migrations


def add_initial_data(apps, schema_editor):
    Profile = apps.get_model('books', 'Profile')
    profile_entries = [
        Profile(
            column_name=column_name,
            is_visible=True
        )
        for column_name in ['name', 'title', 'author', 'description', 'price']
    ]
    Profile.objects.bulk_create(profile_entries)


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),

    ]
