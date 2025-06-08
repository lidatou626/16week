import streamlit as st
import sys

# Python 版本检查
if sys.version_info >= (3, 13):
    st.error("⚠️ 当前 Python 版本为 3.13+，可能与 fastai 不兼容。建议使用 Python 3.11。")
    st.stop()

from fastai.vision.all import *
import pathlib

#载入模型#只读一边，缓存在此
st.cache_resource
def load_model():
    model path = pathlib.Path(__file__).parent /""
    return load_learner(model_path)

#上传文件


#如果不是空的，
if uploaded_file is not None:
    img = PILImage.create(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    st.write(f"预测")