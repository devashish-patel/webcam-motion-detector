from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)
# Create a figure
p = figure(x_axis_type='datetime', title="Motion graph", background_fill_color="#EFE8E2",sizing_mode='scale_width', height=100, width=470)
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start",'@Start_String'), ("End",'@End_String')])
p.add_tools(hover)

p.quad(left='Start', right='End', bottom=0, top=1, fill_color="#3B8686", source=cds)

# Save it to file
output_file("Chart.html")
show(p)