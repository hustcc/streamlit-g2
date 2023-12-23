import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Funnel", page_icon="📈", layout="wide")


"""
## Funnel Chart
"""

options = {
    "autoFit": True,
    "type": "interval",
    "data": [
        { "action": "浏览网站", "pv": 50000 },
        { "action": "放入购物车", "pv": 35000 },
        { "action": "生成订单", "pv": 25000 },
        { "action": "支付订单", "pv": 15000 },
        { "action": "完成交易", "pv": 8000 }
    ],
    "encode": {
        "x": "action",
        "y": "pv",
        "color": "action",
        "shape": "funnel"
    },
    "transform": [
        {
        "type": "symmetryY"
        }
    ],
    "scale": {
        "x": { "padding": 0 }
    },
    "coordinate": {
        "transform": [
        { "type": "transpose" }
        ]
    },
    "animate": {
        "enter": {
        "type": "fadeIn"
        }
    },
    "axis": False,
    "labels": [
        {
            "text": "pv",
            "position": "inside",
            "transform": [
                {
                "type": "contrastReverse"
                }
            ]
        }
    ]
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
    "data": [
        { "action": "浏览网站", "pv": 50000 },
        { "action": "放入购物车", "pv": 35000 },
        { "action": "生成订单", "pv": 25000 },
        { "action": "支付订单", "pv": 15000 },
        { "action": "完成交易", "pv": 8000 }
    ],
    "encode": {
        "x": "action",
        "y": "pv",
        "color": "action",
        "shape": "funnel"
    },
    "transform": [
        {
        "type": "symmetryY"
        }
    ],
    "scale": {
        "x": { "padding": 0 }
    },
    "coordinate": {
        "transform": [
        { "type": "transpose" }
        ]
    },
    "animate": {
        "enter": {
        "type": "fadeIn"
        }
    },
    "axis": False,
    "labels": [
        {
            "text": "pv",
            "position": "inside",
            "transform": [
                {
                "type": "contrastReverse"
                }
            ]
        }
    ]
}

g2(options=options)
```
""")
