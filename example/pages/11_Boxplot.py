import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Boxplot", page_icon="📈", layout="wide")


"""
## Boxplot
"""

options = {
    "autoFit": True,
    "type": "boxplot",
    "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": {
        "type": "fetch",
        "value": "https://assets.antv.antgroup.com/g2/penguins.json"
    },
    "encode": {
        "x": "species",
        "y": "flipper_length_mm",
        "color": "sex",
        "series": "sex",
    }
}

g2(options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": {
        "type": "fetch",
        "value": "https://assets.antv.antgroup.com/g2/penguins.json"
    },
    "encode": {
        "x": "species",
        "y": "flipper_length_mm",
        "color": "sex",
        "series": "sex",
    }
}

g2(options=options)
```
""")
