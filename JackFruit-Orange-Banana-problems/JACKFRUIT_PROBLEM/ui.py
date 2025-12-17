from pil_conversion import *
from PIL import Image
import streamlit as st
from streamlit_cropper import st_cropper

st.title("Jackfruit Problem : Image Processing")

# Sidebar for controls
st.sidebar.header("Controls")

# File uploader in sidebar
uploaded_img = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Initialize session state
if 'cropped_img' not in st.session_state:
    st.session_state.cropped_img = None
if 'show_cropper' not in st.session_state:
    st.session_state.show_cropper = False

# Main content area
if uploaded_img is not None:
    original_img = Image.open(uploaded_img)
    
    # Sidebar controls
    st.sidebar.subheader("Crop Settings")
    
    # Toggle cropper view
    if st.sidebar.button("Enable Crop Mode" if not st.session_state.show_cropper else "Disable Crop Mode"):
        st.session_state.show_cropper = not st.session_state.show_cropper
        if not st.session_state.show_cropper:
            st.session_state.cropped_img = None
    
    # Cropper interface
    if st.session_state.show_cropper:
        st.subheader("Draw ROI to Crop")
        
        # Cropper settings in sidebar
        
        box_color = st.sidebar.color_picker("Box Color", "#0000FF")
        
        
        # Display cropper
        cropped_img = st_cropper(
            original_img,
            realtime_update=True,
            box_color=box_color,
            aspect_ratio=None
        )
        
        # Save crop button
        if st.button("Save Cropped Image"):
            st.session_state.cropped_img = cropped_img
            st.session_state.show_cropper = False
            st.success("Image cropped and saved!")
            st.rerun()
    
    else:
        # Clear crop button
        if st.session_state.cropped_img is not None:
            if st.sidebar.button("Clear Crop"):
                st.session_state.cropped_img = None
                st.rerun()
        
        # Transformation dropdown
        st.sidebar.subheader("Transformation")
        transformation = st.sidebar.selectbox(
            "Select Transformation",
            ["None", "Grayscale", "Blur", "Sharpen", "Edge Detection", 
             "Flip Horizontal", "Flip Vertical", "Rotate 90°", "Rotate 180°", 
             "Brightness Increase", "Brightness Decrease", "Contrast Increase", 
             "Contrast Decrease", "Invert", "Emboss"]
        )
        
        # Determine which image to process
        img_to_process = st.session_state.cropped_img if st.session_state.cropped_img is not None else original_img
        img_mode = get_image_mode(img_to_process)
        
        if img_mode in ["RGB", "RGBA"]:
            img_to_process = img_to_process.convert("RGB")
            
            # Apply transformation if selected
            if transformation != "None":
                img_for_analysis = apply_transformation(img_to_process, transformation)
                analysis_source = f"Transformed Image ({transformation})"
            else:
                img_for_analysis = img_to_process
                if st.session_state.cropped_img is not None:
                    analysis_source = "Cropped Image"
                else:
                    analysis_source = "Original Image"
            
            # Create columns for images
            if st.session_state.cropped_img is not None and transformation != "None":
                col1, col2, col3 = st.columns(3)
            elif st.session_state.cropped_img is not None or transformation != "None":
                col1, col2 = st.columns(2)
            else:
                col1 = st.columns(1)[0]
            
            with col1:
                st.subheader("Original Image")
                st.image(original_img, width='stretch')
            
            if st.session_state.cropped_img is not None:
                with col2:
                    st.subheader("Cropped Image")
                    st.image(st.session_state.cropped_img, width='stretch')
            
            if transformation != "None":
                with (col3 if st.session_state.cropped_img is not None else col2):
                    st.subheader(f"Transformed: {transformation}")
                    st.image(img_for_analysis, width='stretch')
            
            # Calculate metrics on the final processed image
            st.subheader(f"Image Analysis - {analysis_source}")
            
            dom_secondary_color = dom_secondarycolor(img_for_analysis)
            dom_primary = dom_primarycolor(img_for_analysis)
            
            # Create color swatch for dominant secondary color
            import ast
            try:
                rgb_tuple = ast.literal_eval(dom_secondary_color)
                color_swatch = create_color_swatch(rgb_tuple)
            except:
                color_swatch = None
            
            # Display table and color swatch side by side
            table_col, swatch_col = st.columns([3, 1])
            
            with table_col:
                table_data = [
                    {"Metric": "Red Pixel Count", "Value": str(red_pixel_count(img_for_analysis))},
                    {"Metric": "Dominant Primary Color", "Value": str(dom_primary)},
                    {"Metric": "Dominant Secondary Color", "Value": str(dom_secondary_color)},
                ]
                st.table(table_data)
            
            with swatch_col:
                if color_swatch is not None:
                    st.write("**Dominant Color Swatch:**")
                    st.image(color_swatch, width='stretch')
        
        else:
            st.warning('Please upload an image in RGB/RGBA', icon="⚠️")

else:
    st.info("👈 Please upload an image from the sidebar to get started!")