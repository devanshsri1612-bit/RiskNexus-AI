import pandas as pd

graph = pd.read_csv("graph_data.csv")

def investigate_entity(user_id):

    user = graph[graph["user_id"] == user_id]

    if len(user) == 0:
        return "User Not Found"

    device = user.iloc[0]["device_id"]
    merchant = user.iloc[0]["merchant_id"]

    same_device = graph[
        graph["device_id"] == device
    ]["user_id"].tolist()

    same_merchant = graph[
        graph["merchant_id"] == merchant
    ]["user_id"].tolist()

    risk = "LOW"

    if len(same_device) > 2 or len(same_merchant) > 3:
        risk = "HIGH"

    return {
        "User": user_id,
        "Device": device,
        "Merchant": merchant,
        "Connected Users (Device)": same_device,
        "Connected Users (Merchant)": same_merchant,
        "Graph Risk": risk
    }

if __name__ == "__main__":
    print(investigate_entity("U004"))