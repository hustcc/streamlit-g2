import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Pie", page_icon="📈", layout="wide")


"""
## Pie Chart
"""

options = {
    "autoFit": True,
    "type": "interval",
    "coordinate": {
        "type": "theta"
    },
    "data": [
        { "id": "c", "value": 526 },
        { "id": "sass", "value": 220 },
        { "id": "php", "value": 325 },
        { "id": "elixir", "value": 561 },
        { "id": "rust", "value": 54 }
    ],
    "encode": {
        "y": "value",
        "color": "id"
    },
    "transform": [
        { "type": "stackY" }
    ],
    "style": {
        "radius": 4,
        "stroke": "#fff",
        "lineWidth": 1
    },
    "labels": [
        {
        "text": "value",
        "radius": 0.9
        }
    ],
    "animate": {
        "enter": {
        "type": "waveIn"
        }
    },
    "axis": False,
    "legend": False,
}

g2(options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "type": "interval",
    "coordinate": {
        "type": "theta"
    },
    "data": [
        { "id": "c", "value": 526 },
        { "id": "sass", "value": 220 },
        { "id": "php", "value": 325 },
        { "id": "elixir", "value": 561 },
        { "id": "rust", "value": 54 }
    ],
    "encode": {
        "y": "value",
        "color": "id"
    },
    "transform": [
        { "type": "stackY" }
    ],
    "style": {
        "radius": 4,
        "stroke": "#fff",
        "lineWidth": 1
    },
    "labels": [
        {
        "text": "value",
        "radius": 0.9
        }
    ],
    "animate": {
        "enter": {
        "type": "waveIn"
        }
    },
    "axis": False,
    "legend": False,
}

g2(options=options)
```
""")
