"""
preprocessor.py - Module for text preprocessing and cleaning
Functional Requirement: Data input & processing
"""

import re
import string
import logging
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
import nltk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextPreprocessor:
    """Preprocess and clean email text data."""
    
    def __init__(self):
        """Initialize TextPreprocessor with stopwords."""
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = set(string.punctuation)
    
    def clean_text(self, text):
        """
        Clean and normalize text.
        
        Args:
            text (str): Raw text to clean
            
        Returns:
            str: Cleaned text
        """
        if not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize(self, text):
        """
        Tokenize text into words.
        
        Args:
            text (str): Text to tokenize
            
        Returns:
            list: List of tokens
        """
        tokens = word_tokenize(text)
        return tokens
    
    def remove_stopwords(self, tokens):
        """
        Remove common stopwords and punctuation.
        
        Args:
            tokens (list): List of tokens
            
        Returns:
            list: Filtered tokens
        """
        filtered = [
            token for token in tokens 
            if token not in self.stop_words and token not in self.punctuation
            and len(token) > 2
        ]
        return filtered
    
    def preprocess(self, text):
        """
        Full preprocessing pipeline.
        
        Args:
            text (str): Raw text to preprocess
            
        Returns:
            str: Preprocessed text (space-separated tokens)
        """
        # Clean
        text = self.clean_text(text)
        
        # Tokenize
        tokens = self.tokenize(text)
        
        # Remove stopwords
        tokens = self.remove_stopwords(tokens)
        
        # Join back to string
        return ' '.join(tokens)
    
    def preprocess_batch(self, texts):
        """
        Preprocess multiple texts.
        
        Args:
            texts (list): List of text strings
            
        Returns:
            list: List of preprocessed texts
        """
        return [self.preprocess(text) for text in texts]


def validate_preprocessing(original, preprocessed):
    """
    Validate preprocessing output.
    
    Args:
        original (str): Original text
        preprocessed (str): Preprocessed text
        
    Returns:
        dict: Validation statistics
    """
    return {
        'original_length': len(original),
        'preprocessed_length': len(preprocessed),
        'reduction_ratio': (1 - len(preprocessed)/len(original)) * 100 if len(original) > 0 else 0,
        'is_valid': len(preprocessed) > 0
    }


if __name__ == '__main__':
    # Example usage
    preprocessor = TextPreprocessor()
    
    sample_emails = [
        "You have WON $1000! Click here NOW to claim your PRIZE!!!",
        "Hi John, let's meet tomorrow at 2pm to discuss the project",
        "URGENT: Your account has been compromised. Update password NOW!"
    ]
    
    logger.info("\n===== TEXT PREPROCESSING DEMO =====")
    for email in sample_emails:
        preprocessed = preprocessor.preprocess(email)
        stats = validate_preprocessing(email, preprocessed)
        logger.info(f"Original: {email[:50]}...")
        logger.info(f"Processed: {preprocessed[:50]}...")
        logger.info(f"Stats: {stats}\n")
