import streamlit as st
import pandas as pd
import plotly.express as px
import groq
from dotenv import load_dotenv
import os

# Set page config at the very beginning
st.set_page_config(page_title="LLM Dashboard Generator", layout="wide")

# Load environment variables
load_dotenv()

# Initialize Groq client with the API key from environment variable
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def analyze_data(data):
    prompt = f"Analyze this data and suggest appropriate visualizations:\n\n{data.head().to_string()}\n\nData types:\n{data.dtypes.to_string()}"
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a data analyst. Suggest appropriate visualizations for the given data."},
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192"
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred while analyzing the data: {str(e)}")
        return None

def create_visualization(data, viz_type, x_axis, y_axis):
    if viz_type == "bar":
        fig = px.bar(data, x=x_axis, y=y_axis)
    elif viz_type == "line":
        fig = px.line(data, x=x_axis, y=y_axis)
    elif viz_type == "scatter":
        fig = px.scatter(data, x=x_axis, y=y_axis)
    else:
        fig = px.bar(data, x=x_axis, y=y_axis)  # Default to bar chart
    
    fig.update_layout(
        title=f"{viz_type.capitalize()} Chart: {y_axis} vs {x_axis}",
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        template="plotly_white"
    )
    return fig

load_css()

st.title("LLM-Powered Dashboard Generator")

col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    with col2:
        st.write("Data Preview:")
        st.dataframe(data.head(), use_container_width=True)

    col3, col4 = st.columns(2)
    
    with col3:
        columns = data.columns.tolist()
        x_axis = st.selectbox("Select X-axis", columns)
    
    with col4:
        y_axis = st.selectbox("Select Y-axis", columns)

    if st.button("Generate Dashboard"):
        with st.spinner("Analyzing data..."):
            analysis = analyze_data(data)
        
        if analysis:
            st.success("Analysis complete!")
            
            tab1, tab2 = st.tabs(["📊 Visualization", "📝 Analysis"])
            
            with tab1:
                viz_type = st.selectbox("Select Visualization Type", ["bar", "line", "scatter"])
                fig = create_visualization(data, viz_type, x_axis, y_axis)
                st.plotly_chart(fig, use_container_width=True)
            
            with tab2:
                st.write("LLM Analysis:")
                st.write(analysis)

    st.write("Full Data Table:")
    st.dataframe(data, use_container_width=True)

else:
    st.info("Please upload a CSV file to get started.")

st.sidebar.header("About")
st.sidebar.info("This app uses LLM to analyze your data and generate a dashboard automatically.")
st.sidebar.markdown("---")
st.sidebar.markdown("Created with ❤️ by Your Rkan")
