import streamlit as st
from streamlit_g2 import g2

st.set_page_config(page_title="streamlit-g2: AntV G2 for Streamlit!")

"""
# Welcome to [streamlit-g2](https://github.com/hustcc/streamlit-g2)!

[G2](https://github.com/antvis/G2) is a visualization grammar for dashboard building, data exploration and storytelling.

This project was created to allow us to render [G2](https://github.com/antvis/G2) charts in streamlit. In the meantime, below are some examples of what you can do with just a few lines of code:
"""

"""
----
## Bar Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
    "type": "interval",
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
    }
}

g2(options=options)

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
    "type": "interval",
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
    }
}

g2(options=options)
```
"""

"""
----
## Column Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
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
    }
}

g2(options=options)

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
    }
}

g2(options=options)
```
"""


"""
----
## Line Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
    "type": "line",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
    "type": "line",
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
"""


"""
----
## Area Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
"""


"""
----
## Pie Chart
"""

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

"""
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
"""



"""
----
## DualAxes Chart
"""

options = {
  "type": "view",
  "theme": "dark",
  "autoFit": True,
  "data": [
    {
      "Month": "Jan",
      "Evaporation": 2,
      "Precipitation": 2.6,
      "Temperature": 2
    },
    {
      "Month": "Feb",
      "Evaporation": 4.9,
      "Precipitation": 5.9,
      "Temperature": 2.2
    },
    {
      "Month": "Mar",
      "Evaporation": 7,
      "Precipitation": 9,
      "Temperature": 3.3
    },
    {
      "Month": "Apr",
      "Evaporation": 23.2,
      "Precipitation": 26.4,
      "Temperature": 4.5
    },
    {
      "Month": "May",
      "Evaporation": 25.6,
      "Precipitation": 28.7,
      "Temperature": 6.3
    },
    {
      "Month": "Jun",
      "Evaporation": 76.7,
      "Precipitation": 70.7,
      "Temperature": 10.2
    },
    {
      "Month": "Jul",
      "Evaporation": 135.6,
      "Precipitation": 175.6,
      "Temperature": 20.3
    },
    {
      "Month": "Aug",
      "Evaporation": 162.2,
      "Precipitation": 182.2,
      "Temperature": 23.4
    },
    {
      "Month": "Sep",
      "Evaporation": 32.6,
      "Precipitation": 48.7,
      "Temperature": 23
    },
    {
      "Month": "Oct",
      "Evaporation": 20,
      "Precipitation": 18.8,
      "Temperature": 16.5
    },
    {
      "Month": "Nov",
      "Evaporation": 6.4,
      "Precipitation": 6,
      "Temperature": 12
    },
    {
      "Month": "Dec",
      "Evaporation": 3.3,
      "Precipitation": 2.3,
      "Temperature": 6.2
    }
  ],
  "children": [
    {
      "type": "line",
      "encode": {
        "x": "Month",
        "y": "Temperature",
        "color": "#EE6666",
        "shape": "smooth"
      },
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 30
        }
      },
      "axis": {
        "y": {
          "title": "Temperature (°C)",
          "grid": None,
          "titleFill": "#EE6666"
        }
      }
    },
    {
      "type": "interval",
      "encode": {
        "x": "Month",
        "y": "Evaporation",
        "color": "#5470C6"
      },
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 200
        }
      },
      "style": {
        "fillOpacity": 0.8
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Evaporation (ml)",
          "titleFill": "#5470C6"
        }
      }
    },
    {
      "type": "line",
      "encode": {
        "x": "Month",
        "y": "Precipitation",
        "color": "#91CC75"
      },
      "scale": {
        "y": {
          "independent": True
        }
      },
      "style": {
        "lineWidth": 2,
        "lineDash": [
          2,
          2
        ]
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Precipitation (ml)",
          "grid": None,
          "titleFill": "#91CC75"
        }
      }
    }
  ]
}

g2(options=options)

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
  "type": "view",
  "theme": "dark",
  "autoFit": True,
  "data": [
    {
      "Month": "Jan",
      "Evaporation": 2,
      "Precipitation": 2.6,
      "Temperature": 2
    },
    {
      "Month": "Feb",
      "Evaporation": 4.9,
      "Precipitation": 5.9,
      "Temperature": 2.2
    },
    {
      "Month": "Mar",
      "Evaporation": 7,
      "Precipitation": 9,
      "Temperature": 3.3
    },
    {
      "Month": "Apr",
      "Evaporation": 23.2,
      "Precipitation": 26.4,
      "Temperature": 4.5
    },
    {
      "Month": "May",
      "Evaporation": 25.6,
      "Precipitation": 28.7,
      "Temperature": 6.3
    },
    {
      "Month": "Jun",
      "Evaporation": 76.7,
      "Precipitation": 70.7,
      "Temperature": 10.2
    },
    {
      "Month": "Jul",
      "Evaporation": 135.6,
      "Precipitation": 175.6,
      "Temperature": 20.3
    },
    {
      "Month": "Aug",
      "Evaporation": 162.2,
      "Precipitation": 182.2,
      "Temperature": 23.4
    },
    {
      "Month": "Sep",
      "Evaporation": 32.6,
      "Precipitation": 48.7,
      "Temperature": 23
    },
    {
      "Month": "Oct",
      "Evaporation": 20,
      "Precipitation": 18.8,
      "Temperature": 16.5
    },
    {
      "Month": "Nov",
      "Evaporation": 6.4,
      "Precipitation": 6,
      "Temperature": 12
    },
    {
      "Month": "Dec",
      "Evaporation": 3.3,
      "Precipitation": 2.3,
      "Temperature": 6.2
    }
  ],
  "children": [
    {
      "type": "line",
      "encode": {
        "x": "Month",
        "y": "Temperature",
        "color": "#EE6666",
        "shape": "smooth"
      },
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 30
        }
      },
      "axis": {
        "y": {
          "title": "Temperature (°C)",
          "grid": None,
          "titleFill": "#EE6666"
        }
      }
    },
    {
      "type": "interval",
      "encode": {
        "x": "Month",
        "y": "Evaporation",
        "color": "#5470C6"
      },
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 200
        }
      },
      "style": {
        "fillOpacity": 0.8
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Evaporation (ml)",
          "titleFill": "#5470C6"
        }
      }
    },
    {
      "type": "line",
      "encode": {
        "x": "Month",
        "y": "Precipitation",
        "color": "#91CC75"
      },
      "scale": {
        "y": {
          "independent": True
        }
      },
      "style": {
        "lineWidth": 2,
        "lineDash": [
          2,
          2
        ]
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Precipitation (ml)",
          "grid": None,
          "titleFill": "#91CC75"
        }
      }
    }
  ]
}

g2(options=options)
```
"""


"""
----
## Scatter Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
"""



"""
----
## Liquid Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
"""



"""
----
## Ring Chart
"""

options = {
  "autoFit": True,
  "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
  "autoFit": True,
  "theme": "dark",
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
"""


"""
----
## Boxplot
"""

options = {
    "autoFit": True,
    "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
```
"""



"""
----
## Funnel Chart
"""

options = {
    "autoFit": True,
    "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
"""



"""
----
## Histogram
"""

options = {
    "autoFit": True,
    "theme": "dark",
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

"""
```py
import streamlit as st
from streamlit_g2 import g2

options = {
    "autoFit": True,
    "theme": "dark",
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
"""
