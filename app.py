import streamlit as st
st.set_page_config(layout="wide")

import requests
import json
from streamlit_ace import st_ace

hide_footer_style = """
<style>
[class^="embeddedAppMetaInfoBar_container"] {
    display: none !important;
    visibility: hidden !important;
}
header {
    display: none !important;
}
section > div.block-container {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}
h1,
h2,
h3,
h4,
h5,
h6,
p,
span,
@import url("https://fonts.googleapis.com/css2?family=Roboto&family=Roboto+Mono&display=swap");
div {
  font-family: 'Roboto Mono', monospace;
  font-weight: 500;
}
[data-baseweb="slider"] {
    padding-left: 10px !important;
}
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
.modebar{
      display: none !important;
}
</style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)

mode = st.query_params.get("mode", ["uk"])[0]

if mode == "uk":
    with st.expander("Compute current-law taxes and benefits", expanded=True):
        default_situation = {
            "household": {
                "people": {
                    "parent": {
                        "age": {2023: 35},
                        "employment_income": {2023: 30_000},
                    },
                    "child": {
                        "age": {2023: 10},
                    },
                },
                "households": {
                    "household": {
                        "members": ["parent", "child"],
                        "household_net_income": {2023: None},
                        "household_benefits": {2023: None},
                        "household_tax": {2023: None},
                    },
                },
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Python snippet"]
        )
        with data_input:
            st.caption("Describe people and households")
            situation = st_ace(
                language="json5",
                theme="github",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://household.api.policyengine.org/uk/calculate_demo",
                json=json.loads(situation),
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://household.api.policyengine.org/uk/calculate_demo", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)

    with st.expander("Compute impacts of reforms"):
        default_situation = {
            "household": {
                "people": {
                    "parent": {
                        "age": {2023: 35},
                        "employment_income": {2023: 30_000},
                    },
                    "child": {
                        "age": {2023: 10},
                    },
                },
                "households": {
                    "household": {
                        "members": ["parent", "child"],
                        "household_net_income": {2023: None},
                        "household_benefits": {2023: None},
                        "household_tax": {2023: None},
                    },
                },
            },
            "policy": {
                "gov.hmrc.income_tax.rates.uk[0].rate": {
                    "2023-01-01.2024-01-01": 0.25,
                }
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Python snippet"]
        )
        with data_input:
            st.caption("Describe people, households and reforms")
            situation = st_ace(
                language="json",
                theme="github",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://household.api.policyengine.org/uk/calculate_demo",
                json=json.loads(situation),
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://household.api.policyengine.org/uk/calculate_demo", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)


if mode == "us":
    with st.expander("Compute current-law taxes and benefits", expanded=True):
        default_situation = {
            "people": {
                "parent": {
                    "age": {2023: 35},
                    "employment_income": {2023: 30_000},
                },
                "child": {
                    "age": {2023: 10},
                },
            },
            "households": {
                "household": {
                    "members": ["parent", "child"],
                    "household_net_income": {2023: None},
                    "household_benefits": {2023: None},
                    "household_tax": {2023: None},
                },
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Code snippet"]
        )
        with data_input:
            st.caption("Describe people and households")
            situation = st_ace(
                language="json",
                theme="github",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://household.api.policyengine.org/us/calculate_demo",
                json={
                    "household": json.loads(situation),
                },
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://household.api.policyengine.org/us/calculate_demo", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)

    with st.expander("Compute impacts of reforms"):
        default_situation = {
            "household": {
                "people": {
                    "parent": {
                        "age": {2023: 35},
                        "employment_income": {2023: 30_000},
                    },
                    "child": {
                        "age": {2023: 10},
                    },
                },
                "households": {
                    "household": {
                        "members": ["parent", "child"],
                        "household_net_income": {2023: None},
                        "household_benefits": {2023: None},
                        "household_tax": {2023: None},
                    },
                },
            },
            "policy": {
                "gov.usda.snap.income.deductions.earned_income": {
                    "2023-01-01.2024-01-01": 0.25,
                }
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Code snippet"]
        )
        with data_input:
            st.caption("Describe people, households and reforms")
            situation = st_ace(
                language="json",
                theme="github",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://household.api.policyengine.org/us/calculate_demo",
                json=json.loads(situation),
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://household.api.policyengine.org/us/calculate_demo", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)
