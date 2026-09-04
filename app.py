import json 
import pandas as pd
import streamlit as st
from decision_engine import make_decision

# Page Config
st.set_page_config(
    page_title="RiskNexus AI",
    page_icon="🛡️",
    layout="wide"
)

# Header
st.title("🛡️ RiskNexus AI")
st.subheader("Intelligent Transaction Risk Assessment System")

st.markdown("---")

# Input Section
col1, col2, col3 = st.columns(3)

with col1:
    txn_id = st.text_input(
        "Transaction ID",
        value="TX011"
    )

with col2:
    merchant_id = st.text_input(
        "Merchant ID",
        value="M002"
    )

with col3:
    user_id = st.text_input(
        "User ID",
        value="U004"
    )

st.markdown("")

# Analyze Button
if st.button("🔍 Analyze Transaction", use_container_width=True):

    result = make_decision(
        txn_id,
        merchant_id,
        user_id
    )

    st.markdown("---")

    # Metrics Row
    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            label="Risk Score",
            value=result["Risk Score"]
        )

    with m2:
        st.metric(
            label="Trust Score",
            value=result["Trust Score"]
        )

    with m3:
        st.metric(
            label="Confidence",
            value=result["Confidence"]
        )

    st.markdown("---")

    # Decision Banner
    st.subheader("Final Decision")

    if result["Decision"] == "BLOCK":
        st.error("🚫 BLOCK TRANSACTION")

    elif result["Decision"] == "REVIEW":
        st.warning("⚠️ MANUAL REVIEW REQUIRED")

    else:
        st.success("✅ APPROVE TRANSACTION")

    st.markdown("---")
    # AI Investigation Summary

    st.subheader("🤖 AI Investigation Summary")

    summary = f"""
    Transaction {txn_id} was marked as {result['Decision']}.

    Reasons identified:
    """

    for reason in result["Reasons"]:
        summary += f"\n• {reason}"

    if result["Trust Score"] < 50:
        summary += "\n• Merchant trust score is below acceptable threshold."

    if result["Graph Risk"] == "HIGH":
        summary += "\n• Network analysis detected suspicious associations."

    st.info(summary)

    st.markdown("---")
            # AI Investigation Summary

    st.subheader("🤖 AI Investigation Summary")

    summary = f"""
    Transaction {txn_id} was marked as {result['Decision']}.

    Reasons identified:
    """

    for reason in result["Reasons"]:
        summary += f"\n• {reason}"

    if result["Trust Score"] < 50:
        summary += "\n• Merchant trust score is below acceptable threshold."

    if result["Graph Risk"] == "HIGH":
        summary += "\n• Network analysis detected suspicious associations."

    st.info(summary)

    st.markdown("---")

    # Risk Summary
    st.subheader("Risk Summary")

    left, right = st.columns(2)

    with left:
        st.info(
            f"Graph Risk Level: **{result['Graph Risk']}**"
        )

    with right:
        st.info(
            f"Decision Confidence: **{result['Confidence']}**"
        )
    st.subheader("Why was this flagged?")

    for reason in result["Reasons"]:
        st.write("•", reason)

    st.markdown("---")
    st.subheader("🎯 Risk Meter")

    risk_score = result["Risk Score"]

    st.progress(risk_score / 100)

    st.write(f"Current Risk Score: {risk_score}/100")

    if risk_score >= 70:
        st.error(f"🔴 HIGH RISK ({risk_score}/100)")

    elif risk_score >= 40:
        st.warning(f"🟠 MEDIUM RISK ({risk_score}/100)")

    else:
        st.success(f"🟢 LOW RISK ({risk_score}/100)")

    st.progress(int(result["Risk Score"]))

    st.write(
        f"Current Risk Score: {result['Risk Score']}/100"
    )
    st.markdown("---")
    # Risk Status Color

    risk_score = result["Risk Score"]

    if risk_score >= 70:
        st.error(f"🔴 High Risk ({risk_score}/100)")
    elif risk_score >= 40:
        st.warning(f"🟠 Medium Risk ({risk_score}/100)")
    else:
        st.success(f"🟢 Low Risk ({risk_score}/100)")

    st.subheader("Risk vs Trust Analysis")

    chart_data = pd.DataFrame(
        {
            "Metric": ["Risk Score", "Trust Score"],
            "Value": [
                result["Risk Score"],
                result["Trust Score"]
            ]
        }
    )

    st.bar_chart(
        chart_data.set_index("Metric")
    )

    st.markdown("---")

    # Full Report
    st.subheader("Investigation Report")

    st.json(result)
    st.download_button(
    "📄 Download Investigation Report",
    data=json.dumps(result, indent=4),
    file_name="investigation_report.json",
    mime="application/json"
)

    st.success("Analysis Completed Successfully")