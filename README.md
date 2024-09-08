# Smart_Dashboard

## Overview

Smart_Dashboard consist  of LLM-Powered Dashboard Generator is a Streamlit-based web application that uses Large Language Models (LLMs) to analyze data and automatically generate insightful visualizations. This tool allows users to upload CSV files, select data columns for visualization, and receive AI-generated analysis of their data.

## Features

- CSV file upload and preview
- AI-powered data analysis using Groq LLM
- Dynamic visualization generation (bar, line, and scatter plots)
- Interactive dashboard with customizable charts
- Responsive design for various screen sizes
![image](https://github.com/user-attachments/assets/d5fa2888-b840-4b16-850d-cfca195599ef)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 
- pip (Python package manager)
- A Groq API key

## Installation

1. Clone this repository &active ur environment:
```
git clone https://github.com/RkanGen/Smart-Dashboard.git
cd Smart-Dashboard
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
2. `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
```
## Usage

1. Run the Streamlit app:
```
streamlit run app.py
```


## Customization

You can customize the app's appearance by modifying the `style.css` file. The main application logic is contained in `app.py`, which you can edit to add new features or modify existing functionality.
![image](https://github.com/user-attachments/assets/6ffe9fc9-992d-4947-a521-9686dc89c794)

## Contributing

Contributions to the LLM-Powered Dashboard Generator are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License feel free to modified it - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web app framework
- [Plotly](https://plotly.com/) for interactive visualizations
- [Groq](https://groq.com/) for the LLM API

