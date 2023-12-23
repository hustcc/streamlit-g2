import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Histogram", page_icon="📈", layout="wide")


"""
## Histogram
"""

options = {
    "autoFit": True,
    "type": "rect",
    "data": {
        "type": "fetch",
        "value": "https://assets.antv.antgroup.com/g2/athletes.json"
    },
    "encode": {
        "x": "weight",
        "color": "sex"
    },
    "transform": [
        {
        "type": "binX",
        "y": "count"
        },
        {
        "type": "stackY",
        "orderBy": "series"
        }
    ],
    "style": {
        "inset": 0.5
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
    "type": "rect",
    "data": {
        "type": "fetch",
        "value": "https://assets.antv.antgroup.com/g2/athletes.json"
    },
    "encode": {
        "x": "weight",
        "color": "sex"
    },
    "transform": [
        {
        "type": "binX",
        "y": "count"
        },
        {
        "type": "stackY",
        "orderBy": "series"
        }
    ],
    "style": {
        "inset": 0.5
    }
}

g2(options=options)
```
""")
