from typing import Dict

def get_file_extension(language: str) -> str:
    
    # Dictionary mapping programming languages to file extensions
    extensions: Dict[str, str] = {
        'python': '.py', 'java': '.java', 'javascript': '.js', 'c': '.c', 'cpp': '.cpp',
        'ruby': '.rb', 'go': '.go', 'swift': '.swift', 'php': '.php', 'html': '.html',
        'css': '.css', 'kotlin': '.kt', 'rust': '.rs', 'typescript': '.ts', 'shell': '.sh',
        'scala': '.scala', 'dart': '.dart',
        # Add more languages and their extensions as needed
    }

    # Normalize input to lowercase and trim whitespace
    language = language.strip().lower()

    # Alias for common variations
    language_variants = {
        'c++': 'cpp',
        'c#': 'csharp',  # This is added hypothetically, not supported in the extensions
        'html5': 'html',
        # Add more variants here if needed
    }

    # Check the dictionary for the language or its variant
    normalized_language = language_variants.get(language, language)

    # Return the file extension or a not recognized message
    return extensions.get(normalized_language, 'Language not recognized')
    
if __name__ == "__main__":
    get_file_extension(language)