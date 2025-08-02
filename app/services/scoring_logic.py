def compute_transparency_score(text: str) -> float:
    keywords = ["honest", "transparent", "clear"]
    score = sum(word in text.lower() for word in keywords)
    return round(score / len(keywords), 2)