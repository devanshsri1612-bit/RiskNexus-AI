from behavioral_dna import analyze_transaction

def calculate_risk(txn_id):

    result = analyze_transaction(txn_id)

    similarity = result["Similarity Score"]

    # Convert similarity to risk
    risk_score = 100 - similarity

    # Assign risk level
    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "Transaction ID": txn_id,
        "Risk Score": risk_score,
        "Risk Level": risk_level,
        "Reasons": result["Reasons"]
    }


if __name__ == "__main__":
    result = calculate_risk("TX011")
    print(result)