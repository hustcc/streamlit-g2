import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Scatter", page_icon="📈", layout="wide")


"""
## Scatter Chart
"""

options = {
    "autoFit": True,
    "type": "point",
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/basement_prod/6b4aa721-b039-49b9-99d8-540b3f87d339.json",
    },
    "encode": {
        "x": "height",
        "y": "weight",
        "color": "gender",
        "shape": "point"
    },
}

g2(options=options)

st.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "type": "point",
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/basement_prod/6b4aa721-b039-49b9-99d8-540b3f87d339.json",
    },
    "encode": {
        "x": "height",
        "y": "weight",
        "color": "gender",
        "shape": "point"
    },
}

g2(options=options)
```
""")
