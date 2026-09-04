import pandas as pd

merchants = pd.read_csv("merchant.csv")

def calculate_trust_score(merchant_id):

    merchant = merchants[
        merchants["merchant_id"] == merchant_id
    ].iloc[0]

    score = 100

    score -= (5 - merchant["rating"]) * 10
    score -= merchant["complaints"]
    score -= merchant["chargebacks"] * 2

    score = max(0, round(score))

    if score >= 80:
        level = "TRUSTED"
    elif score >= 50:
        level = "MODERATE"
    else:
        level = "RISKY"

    return {
        "Merchant ID": merchant_id,
        "Trust Score": score,
        "Trust Level": level
    }

if __name__ == "__main__":
    print(calculate_trust_score("M002"))