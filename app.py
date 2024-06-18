import mode
import utils
import pandas as pd

metric = {
      "name": "<metric-name>",
      "transform": [
        { "$eq": ["<COLUMN>", "<expression>"] },
        { "$neq": ["<COLUMN>", "<expression>"] },
        { "$gt": ["<COLUMN>", "<expression>"] },
        { "$gte": ["<COLUMN>", "<expression>"] },
        { "$lt": ["<COLUMN>", "<expression>"] },
        { "$lte": ["<COLUMN>", "<expression>"] },
        { "$btw": ["<COLUMN>", "<limit1>", "<limit2>"] },
        { "$in": ["<COLUMN>", ["expression1", "expression2", "expressionN"]] }
      ],
      "response": {
        "getTotalRecords": True,
        "type": {
          "name": ["MODE","MEAN","AVG","MEDIAN","COUNT","SUM"],
          "params": ["ENG_SPEED", "DEF_LEVEL","ENG_COOLANT_TEMP","IDLE_REASON"]

        }
      }
    }
df = pd.read_excel('new_df.xlsx')
print(utils.pick(df,metric))