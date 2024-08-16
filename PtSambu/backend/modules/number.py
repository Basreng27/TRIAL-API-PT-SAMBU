import random
from ..models import Number
from django.db import IntegrityError

def number(request, payload):
    num1 = payload.num1
    num2 = payload.num2
    
    # Validasi nilai input
    if (num1 < 1000000) or (num1 > 100000000) or (num2 < 1000000) or (num2 > 100000000):
        return {"error": "Number Harus Diantara 1,000,000 dan 100,000,000"}

    # Tukar nilai
    if num1 > num2:
        num2, num1 = num1, num2

    # Generate random number di antara kedua nilai
    random_number = random.randint(num1, num2)
    
    try:
        # Simpan nilai ke dalam database
        Number.objects.create(
                num1=num1,
                num2=num2,
                random_number=random_number,
            )
        
        # Kembalikan random number sebagai respon
        return {
            "status": True,
            "message": "Berhasil Simpan Data",
            "data": {
                    "random_number": random_number
                }
            }
    except IntegrityError as e:
        return {
            "status": False,
            "message": "Gagal Simpan Data - Internal Server Error",
            "error": str(e)
        }
    except Exception as e:
        return {
            "status": False,
            "message": "Gagal Simpan Data",
            "error": str(e)
        }