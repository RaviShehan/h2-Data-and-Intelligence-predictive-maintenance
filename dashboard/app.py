from dashboard.dashboard_utils import normalize_predictions

import pandas as pd
import requests
import streamlit as st


API_BASE_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="H3 Predictive Maintenance Dashboard",
    layout="wide"
)


def fetch_data(endpoint: str, default):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as error:
        st.error(f"Could not load {endpoint}: {error}")
        return default


st.title("H3 Predictive Maintenance Dashboard")

st.write(
    "This dashboard visualizes machine prediction history, risk levels, "
    "model information, model evaluation, feature importance, and system health from the H2 API."
)


if st.button("Refresh Dashboard"):
    st.rerun()


health_data = fetch_data("/", {})
prediction_response = fetch_data("/predictions", {"predictions": []})
predictions = normalize_predictions(prediction_response)

model_info = fetch_data("/model-info", {})
model_evaluation = fetch_data("/model-evaluation", {})
feature_importance = fetch_data("/feature-importance", {})
system_health = fetch_data("/system-health", {})


st.sidebar.title("System Status")

if health_data:
    st.sidebar.success("FastAPI is running")
else:
    st.sidebar.error("FastAPI is not reachable")

st.sidebar.write("API Base URL:")
st.sidebar.code(API_BASE_URL)


tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Prediction History",
        "Risk Summary",
        "Model Information",
        "Feature Importance",
        "System Health",
    ]
)


with tab1:
    st.header("Latest Prediction Records")

    if predictions:
        df = pd.DataFrame(predictions)

        st.subheader("Full Prediction Data")
        st.dataframe(df, use_container_width=True)

        st.subheader("Latest Machines")

        display_columns = [
            "machine_id",
            "temperature",
            "vibration_total",
            "rpm",
            "risk_level",
            "failure_probability",
            "recommended_action",
            "is_anomaly",
            "created_at",
        ]

        available_columns = [
            column
            for column in display_columns
            if column in df.columns
        ]

        if available_columns:
            st.dataframe(df[available_columns], use_container_width=True)
        else:
            st.warning("Prediction records were found, but expected columns are missing.")
            st.write("Available columns:")
            st.write(list(df.columns))
    else:
        st.warning("No prediction records found yet.")


with tab2:
    st.header("Machine Risk Summary")

    if predictions:
        df = pd.DataFrame(predictions)

        if "risk_level" in df.columns:
            col1, col2, col3, col4 = st.columns(4)

            total_predictions = len(df)
            critical_count = len(df[df["risk_level"] == "CRITICAL"])
            warning_count = len(df[df["risk_level"] == "WARNING"])
            normal_count = len(df[df["risk_level"] == "NORMAL"])

            col1.metric("Total Predictions", total_predictions)
            col2.metric("Critical", critical_count)
            col3.metric("Warning", warning_count)
            col4.metric("Normal", normal_count)

            st.subheader("Risk Level Count")
            risk_counts = df["risk_level"].value_counts()
            st.bar_chart(risk_counts)
        else:
            st.warning("risk_level column is not available in prediction records.")
            st.write("Available columns:")
            st.write(list(df.columns))

        if "is_anomaly" in df.columns:
            st.subheader("Anomaly Count")
            anomaly_counts = df["is_anomaly"].value_counts()
            st.bar_chart(anomaly_counts)
    else:
        st.warning("No prediction records available for summary.")


with tab3:
    st.header("Model Information")

    if model_info:
        accuracy_value = model_info.get(
            "accuracy",
            model_info.get("accuracy_score", "N/A"),
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Model Type", model_info.get("model_type", "N/A"))
        col2.metric("Accuracy", accuracy_value)
        col3.metric("Model Available", model_info.get("model_available", "N/A"))

        st.subheader("Dataset Source")
        st.write(model_info.get("dataset_source", "N/A"))

        st.subheader("Input Features")
        st.write(model_info.get("input_features", []))

        st.subheader("Risk Classes")
        st.write(model_info.get("risk_classes", []))

        st.subheader("Full Model Metadata")
        st.json(model_info)
    else:
        st.warning("Model information not available.")

    st.header("Model Evaluation")

    if model_evaluation:
        st.json(model_evaluation)
    else:
        st.warning("Model evaluation report not available.")


with tab4:
    st.header("Feature Importance")

    importance_list = feature_importance.get("feature_importance", [])

    if importance_list:
        importance_df = pd.DataFrame(importance_list)

        st.subheader("Feature Importance Table")
        st.dataframe(importance_df, use_container_width=True)

        if "feature" in importance_df.columns and "importance" in importance_df.columns:
            st.subheader("Feature Importance Chart")
            chart_df = importance_df.set_index("feature")
            st.bar_chart(chart_df["importance"])
        else:
            st.warning("Feature importance data does not contain expected columns.")
            st.write("Available columns:")
            st.write(list(importance_df.columns))
    else:
        st.warning("Feature importance report not available.")


with tab5:
    st.header("H4 System Health Monitoring")

    if system_health:
        col1, col2, col3 = st.columns(3)

        col1.metric("Overall Status", system_health.get("overall_status", "N/A"))
        col2.metric("API Status", system_health.get("api_status", "N/A"))
        col3.metric("Database Status", system_health.get("database_status", "N/A"))

        st.subheader("Platform Checks")

        check_data = {
            "Check": [
                "Model File Available",
                "Evaluation Report Available",
                "Feature Importance Available",
            ],
            "Status": [
                system_health.get("model_file_available", False),
                system_health.get("evaluation_report_available", False),
                system_health.get("feature_importance_available", False),
            ],
        }

        check_df = pd.DataFrame(check_data)
        st.dataframe(check_df, use_container_width=True)

        st.subheader("Full System Health Response")
        st.json(system_health)
    else:
        st.warning("System health information is not available.")