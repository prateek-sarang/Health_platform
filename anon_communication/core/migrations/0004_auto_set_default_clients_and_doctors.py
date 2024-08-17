# core/migrations/0004_auto_set_default_clients_and_doctors.py
from django.db import migrations, models

def set_default_clients_and_doctors(apps, schema_editor):
    Message = apps.get_model('core', 'Message')
    Client = apps.get_model('core', 'Client')
    Doctor = apps.get_model('core', 'Doctor')

    # Set a default client and doctor for messages that have null values
    default_client = Client.objects.first()  # or create a specific default client
    default_doctor = Doctor.objects.first()  # or create a specific default doctor

    if default_client and default_doctor:
        Message.objects.filter(client__isnull=True).update(client=default_client)
        Message.objects.filter(doctor__isnull=True).update(doctor=default_doctor)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240723_1926'),  # Last migration file
    ]

    operations = [
        migrations.RunPython(set_default_clients_and_doctors),
    ]
