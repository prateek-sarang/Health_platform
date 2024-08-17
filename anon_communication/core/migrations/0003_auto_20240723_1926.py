# core/migrations/0003_auto_20240723_1926.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_message_client_alter_message_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='client',
            field=models.ForeignKey(null=False, to='core.Client', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='message',
            name='doctor',
            field=models.ForeignKey(null=False, to='core.Doctor', on_delete=models.CASCADE),
        ),
    ]
