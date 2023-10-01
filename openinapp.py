

from googletrans import Translator, LANGUAGES

def translate_to_hindi(text):
    try:
        # Initialize the translator
        translator = Translator()

        # Detect the source language (English in this case)
        detected_lang = translator.detect(text).lang

        # Translate the text to Hindi
        translation = translator.translate(text, src=detected_lang, dest='hi')

        # Return the translated text in Hindi
        return translation.text

    except Exception as e:
        print("An error occurred during translation:", str(e))
        return None

# Example usage:
english_text = input("Enter the sentence: ")
hindi_translation = translate_to_hindi(english_text)



hindi_to_english = {
    "नमस्ते,": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "मैंसे": "from me",
    "आपसे": "from you",
    "समय": "time",
    "स्थान": "place",
    "खुशी": "happiness",
    "प्यार": "love",
    "खाना": "food",
    "पानी": "water",
    "दिन": "day",
    "रात": "night",
    "सूरज": "sun",
    "चाँद": "moon",
    "मनुष्य": "human",
    "गाड़ी": "car",
    "मोबाइल": "mobile phone",
    "किताब": "book",
    "स्कूल": "school",
    "बच्चा": "child",
    "शेयर": "share",
    "तुम्हारा": "your",

    "द": "the",

      "इंतजार": "wait",
    "बैग": "bag",
    "वीडियो": "video",
    "उल्लेख": "mention",
    "उत्पाद": "product",
    "उत्पादों": "products",

     "टिप्पणी": "comment",
    "अनुभाग": "section",
    "प्रतिक्रिया": "feedback",
    "साझा": "share",
    "भूरा":"brown",
    "लोमड़ी":"fox",
    "कुत्ते":"dog",
    "मिनट":"minute",
    "हेडसेट":"headset",
    "डेमो":"demo",
    "आइए":"lets",
    "देखें":"see",
    "पार्टी":"party",
    "बाजार":"market",
    "मैथ्स":"maths",
    "क्लास":"class",
    "परीक्षा":"exam",
    "एग्जाम":"exam",
    "क्रिकेट":"cricket"

}



def convert_hindi_to_english(sentence):
    words = sentence.split()  # Split the sentence into words
    translated_words = []

    for word in words:
        # Check if the word is in the mapping, if yes, translate it, otherwise keep it as is
        translated_word = hindi_to_english.get(word, word)
        translated_words.append(translated_word)

    # Join the translated words to form the translated sentence
    translated_sentence = " ".join(translated_words)
    return translated_sentence

# Example usage:
english_translation = convert_hindi_to_english(hindi_translation)
print(english_translation)