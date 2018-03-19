from motion_detector import df
from bokeh.plotting import figure, output_file, show


# Create a figure
p = figure(x_axis_type='datetime', title="Motion graph", background_fill_color="#EFE8E2",sizing_mode='scale_width', height=100, width=470)
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks=1

p.quad(left=df['Start'], right=df['End'], bottom=0, top=1, fill_color="#3B8686")

# Save it to file
output_file("Chart.html")
show(p)