import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Column", page_icon="📈", layout="wide")


"""
## Column Chart
"""

options = {
    "autoFit": True,
    "type": "interval",
    "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "encode": {
        "x": "genre",
        "y": "sold",
        "color": "genre",
    },
    "scale": {
        "x": { "padding": 0.5 }
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
    "type": "interval",
    "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "encode": {
        "x": "genre",
        "y": "sold",
        "color": "genre",
    },
    "scale": {
        "x": { "padding": 0.5 }
    }
}

g2(options=options)
```
""")


"""
## Dodge Column Chart
"""

options = {
    "autoFit": True,
    "type": "interval",
    "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": [
        { "name": "London", "月份": "Jan.", "月均降雨量": 18.9 },
        { "name": "London", "月份": "Feb.", "月均降雨量": 28.8 },
        { "name": "London", "月份": "Mar.", "月均降雨量": 39.3 },
        { "name": "London", "月份": "Apr.", "月均降雨量": 81.4 },
        { "name": "London", "月份": "May", "月均降雨量": 47 },
        { "name": "London", "月份": "Jun.", "月均降雨量": 20.3 },
        { "name": "London", "月份": "Jul.", "月均降雨量": 24 },
        { "name": "London", "月份": "Aug.", "月均降雨量": 35.6 },
        { "name": "Berlin", "月份": "Jan.", "月均降雨量": 12.4 },
        { "name": "Berlin", "月份": "Feb.", "月均降雨量": 23.2 },
        { "name": "Berlin", "月份": "Mar.", "月均降雨量": 34.5 },
        { "name": "Berlin", "月份": "Apr.", "月均降雨量": 99.7 },
        { "name": "Berlin", "月份": "May", "月均降雨量": 52.6 },
        { "name": "Berlin", "月份": "Jun.", "月均降雨量": 35.5 },
        { "name": "Berlin", "月份": "Jul.", "月均降雨量": 37.4 },
        { "name": "Berlin", "月份": "Aug.", "月均降雨量": 42.4 },
    ],
    "encode": {
        "x": "月份",
        "y": "月均降雨量",
        "color": "name"
    },
    "transform": [{ "type": "dodgeX" }],
    "interaction": { "elementHighlight": { "background": True } },
}

g2(options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "type": "interval",
    "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": [
        { "name": "London", "月份": "Jan.", "月均降雨量": 18.9 },
        { "name": "London", "月份": "Feb.", "月均降雨量": 28.8 },
        { "name": "London", "月份": "Mar.", "月均降雨量": 39.3 },
        { "name": "London", "月份": "Apr.", "月均降雨量": 81.4 },
        { "name": "London", "月份": "May", "月均降雨量": 47 },
        { "name": "London", "月份": "Jun.", "月均降雨量": 20.3 },
        { "name": "London", "月份": "Jul.", "月均降雨量": 24 },
        { "name": "London", "月份": "Aug.", "月均降雨量": 35.6 },
        { "name": "Berlin", "月份": "Jan.", "月均降雨量": 12.4 },
        { "name": "Berlin", "月份": "Feb.", "月均降雨量": 23.2 },
        { "name": "Berlin", "月份": "Mar.", "月均降雨量": 34.5 },
        { "name": "Berlin", "月份": "Apr.", "月均降雨量": 99.7 },
        { "name": "Berlin", "月份": "May", "月均降雨量": 52.6 },
        { "name": "Berlin", "月份": "Jun.", "月均降雨量": 35.5 },
        { "name": "Berlin", "月份": "Jul.", "月均降雨量": 37.4 },
        { "name": "Berlin", "月份": "Aug.", "月均降雨量": 42.4 },
    ],
    "encode": {
        "x": "月份",
        "y": "月均降雨量",
        "color": "name"
    },
    "transform": [{ "type": "dodgeX" }],
    "interaction": { "elementHighlight": { "background": True } },
}

g2(options=options)
```
""")



"""
## Stack Column Chart
"""

options = {
    "autoFit": True,
    "type": "interval",
     "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": [
        { "name": "London", "月份": "Jan.", "月均降雨量": 18.9 },
        { "name": "London", "月份": "Feb.", "月均降雨量": 28.8 },
        { "name": "London", "月份": "Mar.", "月均降雨量": 39.3 },
        { "name": "London", "月份": "Apr.", "月均降雨量": 81.4 },
        { "name": "London", "月份": "May", "月均降雨量": 47 },
        { "name": "London", "月份": "Jun.", "月均降雨量": 20.3 },
        { "name": "London", "月份": "Jul.", "月均降雨量": 24 },
        { "name": "London", "月份": "Aug.", "月均降雨量": 35.6 },
        { "name": "Berlin", "月份": "Jan.", "月均降雨量": 12.4 },
        { "name": "Berlin", "月份": "Feb.", "月均降雨量": 23.2 },
        { "name": "Berlin", "月份": "Mar.", "月均降雨量": 34.5 },
        { "name": "Berlin", "月份": "Apr.", "月均降雨量": 99.7 },
        { "name": "Berlin", "月份": "May", "月均降雨量": 52.6 },
        { "name": "Berlin", "月份": "Jun.", "月均降雨量": 35.5 },
        { "name": "Berlin", "月份": "Jul.", "月均降雨量": 37.4 },
        { "name": "Berlin", "月份": "Aug.", "月均降雨量": 42.4 },
    ],
    "encode": {
        "x": "月份",
        "y": "月均降雨量",
        "color": "name"
    },
    "transform": [{ "type": "stackY" }],
    "scale": {
        "x": { "padding": 0.3 }
    },
    "interaction": { "elementHighlight": { "background": True } },
}

g2(options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "type": "interval",
     "coordinate": {
        "transform": [
            { "type": "transpose" }
        ]
    },
    "data": [
        { "name": "London", "月份": "Jan.", "月均降雨量": 18.9 },
        { "name": "London", "月份": "Feb.", "月均降雨量": 28.8 },
        { "name": "London", "月份": "Mar.", "月均降雨量": 39.3 },
        { "name": "London", "月份": "Apr.", "月均降雨量": 81.4 },
        { "name": "London", "月份": "May", "月均降雨量": 47 },
        { "name": "London", "月份": "Jun.", "月均降雨量": 20.3 },
        { "name": "London", "月份": "Jul.", "月均降雨量": 24 },
        { "name": "London", "月份": "Aug.", "月均降雨量": 35.6 },
        { "name": "Berlin", "月份": "Jan.", "月均降雨量": 12.4 },
        { "name": "Berlin", "月份": "Feb.", "月均降雨量": 23.2 },
        { "name": "Berlin", "月份": "Mar.", "月均降雨量": 34.5 },
        { "name": "Berlin", "月份": "Apr.", "月均降雨量": 99.7 },
        { "name": "Berlin", "月份": "May", "月均降雨量": 52.6 },
        { "name": "Berlin", "月份": "Jun.", "月均降雨量": 35.5 },
        { "name": "Berlin", "月份": "Jul.", "月均降雨量": 37.4 },
        { "name": "Berlin", "月份": "Aug.", "月均降雨量": 42.4 },
    ],
    "encode": {
        "x": "月份",
        "y": "月均降雨量",
        "color": "name"
    },
    "transform": [{ "type": "stackY" }],
    "scale": {
        "x": { "padding": 0.3 }
    },
    "interaction": { "elementHighlight": { "background": True } },
}

g2(options=options)
```
""")
