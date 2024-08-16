from ninja import Schema
from typing import Optional
from ninja import NinjaAPI
from .modules.number import number
from .modules.conversion import number_to_text
from .modules.gross_up import calculate

api = NinjaAPI()

# Schema
class NumberSchema(Schema):
    num1: int
    num2: int
    random_number: Optional[float] = None

# Random Angka
@api.post("/generate-number")
def create(request, payload: NumberSchema):
    return number(request, payload)

# Konversi Dari Angka Ke Text
@api.get("/conversion/{number}")
def get(request, number:int):
    return number_to_text(request, number)

# Kalkulasi Gross UP
@api.get("/gross-up/{basic_salary}")
def get(request, basic_salary:int):
    return calculate(request, basic_salary)