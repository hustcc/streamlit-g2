import pandas as pd

# Loop to process dataFrame to data dict.
def normalize_options(options):
  if isinstance(options, dict):
    for k, v in options.items():
      if k == "data" and isinstance(v, pd.DataFrame):
        options["data"] = v.to_dict(orient='records')
      else:
        normalize_options(v)
  elif isinstance(options, list):
    for v in options:
      normalize_options(v)
