import streamlit as st

st.title("Our Projects")

projects = [
    {"title": "Clean Water Initiative", "desc": "Bringing safe drinking water to rural areas."},
    {"title": "School Supplies Drive", "desc": "Providing students the tools to learn."},
    {"title": "Medical Outreach", "desc": "Healthcare access for vulnerable populations."}
]

for project in projects:
    with st.container():
        st.subheader(project["title"])
        st.write(project["desc"])
        st.divider()
