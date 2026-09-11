# GeoSentials

GeoSentials is a browser-runnable Smart India Hackathon 2026 prototype for proactive disaster management decision support.

## Run locally

This workspace is intentionally dependency-light because the demonstration environment may not have Node.js installed.

1. Open `index.html` directly in a browser, or serve the folder with any static server.
2. For a local static server with Python installed:

```powershell
python -m http.server 5500
```

Then open `http://localhost:5500`.

The map uses OpenStreetMap tiles through Leaflet's CDN. An internet connection is needed for the basemap; the command center and simulated data remain local.

## Run with Streamlit

Install the Streamlit dependency and start the hosted version:

```powershell
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the displayed local URL, usually `http://localhost:8501`.

For public deployment, push this folder to GitHub and create a new app at [Streamlit Community Cloud](https://share.streamlit.io). Select `streamlit_app.py` as the main file. Streamlit will install `requirements.txt` automatically.

## Optional FastAPI demo service

```powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The browser prototype currently uses local mock data so it works when the API and database are unavailable. The API provides the replacement seam for future authorized data integrations.

## Demo flow

Dashboard -> click a critical habitation or red zone -> AI Analysis -> Relocation Planner -> Carrying Capacity -> Alerts / Sensors.

All displayed hazards, scores, sensor readings, alerts, and capacities are explicitly simulated prototype data.
