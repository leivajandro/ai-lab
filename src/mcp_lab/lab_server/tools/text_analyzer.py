"""Text analyzer tool for MCP server"""

def text_analyzer(text: str) -> dict:
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text),
        "sentences": len([s for s in text.split('.') if s.strip()])
    }