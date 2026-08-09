import pathlib

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Simpan · Tax Relief Tracker",
    page_icon="🧾",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Strip Streamlit's default chrome (padding, header, footer, sidebar toggle)
# so the embedded app can use the full viewport, exactly like the standalone
# HTML file does.
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        div.block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        iframe {
            display: block;
        }
        .stApp {
            background: #0D1310;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Load the original Simpan app (single self-contained HTML/CSS/JS file) and
# render it verbatim inside an iframe. This keeps the UI, animations,
# bottom-sheet interactions and localStorage-based persistence 100% identical
# to the standalone HTML file — Streamlit is just hosting it.
# ---------------------------------------------------------------------------
APP_HTML_PATH = pathlib.Path(__file__).parent / "assets" / "simpan_app.html"
html_code = APP_HTML_PATH.read_text(encoding="utf-8")

components.html(html_code, height=900, scrolling=True)
