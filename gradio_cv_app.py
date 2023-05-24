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

# def plot_histograms(image1, image2, image3):
#     images = [image1, image2, image3]
#     num_images = len(images)
#     fig, axes = plt.subplots(num_images, 1, figsize=(6, 4*num_images))
    
#     for i, image in enumerate(images):
#         greenmask = create_mask(image)
#         hist_mask_values = cv2.calcHist([image], channels=[1], mask=greenmask, histSize=[256], ranges=[0, 256])
        
#         axes[i].plot(hist_mask_values, 'g')
#         axes[i].set_title('Histogram - Image {}'.format(i+1))
#         axes[i].set_xlabel('Pixel Value')
#         axes[i].set_ylabel('Frequency')
    
#     plt.tight_layout()

#     # Save the combined histogram plot as an image
#     plt.savefig("histograms.png")
#     plt.close()

#     # Return the combined histogram plot image
#     return "histograms.png"
def plot_histograms(image1, image2):
    images = [image1, image2]
    num_images = len(images)
    fig, ax = plt.subplots(figsize=(8, 6))

    for image in images:
        greenmask = create_mask(image)
        hist_mask_values = cv2.calcHist([image], channels=[1], mask=greenmask, histSize=[256], ranges=[0, 256])
        
        ax.plot(hist_mask_values, 'g')
    
    ax.set_title('Histogram Comparison of Multiple Images')
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')

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
