############################################################################
## Django ORM Standalone Python Template
############################################################################

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import your models for use in your script
from db.models import User


# # # Lambda Handler 
def lambda_handler(event, context):
    
    users = [
        {
            "id": elem.get_id(),
            "email": elem.email,
        } 
        for elem in User.objects.all()[:10]
    ]
    print(users)

    return {
        "statusCode": 200,
        "users": users
    }
