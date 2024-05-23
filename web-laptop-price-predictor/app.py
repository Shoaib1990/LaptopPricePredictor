import streamlit as st
import pickle
import numpy as np


# import model
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        model_data = pickle.load(file)
    return model_data


data = load_model()

rf_model = data["model"]
manufacturer_encoder = data["manufacturer_encoder"]
cpu_encoder = data["cpu_encoder"]
gpu_encoder = data["gpu_encoder"]
os_encoder = data["os_encoder"]

# {"model": rf, "manufacturer_encoder": manufacturer_encoder, "cpu_encoder": cpu_encoder, "gpu_encoder": gpu_encoder, "os_encoder": os_encoder}

# pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# brand
brand = st.radio('Brand', df['manufacturer'].unique())

ram = st.radio('Ram (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 40, 48, 64])

touchscreen = st.radio('Touchscreen', ['No', 'Yes'])

ips = st.radio('IPS', ['No', 'Yes'])

# screen size
# [13.5, 15. , 15.6, 16. , 14.4, 17.3, 14. , 13.4, 17. , 11.6, 13.6, 14.2, 15.3, 16.2, 13.3, 12.3, 10.5]
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.radio('Screen Resolution',
                      ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                       '2560x1440', '2304x1440'])

cpu = st.radio('CPU', df['cpu_name'].unique())

memory = st.radio('Storage(in GB)', [32, 64, 128, 256, 512, 1024, 2048, 3072])

num_processors = st.radio('Num of Processors', [1, 2, 4, 6, 8, 12, 14, 16, 24])

gpu = st.radio('GPU', df['graphics_copressor'].unique())

os = st.radio('OS', df['os'].unique())

st.write('<style>.row-widget.stRadio > div{display: flex;flex-direction:row;}</style>', unsafe_allow_html=True)

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    # query = np.array([brand, ram, touchscreen, ips, ppi, cpu, memory, gpu, os])
    # query = query.reshape(1, 9)
    # st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

    X = np.array([[brand, ram, touchscreen, ips, ppi, cpu, memory, num_processors, gpu, os]])
    X[:, 0] = manufacturer_encoder.transform(X[:, 0])
    X[:, 5] = cpu_encoder.transform(X[:, 5])
    X[:, 8] = gpu_encoder.transform(X[:, 8])
    X[:, 9] = os_encoder.transform(X[:, 9])
    X = X.astype(float)

    price = np.exp(rf_model.predict(X))
    st.subheader(f"The estimated salary is ${price[0]:.2f}")
