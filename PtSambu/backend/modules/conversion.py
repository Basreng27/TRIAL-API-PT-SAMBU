from num2words import num2words

def number_to_text(request, number: int):
    # Konversi angka menjadi teks
    text = num2words(number, lang='id')
    result_text = f"{text.capitalize()} rupiah"
    
    # return sebagai respon
    return {
            "status": True,
            "message": "Berhasil",
            "data": {
                    "text": result_text
                }
            }