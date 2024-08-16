# Untuk menghitung gaji bruto, tunjangan, tunjangan pajak, dan gaji bruto akhir
def calculate(request, basic_salary: int):
    # Persentase tunjangan pajak
    allowance_percentage = 0.20
    # Persentase pajak
    tax_percentage = 0.05

    # Hitung tunjangan (20% dari gaji pokok)
    allowance = basic_salary * allowance_percentage

    # Estimasi awal gaji bruto tanpa pajak
    estimated_gross_salary = basic_salary + allowance

    # Hitung tunjangan pajak
    tax_allowance = (estimated_gross_salary * tax_percentage) / (1 - tax_percentage)

    # Hitung gaji bruto sebenarnya dengan tunjangan pajak
    gross_salary = basic_salary + allowance + tax_allowance

    # Return hasil perhitungan
    return {
        "basic_salary": f"Rp.{round(basic_salary, 2)}",
        "allowance": f"Rp.{round(allowance, 2)}",
        "tax_allowance": f"Rp.{round(tax_allowance, 2)}",
        "gross_salary": f"Rp.{round(gross_salary, 2)}"
    }