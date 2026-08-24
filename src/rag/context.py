def build_context(results):
    
    context_parts = []
    
    for index, result in enumerate(results, start=1):
        
        document = result["document"]
        
        chunk = (
            f"================ CHUNK {index} ================\n\n"
            f"{document}\n"
        ) 
        
        context_parts.append(chunk)
        
    return "\n".join(context_parts)