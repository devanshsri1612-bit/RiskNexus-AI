import pandas as pd

# Load CSV files
users = pd.read_csv("users.csv")
transactions = pd.read_csv("transactions.csv")

def analyze_transaction(txn_id):

    txn = transactions[transactions["txn_id"] == txn_id].iloc[0]

    user = users[users["user_id"] == txn["user_id"]].iloc[0]

    similarity = 100
    reasons = []

    # Amount check
    if txn["amount"] > user["avg_amount"] * 5:
        similarity -= 40
        reasons.append("Amount unusually high")

    # Device check
    if txn["device"] != user["usual_device"]:
        similarity -= 30
        reasons.append("New device detected")

    # Location check
    if txn["location"] != user["usual_location"]:
        similarity -= 30
        reasons.append("Location mismatch")

    similarity = max(similarity, 0)

    return {
        
        "Transaction ID": txn_id,
        "Similarity Score": similarity,
        "Reasons": reasons

    }

if __name__ == "__main__":
    result = analyze_transaction("TX011")
    print(result)