# Enhancing Geospatial Learning with Folium

This project demonstrates how to create an interactive map using the Folium library in Python. The map centers on New York City and Thai School in Bangkok, Thailand, and includes a marker with a popup.

## Installation

To run this project, you need to have Python and Folium installed on your machine. You can install Folium using pip:

```bash
pip install folium
```

## Usage

To generate the map, you can use the following Python code:

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
---

```python
import folium

# Define map center coordinates (Thai School)
map_center = [13.676519, 100.3372947]  # Corrected longitude for Thai School

# Create a base map with zoom level 12
mymap = folium.Map(location=map_center, zoom_start=12)

# Create a marker for Thai School with a blue info sign icon and a popup
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

This project focuses on creating an interactive map centered on New York City and Thai School. The map includes:

- A base map centered at the coordinates of the New York City and Thai School.
- A marker at the school's location with a blue info sign icon.
- A popup displaying "New York City and Thai School" when the marker is clicked.

## Running the Project

To run the project, save the provided code in a Python script or Jupyter Notebook and execute it. The map will be generated and displayed in your default web browser.

## Notes

- Ensure the coordinates for the map center and marker are correct.
- Customize the popup text and marker icon as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Screenshots

![Burger Bar Cafe website](./image.png)

## Contact

For any inquiries or issues, please contact me!

## Author

- **Worachat W, Dev.** - *Data Science, Engineering & Full Stack Dev. 2024*  
  [LinkedIn](https://www.linkedin.com/in/brainwaves-your-ai-playground-82155961/) | [GitHub](https://github.com/worachat-dev) | [Facebook](https://web.facebook.com/NutriCious.Thailand)


---

**Additional Notes:**

- Consider adding error handling (try-except block) to gracefully handle potential issues.
- Folium offers extensive capabilities for customizing the map, adding different layers, and creating interactive features. Explore the library's documentation for further customization: [https://github.com/python-visualization/folium](https://github.com/python-visualization/folium)

