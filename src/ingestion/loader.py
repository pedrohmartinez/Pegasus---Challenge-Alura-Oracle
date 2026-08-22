from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

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

def load_pdf(pdf_path: Path):

    loader = PyMuPDFLoader(str(pdf_path))

    documents = loader.load()

    return documents

def load_all_pdfs(pdf_directory: str):
    directory = Path(pdf_directory)
    
    pdf_files = list(directory.glob("*.pdf"))  
    
    all_documents = []

    for pdf_path in pdf_files:
        loader = PyMuPDFLoader(str(pdf_path))
        
        dados_pdf = loader.load()
        
        all_documents.extend(dados_pdf)
        
    return all_documents
