"""
Random Joke Generator
Uses the JokeAPI (https://jokeapi.dev) to fetch random jokes
"""

import requests
import json
from typing import Dict, Optional

API_URL = "https://v2.jokeapi.dev/joke/Any"

def get_random_joke() -> Dict:
    """
    Fetches a random joke from the JokeAPI
    
    Returns:
        Dict: Joke object containing the joke content and metadata
    """
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        
        joke_data = response.json()
        
        # Handle different joke types
        if joke_data.get('type') == 'single':
            return {
                'joke': joke_data.get('joke'),
                'type': 'single',
                'category': joke_data.get('category')
            }
        elif joke_data.get('type') == 'twopart':
            return {
                'joke': f"{joke_data.get('setup')}\n{joke_data.get('delivery')}",
                'type': 'twopart',
                'category': joke_data.get('category')
            }
        
        return joke_data
    
    except requests.exceptions.RequestException as error:
        return {
            'error': True,
            'message': f'Failed to fetch a joke: {str(error)}'
        }

def display_joke() -> None:
    """Displays a formatted joke"""
    print('\n🎭 Getting a random joke...\n')
    
    joke_data = get_random_joke()
    
    if joke_data.get('error'):
        print(f"❌ {joke_data.get('message')}")
    else:
        print(f"📂 Category: {joke_data.get('category')}")
        print(f"✨ {joke_data.get('joke')}")
        print()

if __name__ == "__main__":
    display_joke()
