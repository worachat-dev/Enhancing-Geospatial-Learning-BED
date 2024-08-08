## Enhancing Geospatial Learning with Folium

# Folium Map Project

This project demonstrates how to create an interactive map using the Folium library in Python. The map centers on Matthayom Wat Nongkhaem School in Bangkok, Thailand, and includes a marker with a popup.

## Installation

To run this project, you need to have Python and Folium installed on your machine. You can install Folium using pip:

```bash
pip install folium
```

## Usage

To generate the map, you can use the following Python code:

```python
import folium

# Define map center coordinates (Matthayom Wat Nongkhaem School)
map_center = [13.676519, 100.3372947]  # Corrected longitude for Matthayom Wat Nongkhaem School

# Create a base map with zoom level 12
mymap = folium.Map(location=map_center, zoom_start=12)

# Create a marker for Matthayom Wat Nongkhaem School with a blue info sign icon and a popup
marker = folium.Marker(
    location=map_center,
    popup="Matthayom Wat Nongkhaem School",
    icon=folium.Icon(color="blue", prefix="fa", icon="info-sign")
)

# Add the marker to the map
marker.add_to(mymap)

# Display the map (no need for IPython.display since folium handles it)
mymap
```

## Description

This project focuses on creating an interactive map centered on Matthayom Wat Nongkhaem School. The map includes:

- A base map centered at the coordinates of the school.
- A marker at the school's location with a blue info sign icon.
- A popup displaying "Matthayom Wat Nongkhaem School" when the marker is clicked.

## Running the Project

To run the project, save the provided code in a Python script or Jupyter Notebook and execute it. The map will be generated and displayed in your default web browser.

## Notes

- Ensure the coordinates for the map center and marker are correct.
- Customize the popup text and marker icon as needed.

## License

This project is licensed under the MIT License.


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

