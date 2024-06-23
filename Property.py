class CssPropertyManager:
    def __init__(self, table):
        self.table = table
    
    def add_css_property(self):
        self.table.add_row("color", ["black","#000","white","#FFFFFF","rgb(255, 255, 255)","hsl(0, 0%, 100%)","red","hsl(0, 100%, 50%)","green","hsl(120, 100%, 50%)","blue","hsl(240, 100%, 50%)"])
        self.table.add_row("background-color", ["transparent","initial","white","#FFFFFF","rgb(255, 255, 255)","hsl(0, 0%, 100%)","black","#000"])
        self.table.add_row("font-family", ["Arial", "Times New Roman"])
        self.table.add_row("font-size", ["10",["px","%","em","rem","cm"]])
        self.table.add_row("font-weight", [
            "normal",
            "bold",
            "bolder",
            "lighter",
            "100",
            "200",
            "300",
            "400",
            "500",
            "600",
            "700",
            "800",
            "900"
        ])
        self.table.add_row("text-align", [
            "left",
            "right",
            "center",
            "justify"
        ])
        self.table.add_row("margin", [["margin-top", ["10",["px","%","em","rem","cm"]]], ["margin-right", ["10",["px","%","em","rem","cm"]]], ["margin-bottom", ["10",["px","%","em","rem","cm"]]], ["margin-left", ["10",["px","%","em","rem","cm"]]]])
        self.table.add_row("padding", [["padding-top", ["10",["px","%","em","rem","cm"]]], ["padding-right", ["10",["px","%","em","rem","cm"]]], ["padding-bottom", ["10",["px","%","em","rem","cm"]]], ["padding-left", ["10",["px","%","em","rem","cm"]]]])
        self.table.add_row("border", [["thickness","1px"],["style",["solid","double","groove","ridge","inset","outset"]],["color",["black","white"]]])
        self.table.add_row("width",  ["10",["px","%","em","rem","cm","initial"]])
        self.table.add_row("height",  ["10",["px","%","em","rem","cm","auto"]])
        self.table.add_row("min-width",  ["",["none","px","%","em","rem","cm"]])
        self.table.add_row("min-height",  ["",["none","px","%","em","rem","cm"]])
        self.table.add_row("max-width",  ["",["none","px","%","em","rem","cm"]])
        self.table.add_row("max-height",  ["",["none","px","%","em","rem","cm"]])
        self.table.add_row("line-height",  ["",["normal","px","%","em","rem","cm"]])
        self.table.add_row("font-style", [
            "normal",
            "italic",
            "oblique"
        ])
        self.table.add_row("text-decoration", [
            "none",
            "underline",
            "overline",
            "line-through"
        ])
        self.table.add_row("display", ["block", "inline", "inline-block"])
        self.table.add_row("overflow", [
            "visible",
            "hidden",
            "scroll",
            "auto"
        ])
        
        self.table.add_row("list-style-type", [
            "none",
            "disc",
            "circle",
            "square",
            "decimal",
            "lower-alpha",
            "upper-alpha"
            
        ])
        
        
        
        self.table.add_row("cursor", [
            "auto",
            "pointer",
            "default",
            "wait",
            "text",
            "move",
            "not-allowed",
            "crosshair",
            "help"
        ])
        self.table.add_row("z-index", [
            "auto",
            "10",
            "20",
            "30",
            "40",
            "50"
        ])
        self.table.add_row("flex",[["flex-grow", [
            "1",
            "2",
            "3",
            "4",
            "initial",
            "inherit"
        ]],["flex-shrink", [
            "1",
            "2",
            "3",
            "4",
            "initial",
            "inherit"
        ]],["flex-basis", [
            "auto",
            "1",
            "2",
            "3",
            "4",
            "initial",
            "inherit"
        ]]])
        self.table.add_row("display", [
            "block",
            "inline",
            "inline-block",
            "flex",
            "grid",
            "table",
            "none"
        ])
        
        self.table.add_row("text-transform", [
            "none",
            "uppercase",
            "lowercase",
            "capitalize"
        ])
        
        self.table.add_row("white-space", [
            "normal",
            "nowrap",
            "pre",
            "pre-wrap",
            "pre-line"
        ])
        
        self.table.add_row("border-style", [
            "solid",
            "dashed",
            "dotted",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "none",
            "hidden"
        ])
        
        self.table.add_row("position", [
            "static",
            "relative",
            "absolute",
            "fixed",
            "sticky"
        ])
        
        self.table.add_row("float", [
            "left",
            "right",
            "none"
        ])
        
        self.table.add_row("clear", [
            "none",
            "left",
            "right",
            "both"
        ])
        
        self.table.add_row("visibility", [
            "visible",
            "hidden",
            "collapse"
        ])
        
        
        
        self.table.add_row("opacity", [
            "1.0",
            "0.75",
            "0.5",
            "0.25",
            "0.0"
        ])
        
        self.table.add_row("background-repeat", [
            "repeat",
            "repeat-x",
            "repeat-y",
            "no-repeat"
        ])
        
        self.table.add_row("background-size", [
            "auto",
            "cover",
            "contain"
        ])
        
        self.table.add_row("border-width", ["",[
            "thin",
            "medium",
            "thick",
            "px",
            "%",
            "em",
            "rem",
            "cm",
            "initial"
        ]])
        
        self.table.add_row("box-shadow", [
            "none",
            "0px 4px 2px -2px gray",
            "inset 0 0 10px #000000"
        ])
        

        
        
        
        
        
        self.table.add_row("height", [
            "auto",
            "value",
            "initial",
            "inherit"
        ])

        

        
        self.table.add_row("vertical-align", [
            "baseline",
            "sub",
            "super",
            "top",
            "text-top",
            "middle",
            "bottom",
            "text-bottom"
        ])
        
        
        self.table.add_row("align-content", [
            "center",
            "flex-start",
            "flex-end",
            "space-between",
            "space-around",
            "stretch"
        ])
        
        self.table.add_row("align-items", [
            "stretch",
            "flex-start",
            "flex-end",
            "center",
            "baseline"
        ])
        
        self.table.add_row("align-self", [
            "auto",
            "flex-start",
            "flex-end",
            "center",
            "baseline",
            "stretch"
        ])
        
        self.table.add_row("flex-direction", [
            "row",
            "row-reverse",
            "column",
            "column-reverse"
        ])
        
        self.table.add_row("flex-wrap", [
            "nowrap",
            "wrap",
            "wrap-reverse"
        ])
        
        self.table.add_row("justify-content", [
            "flex-start",
            "flex-end",
            "center",
            "space-between",
            "space-around",
            "space-evenly"
        ])
        
        self.table.add_row("order", [
            "1",
            "2",
            "3",
            "initial",
            "inherit"
        ])
        
        
        
        self.table.add_row("grid-template-columns", [
            "none",
            "value"
        ])
        
        self.table.add_row("grid-template-rows", [
            "none",
            "value"
        ])
        
        self.table.add_row("grid-template-areas", [
            "none",
            "value"
        ])
        
        self.table.add_row("grid-column", [
            "auto",
            "span 10",
            "span 20",
            "start / end"
        ])
        
        self.table.add_row("grid-row", [
            "auto",
            "span 10",
            "span 20",
            "start / end"
        ])
        
        self.table.add_row("grid-auto-columns", [
            "auto",
            "10",
            "20",
        ])
        
        self.table.add_row("grid-auto-rows", [
            "auto",
            "10",
            "20",
        ])
        
        self.table.add_row("grid-auto-flow", [
            "row",
            "column",
            "dense",
            "row dense",
            "column dense"
        ])
        
    
    

