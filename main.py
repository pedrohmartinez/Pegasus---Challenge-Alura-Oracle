from src.ingestion.loader import (
    get_pdf_files,
    load_pdf,
    load_all_pdfs
)


def main():
    
    try:
        
        pdf_files = get_pdf_files("data/pdfs")
        
        first_pdf = pdf_files[0]
        
        documents = load_pdf(first_pdf)
        
        all_documents = load_all_pdfs("data/pdfs")
        
        # print(f"total de PDFs encontrados: {all_documents}")
        print(f"PDFs encontrados: {len(pdf_files)}")
        print(f"total de Document carregados: {len(all_documents)}")
                            
        print("\nLista de documents\n")

        print(f"PDF: {first_pdf.name}")
        print(f"Páginas carregadas: {len(documents)}")
        
        print("\nMETADATA\n")
        print(documents[0].metadata)
        
        print("\nCONTEÚDO\n")
        print(documents[0].page_content[:1000])
        
        print(type(documents))
        print(type(documents[0])) 
        
        print(documents[0].metadata["page"])
        print(documents[1].metadata["page"])
        print(documents[2].metadata["page"])
        
        print(all_documents[0].metadata["source"])
        print(all_documents[-1].metadata["source"])
        
    except Exception as e:
        print(f"Erro:{e}")

if __name__ == "__main__":
    main()