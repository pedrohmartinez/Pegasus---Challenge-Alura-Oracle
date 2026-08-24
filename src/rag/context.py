def build_context(results):
    
    context = ""
    
    for result in results:
        
        context += result["document"]
        context += "\n\n"
        
    return context