from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "divider")

app.layout = DocsBlock(
    component_name="Divider",
    children=[
        ComponentDescription(
            "Horizontal line with optional label or vertical divider."
        ),
        Heading("Simple Example", id="simple-example"),
        Text(
            "The simplest divider is basically an html.Hr component. dmc.Divider can be customized by providing a "
            "`label`, setting the label's `position` and changing its size or style or color. "
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("With Label", id="label"),
        Text("You can provide `label` and `labelPosition` to customize dmc.Divider."),
        CodeBlock(__file__, "label.py", app),
        Heading("Different Sizes", id="sizes"),
        Text("Set the `size` property to change the size of the divider."),
        CodeBlock(__file__, "sizes.py", app),
        Heading("Vertical Divider", id="vertical"),
        Text(
            """Divider can be used in vertical orientations as well by setting `orientation="vertical"` and providing 
            it some height."""
        ),
        CodeBlock(__file__, "vertical.py", app),
        Heading("With Color", id="color"),
        Text("Set Divider color from one of the colors of Mantine default theme."),
        CodeBlock(__file__, "colors.py", app),
    ],
)