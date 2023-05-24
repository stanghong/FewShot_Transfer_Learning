# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
# %%
def create_mask(image):
    # Create a mask for the whole image area
    height, width, _ = image.shape
    mask = np.ones((height, width), dtype=np.uint8) * 255
    return mask

def plot_histograms(image1, image2):
    images = [image1, image2]
    num_images = len(images)
    fig, ax = plt.subplots(figsize=(8, 6))

    colors = ['g', 'b']  # List of colors for different histograms
    labels = ['Image 1', 'Image 2']  # List of labels for the legend

    for i, image in enumerate(images):
        greenmask = create_mask(image)
        hist_mask_values = cv2.calcHist([image], channels=[1], mask=greenmask, histSize=[256], ranges=[0, 256])
        
        ax.plot(hist_mask_values, color=colors[i], label=labels[i])  # Plot each histogram with different color and label
    
    ax.set_title('Histogram Comparison of Multiple Images')
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')
    ax.legend()  # Display the legend

    plt.tight_layout()

    # Save the histogram plot as an image
    plt.savefig("histograms.png")
    plt.close()

    # Return the histogram plot image
    return "histograms.png"

# %%
# Create the Gradio interface
iface = gr.Interface(fn=plot_histograms,
                     inputs=[
                         gr.inputs.Image(source="upload", label="Image 1"),
                         gr.inputs.Image(source="upload", label="Image 2"),
                        #  gr.inputs.Image(source="upload", label="Image 3")
                     ],
                     outputs="image",
                     title="Multiple Image Histograms",
                     description="Plot the histograms of multiple images.",
                     allow_flagging=False)

iface.launch()

# %%
