import unicodedata

from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
def similarity(embedding1, embedding2):
    return util.cos_sim(embedding1, embedding2)
    # return cosine_similarity([doc1, doc2])

def similarity_minus_one(embedding1, embedding2):
    return 1 - util.cos_sim(embedding1, embedding2)

def transliterate_to_ascii(s):
    # Normalize unicode characters to their closest ASCII representation
    normalized = unicodedata.normalize('NFKD', s)

    # Encode to ASCII bytes, then decode back to string, ignoring non-ASCII characters
    ascii_encoded = normalized.encode('ascii', 'ignore').decode('ascii')

    # Custom replacements for specific characters
    replacements = {
        'ı': 'i',
        'ğ': 'g',
        "ç": "c",
        "ö": "o",
        "ü": "u",
    }

    # Apply custom replacements
    result = ''.join(replacements.get(char, char) for char in ascii_encoded)

    return result