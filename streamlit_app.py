from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GeoSentials | Disaster Intelligence Command Center",
    page_icon="G",
    layout="wide",
    initial_sidebar_state="collapsed",
)

root = Path(__file__).parent
styles = (root / "styles.css").read_text(encoding="utf-8")
app_script = (root / "app.js").read_text(encoding="utf-8")

html = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <style>{styles}</style>
</head>
<body>
  <div id="app"></div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>{app_script}</script>
</body>
</html>
"""

components.html(html, height=980, scrolling=True)
