from datetime import datetime

def generate_nim(prodi: str) -> str:
    year = datetime.now().year
    code = prodi[:2].upper()
    time = datetime.now().strftime("%H%M%S")
    return f"{year}{code}{time}"
