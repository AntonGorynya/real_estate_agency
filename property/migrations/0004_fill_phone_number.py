from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber
from phonenumbers import is_valid_number, parse

def fill_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = flat.owners_phonenumber
        if is_valid_number(parse(phonenumber, 'RU')):
            flat.owner_pure_phone = PhoneNumber.from_string(phonenumber, region='RU')
            flat.save()

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone=0)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_fill_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_phone_number, move_backward)
    ]
