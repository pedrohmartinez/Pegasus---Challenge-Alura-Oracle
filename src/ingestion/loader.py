from pathlib import Path

def get_pdf_files(pdf_directory: str) -> list[Path]:
    
    directory = Path(pdf_directory)
    
    if not directory.exists():
        raise FileNotFoundError(
            f"Diretório não encontrado: {pdf_directory}"
        )
    if not directory.is_dir():
        raise FileNotFoundError(
            f"O caminho não é um diretório: {pdf_directory}"
        )
    
    pdf_files = list(directory.glob("*.pdf"))
    
    return pdf_files