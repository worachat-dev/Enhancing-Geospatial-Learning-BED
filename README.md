Python code for creating a map:

## New York City Map with Folium

This project demonstrates a simple Python script using the `folium` library to create a map centered on New York City with a blue info sign marker and a popup.

**Running the code:**

1. **Install folium:** Open a terminal and run the command `pip install folium`.
2. **Create a Python file:** Save the following code in a Python file (e.g., `map.py`):

```python
import folium

# Define map center coordinates (New York City)
map_center = [40.7128, -74.0060]

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

# Display the map (folium handles it automatically)
mymap
```

3. **Run the script:** Execute the Python file using a command like `python map.py` in your terminal.

**Explanation:**

- The code imports the `folium` library.
- It defines the map center coordinates for New York City.
- It creates a base map object with the specified center and zoom level.
- It then defines a marker object with the same coordinates, a popup message, and a blue info sign icon.
- The marker is added to the map, and finally, the map is displayed.

**Additional Notes:**

- Consider adding error handling (try-except block) to gracefully handle potential issues.
- Folium offers extensive capabilities for customizing the map, adding different layers, and creating interactive features. Explore the library's documentation for further customization: [https://github.com/python-visualization/folium](https://github.com/python-visualization/folium)

