import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Area", page_icon="📈", layout="wide")


"""
## Area Chart
"""

options = {
    "autoFit": True,
    "type": "area",
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/bmw-prod/551d80c6-a6be-4f3c-a82a-abd739e12977.csv",
    },
    "encode": {
        "x": "date",
        "y": "close",
    },
}

g2(options=options)

st.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "type": "area",
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/bmw-prod/551d80c6-a6be-4f3c-a82a-abd739e12977.csv",
    },
    "encode": {
        "x": "date",
        "y": "close",
    },
}

g2(options=options)
```
""")
