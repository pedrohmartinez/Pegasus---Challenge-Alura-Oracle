from src.ingestion.loader import get_pdf_files


def main():
    
    try:
        
        pdf_files = get_pdf_files("data/pdfs")
        
        if not pdf_files:
            print("Nenhum PDF encontrado")
            return

        print(f"PDFs encontrados: {len(pdf_files)}")

        for pdf in pdf_files:
            print(pdf)

    except Exception as e:
        print(f"Erro:{e}")

if __name__ == "__main__":
    main()