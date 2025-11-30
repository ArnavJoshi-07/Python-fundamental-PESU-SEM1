from PIL import Image
import streamlit as st
import pandas as pd
import base64
from io import BytesIO

# Configuration for image sizes
each_color_size = (150, 20)
color_palette_size = (150, 60)

def create_color_swatch(rgb, size=each_color_size):
    """Creates a small image of a solid color."""
    return Image.new('RGB', size, rgb)

def pil_to_base64_data_url(img: Image.Image) -> str:
    """
    Converts a PIL Image object to a Base64 encoded Data URL string.
    This format is required for st.column_config.ImageColumn.
    """
    buffered = BytesIO()
    # Save the PIL image to the BytesIO buffer in PNG format
    img.save(buffered, format="PNG") 
    # Get the raw base64 string
    img_byte_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
    # Prepend the Data URL prefix
    return f"data:image/png;base64,{img_byte_string}"

# Define your colors and create the combined image
colors_rgb = [(8, 16, 27), (100, 0, 26), (123, 231, 91)]
combined_image_pil = Image.new('RGB', color_palette_size)
y_offset = 0
for color in colors_rgb:
    swatch = create_color_swatch(color)
    combined_image_pil.paste(swatch, (0, y_offset))
    y_offset += each_color_size[1]

# Display the combined image directly using st.image (for verification)
st.image(combined_image_pil, caption="Combined Image via st.image")

# Prepare the image for the table
image_data_url = pil_to_base64_data_url(combined_image_pil)

# Create a DataFrame
df = pd.DataFrame({
    "Palette Name": ["Custom Palette 1"],
    "Colors": [str(colors_rgb)], # Displaying the RGB values as a string
    "Image Display": [image_data_url] # This column holds the Data URL
})

# Display the DataFrame with the ImageColumn configuration
st.dataframe(
    df,
    column_config={
        "Image Display": st.column_config.ImageColumn(
            "Color Swatch", # Column header label
            help="The generated color palette image"
        )
    },
    hide_index=True
)