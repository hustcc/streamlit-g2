import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="Ring", page_icon="📈", layout="wide")


"""
## Ring Chart
"""

options = {
  "autoFit": True,
  "type": "interval",
  "data": {
    "value": [
      { "name": "G", "star": 814 },
      { "name": "G2", "star": 11425 },
      { "name": "G2Plot", "star": 2320 },
      { "name": "S2", "star": 968 },
      { "name": "F2", "star": 7346 },
      { "name": "L7", "star": 2888 },
      { "name": "G6", "star": 9314 },
      { "name": "X6", "star": 3985 },
      { "name": "AVA", "star": 1151 }
    ],
    "transform": [
      {
        "type": "sortBy",
        "fields": [
          [ "star", True ]
        ]
      }
    ]
  },
  "encode": {
    "x": "name",
    "y": "star",
    "color": "name",
    "size": 40
  },
  "scale": {
    "y": {
      "type": "sqrt"
    }
  },
  "coordinate": {
    "type": "radial",
    "endAngle": 3.141592653589793
  },
  "style": {
    "radius": 20
  },
  "animate": {
    "enter": {
      "type": "waveIn",
      "duration": 1000
    }
  },
  "axis": {
    "x": {
      "title": False
    },
    "y": False
  },
  "labels": [
    {
      "text": "star",
      "position": "outside",
      "autoRotate": True,
      "rotateToAlignArc": True,
      "dx": 4
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
  "data": {
    "value": [
      { "name": "G", "star": 814 },
      { "name": "G2", "star": 11425 },
      { "name": "G2Plot", "star": 2320 },
      { "name": "S2", "star": 968 },
      { "name": "F2", "star": 7346 },
      { "name": "L7", "star": 2888 },
      { "name": "G6", "star": 9314 },
      { "name": "X6", "star": 3985 },
      { "name": "AVA", "star": 1151 }
    ],
    "transform": [
      {
        "type": "sortBy",
        "fields": [
          [ "star", True ]
        ]
      }
    ]
  },
  "encode": {
    "x": "name",
    "y": "star",
    "color": "name",
    "size": 40
  },
  "scale": {
    "y": {
      "type": "sqrt"
    }
  },
  "coordinate": {
    "type": "radial",
    "endAngle": 3.141592653589793
  },
  "style": {
    "radius": 20
  },
  "animate": {
    "enter": {
      "type": "waveIn",
      "duration": 1000
    }
  },
  "axis": {
    "x": {
      "title": False
    },
    "y": False
  },
  "labels": [
    {
      "text": "star",
      "position": "outside",
      "autoRotate": True,
      "rotateToAlignArc": True,
      "dx": 4
    }
  ]
}

g2(options=options)
```
""")
