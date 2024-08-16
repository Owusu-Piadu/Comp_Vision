import streamlit as st

# Setting Up Title
st.title('Brain MRI tumor detection')

# Setting Header
st.header('Please upload an image')

# Upload File
file = st.file_uploader('', type=['png', 'jpg', 'jpeg'])

# Load Model
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file('COCO-Detection/retinanet_R_101_FPN_3x.yaml'))
cfg.MODEL.WEIGHTS = './model/model.pth'
cfg.MODEL.DEVICE = 'cpu'

# Load Image

# Detect Objects

# Visualize