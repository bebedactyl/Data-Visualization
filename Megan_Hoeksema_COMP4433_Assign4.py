# Using free and open source tools, provide a set of choropleth visualizations for each of the columns containing
# dates such that the resulting visualizations (48 states only) tell the story by conveying through color, texture,
# or both the time lines of achievement of each milestone/column in the provided dataset. Missing data are of
# particular interest in that when a state has never achieved a given milestone, that should be indicated in a
# standout manner such as cross-hatching. Consider that the publication may be grayscale. Provide a solution for that
# as well. Provide the titles, labels, and legends necessary for clarification. File support is given as follows:
# SturmCodebook has the explanation. SturmData is the data CSV.

import geopandas as gpd
import geoplot
