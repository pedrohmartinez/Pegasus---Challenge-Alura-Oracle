from src.ingestion.loader import (
    get_pdf_files,
    load_pdf,
    load_all_pdfs
)

from src.chunking.splitter import (
    split_documents
)


def main():
    
    try:
        
        pdf_files = get_pdf_files("data/pdfs")
        
        first_pdf = pdf_files[0]
        
        documents = load_pdf(first_pdf)
        
        all_documents = load_all_pdfs("data/pdfs")
        
        chunks = split_documents(all_documents)
        
        print(f"PDFs encontrados: {len(pdf_files)}")
        print(f"total de Document carregados: {len(all_documents)}")
                            
        print("\nLista de documents\n")

        print(f"PDF: {first_pdf.name}")
        print(f"Páginas carregadas: {len(documents)}")
        
        print("\nMETADATA\n")
        print(documents[0].metadata)
        
        print("\nCONTEÚDO\n")
        print(documents[0].page_content[:1000])
        
        print("\n")
        
        print(f"Variável tipo: {type(documents)}")
        print(f"Possui objetos: {type(documents[0])}") 
        
        print("\nSEPARAÇÕES\n")
        
        print(f"Página: {documents[0].metadata["page"]} do Document")
        print(f"Página: {documents[1].metadata["page"]} do Document")
        print(f"Página: {documents[2].metadata["page"]} do Document")
        
        print("\n")
        
        print(f"Primeiro PDF de all_documents: \n{all_documents[0].metadata["source"]}")
        print(f"Último PDF de all_documents: \n{all_documents[-1].metadata["source"]}")
        
        print("\n")
        
        print(f"Documents: {len(all_documents)}")
        print(f"Chunks: {len(chunks)}")
        
        print("\nSEPARAÇÕES\n")
        print(chunks[0].page_content)
        
        print("\nSEPARAÇÕES\n")
        print(chunks[1].page_content)
        
        
    except Exception as e:
        print(f"Erro:{e}")

if __name__ == "__main__":
    main()