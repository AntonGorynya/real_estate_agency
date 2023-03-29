from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber
from phonenumbers import is_valid_number, parse

def fill_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        print(flat)
        owner, created = Owner.objects.get_or_create(
            name=flat.owner_old,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        owner.owners_flats.add(flat)
        owner.save()

def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0006_auto_20230329_2138'),
    ]

    operations = [
        migrations.RunPython(fill_owner, move_backward)
    ]
