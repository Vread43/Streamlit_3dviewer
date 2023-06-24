import streamlit as st
import pythreejs as p3
import ipywidgets as widgets
from io import BytesIO

# Set up the Streamlit app layout
st.title("3D File Viewer")
st.subheader("Open and View 3D Files")

# Check if a file is uploaded
if st.button("Upload 3D File"):
    uploaded_file = st.file_uploader("Upload a 3D file:", type=["obj", "stl", "ply"], accept_multiple_files=False, key="file_uploader")
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.success("File uploaded successfully!")

        # Load the 3D file
        try:
            geometry = p3.Geometry.from_file(uploaded_file.name, BytesIO(file_contents))
        except Exception as e:
            st.error(f"Error loading the 3D file: {e}")
        else:
            # Create a 3D view
            view_width = 800
            view_height = 600
            renderer = p3.Renderer(width=view_width, height=view_height)
            scene = p3.Scene(children=[p3.Mesh(geometry=geometry)])
            controller = p3.OrbitControls(controlling=scene.camera)
            renderer.camera = scene.camera
            renderer.controls = [controller]
            renderer.layout.height = f"{view_height}px"
            renderer.layout.width = f"{view_width}px"

            # Create an IPyWidget container to display the 3D view
            container = widgets.HBox([renderer])

            # Display the 3D view
            st.subheader("3D View")
            st.write(container)

# Display information about the 3D file viewer
st.subheader("About the 3D File Viewer")
st.write("The 3D file viewer in this tool allows you to upload and view 3D files in formats such as OBJ, STL, or PLY. After uploading a valid 3D file, a 3D view will be displayed where you can rotate, pan, and zoom to explore the object.")
