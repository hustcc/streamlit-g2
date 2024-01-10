import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Liquid", page_icon="📈", layout="wide")


"""
## Liquid Chart
"""

options = {
    "autoFit": True,
    "type": "liquid",
    "data": { "value": 0.64 },
    "style": {
        "outlineBorder": 4,
        "outlineDistance": 4,
        "waveLength": 256,
        "textFontSize": 64,
        "textFill": "white",
    },
}

g2(options=options)

st.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "type": "liquid",
    "data": { "value": 0.64 },
    "style": {
        "outlineBorder": 4,
        "outlineDistance": 4,
        "waveLength": 256,
        "textFontSize": 64,
        "textFill": "white",
    },
}

g2(options=options)
```
""")
