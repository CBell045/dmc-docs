import dash_mantine_components as dmc
from dash.development.base_component import Component
from dash_mantine_react_table import DashMantineReactTable
from markdown2dash import Kwargs as KwargsBase

from lib.constants import PROPS_TO_EXCLUDE

mapping = {
    "; optional": "",
    "boolean | number | string | dict | list": "dict",
    "a value equal to: ": "",
    "a list of or a singular dash component, string or number": "any",
}


def format_kwargs(data):
    for row in data:
        for old, new in mapping.items():
            row["type"] = row.pop("type").replace(old, new)
        row["description"] = row["description"].replace("\n   ", "")

    return [row for row in data if row["name"] not in PROPS_TO_EXCLUDE]


class Kwargs(KwargsBase):
    # noinspection PyMethodMayBeStatic
    def hook(self, md, state):
        super().hook(md, state)

        sections = []

        for tok in state.tokens:
            if tok["type"] == self.block_name:
                sections.append(tok)

        for section in sections:
            kwargs = section["attrs"]["kwargs"]
            section["attrs"]["kwargs"] = format_kwargs(kwargs)
