import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlparse
import time
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Recipe data with titles and URLs
recipes = [
    {"title_da": "Spinat vafler", "url": "https://www.valdemarsro.dk/spinatvafler/"},
    {"title_da": "Crispy Kylling burger", "url": "https://www.valdemarsro.dk/burger-med-crispy-kylling/"},
    {"title_da": "Pokebowl m kylling", "url": "https://bellasmadunivers.dk/opskrift/hjemmelavet-poke-bowl-med-teriyaki-kylling/"},
    {"title_da": "Pasta carbonara", "url": "https://www.valdemarsro.dk/carbonara_opskrift/"},
    {"title_da": "Torske-Tacos", "url": "https://mambeno.dk/opskrifter/fish-tacos-med-paneret-torsk-mangosalat-og-dressing/"},
    {"title_da": "Kebab med grøntsager", "url": "https://mambeno.dk/opskrifter/durum-med-kebab-groentsager-dressing-og-pommes-frites/"},
    {"title_da": "Fladbrød", "url": "https://mambeno.dk/opskrifter/hjemmelavede-fladbroed/"},
    {"title_da": "Mac and Cheese", "url": "https://mambeno.dk/opskrifter/krydret-mac-and-cheese-med-oksekoed-og-kidneyboenner-til-to-dage/"},
    {"title_da": "Sød kartoffel gryde", "url": "https://stinna.dk/aftensmad/soed-kartoffel-gryde.html"},
    {"title_da": "Lasagne", "url": "https://www.valdemarsro.dk/lasagne/"},
    {"title_da": "Bønne gryde", "url": "https://www.valdemarsro.dk/boennegryde/"},
    {"title_da": "Butter chicken", "url": "https://gourministeriet.dk/cremet-butter-chicken/?fbclid=IwAR1W2yApwRrK1cG281-Qyyu3J-cAiyc9WWLDInnjhFy3u5nAoWPoVKZqPxo"},
    {"title_da": "Quesadillas med kylling", "url": "https://martinys.dk/quesadillas-med-kylling/"},
    {"title_da": "Vegetar lasagne", "url": "https://www.louisesmadblog.dk/super-laekker-vegetarlasagne/"},
    {"title_da": "Thai inspireret farsbrød", "url": "https://mambeno.dk/opskrifter/thai-inspireret-farsbroed-med-ris-kokossauce-og-peanuts-til-to-dage/"},
]

# English translations for common Danish cooking terms
translations = {
    "spinat": "spinach",
    "vafler": "waffles",
    "kylling": "chicken",
    "oksekød": "beef",
    "grisekød": "pork",
    "fisk": "fish",
    "laks": "salmon",
    "torsk": "cod",
    "kartofler": "potatoes",
    "kartoffel": "potato",
    "løg": "onion",
    "hvidløg": "garlic",
    "tomat": "tomato",
    "tomater": "tomatoes",
    "champignon": "mushroom",
    "champignoner": "mushrooms",
    "porre": "leek",
    "broccoli": "broccoli",
    "blomkål": "cauliflower",
    "gurkemeje": "turmeric",
    "chili": "chili",
    "salt": "salt",
    "peber": "pepper",
    "olie": "oil",
    "smør": "butter",
    "fløde": "cream",
    "mel": "flour",
    "sukker": "sugar",
    "ægge": "egg",
    "æg": "egg",
    "mælk": "milk",
    "ost": "cheese",
    "bacon": "bacon",
    "dressing": "dressing",
    "sovs": "sauce",
    "krydderi": "spice",
    "timian": "thyme",
    "oregano": "oregano",
    "basilikum": "basil",
    "persille": "parsley",
    "koriander": "coriander",
    "ginger": "ginger",
    "ingefær": "ginger",
    "cheddar": "cheddar",
    "bønner": "beans",
    "salsa": "salsa",
    "tortilla": "tortilla",
    "cremet": "creamy",
    "sød": "sweet",
    "gryde": "stew",
    "risret": "rice dish",
    "taco": "taco",
    "lasagne": "lasagne",
    "carbonara": "carbonara",
    "burger": "burger",
}

def translate_to_english(danish_text):
    text = danish_text.lower()
    result = danish_text

    for da, en in translations.items():
        result = re.sub(r'\b' + da + r'\b', en, result, flags=re.IGNORECASE)

    return result

def parse_ingredient(ingredient_text):
    ingredient_text = ingredient_text.strip()

    # Simple pattern: amount unit? name
    pattern = r'^([\d\s\-½¼¾⅓⅔]*?)\s+(tsk|tsk\.|spsk|spsk\.|dl|g|kg|ml|stk|stk\.|handful|teaspoon|tablespoon|gram|kilogram)[\.\s]+(.*?)$|^(.+)$'

    match = re.match(pattern, ingredient_text, re.IGNORECASE)

    if match and match.group(3):
        amount = match.group(1).strip() if match.group(1) else None
        unit = match.group(2).strip() if match.group(2) else None
        name = match.group(3).strip()

        return {
            "amount": amount if amount else None,
            "unit": unit if unit else None,
            "name": name
        }
    elif match:
        return {
            "amount": None,
            "unit": None,
            "name": ingredient_text
        }

    return {
        "amount": None,
        "unit": None,
        "name": ingredient_text
    }

def looks_like_ingredient(text):
    text_lower = text.lower()

    skip_patterns = [
        'opskrift', 'madplan', 'indkøbsliste', 'favoritter', 'nyheds',
        'kontakt', 'log', 'kurv', 'tilbehør', 'hjælp', 'betingelser',
        'trustpilot', 'facebook', 'instagram', 'kundeservice', 'send',
        'opret', 'ansøg', 'donner', 'forskel', 'billeder', 'video',
        'trin', 'sted', 'chef', 'timer', 'varighed', 'svær',
        'delicious', 'security', 'incident'
    ]

    if any(pattern in text_lower for pattern in skip_patterns):
        return False

    if len(text) < 3 or len(text) > 200:
        return False

    has_number = any(char.isdigit() for char in text)
    has_unit = any(unit in text.lower() for unit in ['gram', 'ml', 'tsk', 'spsk', 'dl', 'stk', 'liter', 'g '])

    if text.count('\n') > 0:
        return False

    return has_number or has_unit or (len(text) < 80 and len(text.split()) < 15)

def scrape_recipe(title, url):
    print(f"Scraping: {title}")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')

        ingredients = []

        # Try to find ingredient section
        for section in soup.find_all(['div', 'section', 'article']):
            section_text = section.get_text().lower()
            if 'ingrediens' in section_text or 'ingredient' in section_text:
                lis = section.find_all('li')
                if lis:
                    for li in lis:
                        text = li.get_text().strip()
                        if text and looks_like_ingredient(text):
                            parsed = parse_ingredient(text)
                            if parsed['name']:
                                ingredients.append(parsed)
                    if len(ingredients) > 3:
                        break

        # If still no ingredients, try all lists
        if not ingredients or len(ingredients) < 3:
            for ul in soup.find_all('ul')[:10]:
                lis = ul.find_all('li')
                if 2 <= len(lis) <= 50:
                    temp_ingredients = []
                    for li in lis:
                        text = li.get_text().strip()
                        if text and looks_like_ingredient(text):
                            parsed = parse_ingredient(text)
                            if parsed['name']:
                                temp_ingredients.append(parsed)
                    if len(temp_ingredients) > len(ingredients):
                        ingredients = temp_ingredients
                    if len(ingredients) > 3:
                        break

        # Remove duplicates
        seen = set()
        unique_ingredients = []
        for ing in ingredients:
            ing_key = ing['name'].lower()
            if ing_key not in seen:
                seen.add(ing_key)
                unique_ingredients.append(ing)

        if not unique_ingredients:
            print(f"  Warning: No ingredients found")

        return {
            "title_da": title,
            "title_en": translate_to_english(title),
            "url": url,
            "ingredients": unique_ingredients[:25]
        }

    except Exception as e:
        print(f"  Error: {str(e)}")
        return {
            "title_da": title,
            "title_en": translate_to_english(title),
            "url": url,
            "ingredients": [],
        }

def main():
    all_recipes = []

    for recipe in recipes:
        result = scrape_recipe(recipe["title_da"], recipe["url"])
        all_recipes.append(result)
        time.sleep(0.5)

    # Create Danish version
    danish_data = {
        "recipes": [
            {
                "titel": r["title_da"],
                "link": r["url"],
                "ingredienser": r.get("ingredients", [])
            }
            for r in all_recipes
        ]
    }

    # Create English version
    english_data = {
        "recipes": [
            {
                "title": r["title_en"],
                "link": r["url"],
                "ingredients": r.get("ingredients", [])
            }
            for r in all_recipes
        ]
    }

    # Write Danish JSON
    with open('recipes_da.json', 'w', encoding='utf-8') as f:
        json.dump(danish_data, f, ensure_ascii=False, indent=2)

    # Write English JSON
    with open('recipes_en.json', 'w', encoding='utf-8') as f:
        json.dump(english_data, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Saved to recipes_da.json and recipes_en.json")

if __name__ == "__main__":
    main()
