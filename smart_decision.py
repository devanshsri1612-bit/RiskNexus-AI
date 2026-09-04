from risk_engine import calculate_risk
from trustlens import calculate_trust_score
from graph_engine import investigate_entity

def smart_decision(txn_id, merchant_id, user_id):

    risk = calculate_risk(txn_id)
    trust = calculate_trust_score(merchant_id)
    graph = investigate_entity(user_id)

    score = 0

    # Risk Engine
    if risk["Risk Score"] >= 70:
        score += 1

    # TrustLens
    if trust["Trust Score"] < 50:
        score += 1

    # Graph Engine
    if graph["Graph Risk"] == "HIGH":
        score += 1

    if score == 3:
        decision = "BLOCK"
        confidence = "95%"

    elif score == 2:
        decision = "REVIEW"
        confidence = "75%"

    else:
        decision = "ALLOW"
        confidence = "60%"

    return {
        "Transaction": txn_id,
        "User": user_id,
        "Merchant": merchant_id,
        "Risk Score": risk["Risk Score"],
        "Trust Score": trust["Trust Score"],
        "Graph Risk": graph["Graph Risk"],
        "Decision": decision,
        "Confidence": confidence
    }


result = smart_decision(
    "TX011",
    "M002",
    "U004"
)

print(result)