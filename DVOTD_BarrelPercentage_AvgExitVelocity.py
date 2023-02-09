# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:58:45 2023

@author: HuntS2
"""

import pandas as pd
import plotly_express as px 
import plotly.io as pio
pio.renderers.default = "browser"

df = pd.read_csv(r"C:\Users\Hunts2\OneDrive - AECOM\Documents\Data Science Projects\bbsavant20230209.csv")


fig = px.scatter(df,
                 x = "barrel_batted_rate",
                 y = "exit_velocity_avg",
                 hover_data = [" first_name", "last_name"],
                 color = "launch_angle_avg",
                 labels = {"barrel_batted_rate" : "Barrel Percentage", "exit_velocity_avg" : "Avg Exit Velocity", "launch_angle_avg" : "Avg Launch Angle"},
                 trendline = "ols", trendline_color_override = "black",
                 title = "MLB 2022 Season Barrel Percentage vs. Avg Exit Velocity")
fig.show()