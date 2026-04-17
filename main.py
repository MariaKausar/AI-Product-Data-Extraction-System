from fastapi import FastAPI
import re

app = FastAPI()

# helper function
def safe_extract(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


def extract_price_number(price_text):
    if not price_text:
        return None
    numbers = ''.join(filter(str.isdigit, price_text))
    return int(numbers) if numbers else None


@app.get("/")
def home():
    return {"message": "AI Data Extractor is running 🚀"}


@app.post("/extract")
def extract_data(text: str):

    # normalize input
    text = text.replace("\n", " ")

    data = {}

    # -------------------------
    # EXTRACTION PART
    # -------------------------
    data["product"] = safe_extract(
        r"Product:\s*(.*?)(?=Material:|Price:|Sustainability:|$)", text
    )

    data["material"] = safe_extract(
        r"Material:\s*(.*?)(?=Price:|Sustainability:|$)", text
    )

    data["price"] = safe_extract(
        r"Price:\s*(.*?)(?=Sustainability:|$)", text
    )

    data["sustainability"] = safe_extract(
        r"Sustainability:\s*(.*)", text
    )

    # -------------------------
    # FEATURE 1: eco_friendly
    # -------------------------
    if data["sustainability"] and "Recyclable" in data["sustainability"]:
        data["eco_friendly"] = True
    else:
        data["eco_friendly"] = False

    # -------------------------
    # FEATURE 2: price_category
    # -------------------------
    price_value = extract_price_number(data["price"])

    if price_value is not None:
        data["price_category"] = "expensive" if price_value > 100 else "cheap"
    else:
        data["price_category"] = "unknown"

    # -------------------------
    # FEATURE 3: sustainability_score
    # -------------------------
    score = 0

    if data["sustainability"] and "Recyclable" in data["sustainability"]:
        score += 1

    if data["material"] and "Wood" in data["material"]:
        score += 1

    data["sustainability_score"] = score

    # -------------------------
    # FEATURE 4: confidence score
    # -------------------------
    filled_fields = 0

    for key in ["product", "material", "price", "sustainability"]:
        if data.get(key):
            filled_fields += 1

    data["confidence"] = round(filled_fields / 4, 2)

    return data