# -*- coding: utf-8 -*-
"""My-Refined-Python-Code2CreateAmap

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SSwgbHEP5wS7Ime8RU6NcUmgscL5ZpBv

My refined Python code to create a map by Worachat Wannawong, Ph.D., incorporating best practices and addressing potential issues:
"""

import folium

# Define map center coordinates (New York City)
map_center = [40.7128, -74.0060]  # Corrected longitude for New York City

# Create a base map with zoom level 12
mymap = folium.Map(location=map_center, zoom_start=12)

# Create a marker for New York City with a blue info sign icon and a popup
marker = folium.Marker(
    location=map_center,
    popup="New York City",
    icon=folium.Icon(color="blue", prefix="fa", icon="info-sign")
)

# Add the marker to the map
marker.add_to(mymap)

# Display the map (no need for IPython.display since folium handles it)
mymap

"""Here's a breakdown of the improvements:

- **Clarity and Conciseness:** The code is well-formatted and uses clear variable names, making it easy to understand.
- **Corrected Longitude:** The `map_center` now has the correct longitude (-74.0060) for New York City.
- **Modern Icon Style:** The `icon` argument in `folium.Marker` uses the `prefix="fa"` and `icon="info-sign"` syntax for a more recent and widely supported FontAwesome icon style.
- **Direct Display:** The `display(mymap)` line is removed as folium handles displaying the map automatically.
- **Error Handling (Optional):** Consider adding a `try-except` block to gracefully handle potential errors during map creation:
"""

import folium

# Define map center coordinates (Matthayom Wat Nongkhaem School)
map_center = [13.676519, 100.3372947]  # Corrected longitude for Matthayom Wat Nongkhaem School

# Create a base map with zoom level 12
mymap = folium.Map(location=map_center, zoom_start=12)

# Create a marker for Matthayom Wat Nongkhaem School with a blue info sign icon and a popup
marker = folium.Marker(
    location=map_center,
    popup="New York City",
    icon=folium.Icon(color="blue", prefix="fa", icon="info-sign")
)

# Add the marker to the map
marker.add_to(mymap)

# Display the map (no need for IPython.display since folium handles it)
mymap

"""Remember to install the `folium` library before running the code:

```bash
pip install folium
```

This refined code effectively creates a map centered on New York City and Matthayom Wat Nongkhaem School, Thailand with a blue info sign marker and a popup, providing a clear and visually appealing representation. URL: https://www.google.com/maps/place/โรงเรียนมัธยมวัดหนองแขม/@13.676519,100.3372947,839m/data=!3m1!1e3!4m14!1m7!3m6!1s0x30e2be0d6edb02a1:0xca5208e559090800!2z4LmC4Lij4LiH4LmA4Lij4Li14Lii4LiZ4Lih4Lix4LiY4Lii4Lih4Lin4Lix4LiU4Lir4LiZ4Lit4LiH4LmB4LiC4Lih!8m2!3d13.676519!4d100.3398696!16s%2Fg%2F1234td6l!3m5!1s0x30e2be0d6edb02a1:0xca5208e559090800!8m2!3d13.676519!4d100.3398696!16s%2Fg%2F1234td6l?entry=ttu
"""