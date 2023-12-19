import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
    "type": "interval",
    "data": [
        { "genre": 'Sports', "sold": 275 },
        { "genre": 'Strategy', "sold": 115 },
        { "genre": 'Action', "sold": 120 },
        { "genre": 'Shooter', "sold": 350 },
        { "genre": 'Other', "sold": 150 },
    ],
    "encode": {
        "x": "genre",
        "y": "sold",
        "color": "genre",
    }
}

g2(options=options, style=None, key="streamlit_g2")
