import asyncio
from googletrans import Translator

# List of supported languages
LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi"
}

def translate_text(text, dest_lang="es"):  
    translator = Translator()
    loop = asyncio.new_event_loop()  # Create an event loop
    asyncio.set_event_loop(loop)
    
    translation = loop.run_until_complete(translator.translate(text, dest=dest_lang))  # Run async function
    return translation.text  # Extract translated text
