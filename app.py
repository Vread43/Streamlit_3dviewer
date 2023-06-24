import streamlit as st
import pyvista as pv
from pyvista.plotting.renderer import Renderer

# Set up the Streamlit app layout
st.title("3D File Viewer")
st.subheader("Open and View 3D Files")

# Check if a file is uploaded
if st.button("Upload 3D File"):
    uploaded_file = st.file_uploader("Upload a 3D file:", type=["obj", "stl", "ply"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.success("File uploaded successfully!")

        # Load the 3D file
        try:
            mesh = pv.read_buffer(file_contents, file_format=uploaded_file.name.split(".")[-1])
        except Exception as e:
            st.error(f"Error loading the 3D file: {e}")
        else:
            # Create a PyVista plotter and add the mesh
            plotter = pv.Plotter(window_size=(800, 600), off_screen=True)
            plotter.add_mesh(mesh)

            # Set up plotter settings
            plotter.enable_eye_dome_lighting()
            plotter.background_color = "white"

            # Render the scene and capture a screenshot
            plotter.show()
            screenshot = plotter.screenshot()

            # Display the 3D view
            st.subheader("3D View")
            st.image(screenshot, caption="3D View")

# Display information about the 3D file viewer
st.subheader("About the 3D File Viewer")
st.write("The 3D file viewer in this tool allows you to upload and view 3D files in formats such as OBJ, STL, or PLY. After uploading a valid 3D file, a 3D view will be displayed where you can rotate, pan, and zoom to explore the object.")
