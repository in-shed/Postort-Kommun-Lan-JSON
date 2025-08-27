import pandas as pd
import json

df = pd.read_csv("Postort-Kommun-Lan.csv")

flat_list = df.to_dict(orient="records")

by_postort = df.set_index("Postort").to_dict(orient="index")

hierarchical = {}
for _, row in df.iterrows():
    lan = row["LnNamn"]
    kommun = row["KnNamn"]
    postort = row["Postort"]

    hierarchical.setdefault(lan, {}).setdefault(
        kommun,
        {
            "KnKod": row["KnKod"],
            "LnKod": row["LnKod"],
            "LnBokstav": row["LnBokstav"],
            "Postorter": [],
        },
    )
    hierarchical[lan][kommun]["Postorter"].append(postort)

with open("postort-kommun-lan-flat.json", "w", encoding="utf-8") as f:
    json.dump(flat_list, f, ensure_ascii=False, indent=2)

with open("postort-kommun-lan-by-postort.json", "w", encoding="utf-8") as f:
    json.dump(by_postort, f, ensure_ascii=False, indent=2)

with open("postort-kommun-lan-hierarchical.json", "w", encoding="utf-8") as f:
    json.dump(hierarchical, f, ensure_ascii=False, indent=2)
    