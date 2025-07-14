import streamlit as st

st.set_page_config(page_title="MedTech Solutions", layout="wide")

# Custom CSS for layout, font, and buttons
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', sans-serif;
        background-color: white;
        color: #1d1d1f;
    }

    .header {
        background-color: #001E60;
        padding: 60px 40px;
        text-align: left;
        color: white;
    }

    .header h1 {
        font-size: 3.2em;
        margin-bottom: 10px;
    }

    .header h3 {
        font-weight: 300;
        font-size: 1.5em;
    }

    .btn-main {
        background-color: #0072CE;
        color: white;
        padding: 12px 25px;
        font-size: 16px;
        border: none;
        border-radius: 0px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }

    .btn-main:hover {
        background-color: #005bb5;
    }

    .section {
        padding: 60px 40px;
        background-color: #f5f7fa;
    }

    .section.dark {
        background-color: #ffffff;
    }

    .section h2 {
        font-size: 2.2em;
        margin-bottom: 20px;
    }

    .card {
        background: white;
        padding: 30px;
        border-radius: 6px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="header">
    <h1>MedTech Solutions</h1>
    <h3>Drive innovation and improve patient outcomes with actionable insights from data and expert analytics.</h3>
    <br>
    <a href="#" class="btn-main">Contact Us</a>
</div>
""", unsafe_allow_html=True)

# Value Section
st.markdown("""
<div class="section">
    <h2>Why Choose Our MedTech Solutions?</h2>
    <div class="card">
        <p><strong>Accelerate Product Development:</strong> Bring devices to market faster with data-driven decisions.</p>
        <p><strong>Stay Compliant:</strong> Navigate regulatory pathways with ease and confidence.</p>
        <p><strong>Expand Global Reach:</strong> Understand markets with clarity and precision.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="section dark">
    <h2>Comprehensive Services</h2>
    <div class="card">
        <ul>
            <li><strong>Market Intelligence:</strong> Deep analysis of trends and competitors</li>
            <li><strong>Regulatory Strategy:</strong> Global approval insights from FDA, EU MDR, and more</li>
            <li><strong>Clinical Trial Benchmarking:</strong> Access powerful trial databases</li>
            <li><strong>Custom Research:</strong> Get expert-led reports tailored to your business needs</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Final CTA
st.markdown("""
<div class="section">
    <h2>Let’s Talk</h2>
    <p>Discover how our MedTech solutions can support your business objectives.</p>
    <a href="#" class="btn-main">Schedule a Demo</a>
</div>
""", unsafe_allow_html=True)
