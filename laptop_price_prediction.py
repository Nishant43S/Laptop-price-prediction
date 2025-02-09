from sklearn.model_selection import train_test_split  ### importing libraries
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBRegressor
import pickle
import numpy as np
import streamlit as st

## page setting
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)

#### app functions

### insert external css
@st.cache_data
def insert_css(css_file:str):
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

insert_css("css_files/settings.css")


#### load Models

with open("models/rf_model.pkl","rb") as model:
    RF_model = pickle.load(model)

with open("models/xgb_model.pkl","rb") as model:
    XGB_model = pickle.load(model)

standard_scaller = pickle.load(open("models/Standard_scaller.pkl","rb"))

## creating app side bar
app_sidebar = st.sidebar

with app_sidebar:
    st.title("")
    st.title("")

    model_select = st.selectbox(
        label="Select Modal",
        options=["Random Forest","XGBoost"],
        index=0,key="Model selector"
    )


### model select 

def ML_model(model,specification):

    laptop_specs = standard_scaller.transform([specification])
    try:

        if model == "Random Forest":
            rf_prediction = RF_model.predict(laptop_specs)[0]
            return np.round(rf_prediction,2)
        
        elif model == "XGBoost":
            xgb_prediction = XGB_model.predict(laptop_specs)[0]
            return np.round(xgb_prediction)
    except Exception as er:
        st.warning("Error {}".format(er),icon="⚠️")

### random data
random_laptop = [
    2,    # Company (e.g., Asus)
    1,    # TypeName (e.g., Gaming)
    15.6, # Inches
    16,   # Ram (GB)
    2.3,  # Weight (kg)
    1920, # ScreenW (Resolution Width)
    1080, # ScreenH (Resolution Height)
    5,    # OS (e.g., Windows 10)
    1,    # Touchscreen (1 = Yes, 0 = No)
    1,    # IPSpanel (1 = Yes, 0 = No)
    0,    # RetinaDisplay (1 = Yes, 0 = No)
    1,    # CPU_company (e.g., Intel)
    4,    # CPU_model (e.g., Intel Core i7)
    2.8,  # CPU_freq (GHz)
    512,  # PrimaryStorage (GB)
    0,    # PrimaryStorageType (e.g., SSD)
    1024, # SecondaryStorage (GB)
    1,    # SecondaryStorageType (e.g., HDD)
    2,    # GPU_company (e.g., NVIDIA)
    3,    # GPU_model (e.g., GTX 1650)
    15  # Battery Life (Assuming a numerical value, replace if different)
]


###################  features  ###############
from features import LaptopFeatures  ### importing categorial features

laptop_features = LaptopFeatures()


### main app
Laptop_prediction_col = st.columns([2,8,2],gap="small")

### blank columns
with Laptop_prediction_col[0]:
    pass
with Laptop_prediction_col[2]:
    pass

### main app column
with Laptop_prediction_col[1]:
  ### app heading
    st.subheader("Laptop Price Prediction")

    ### laptop features
    features_col = st.columns([4,4],gap="small")

    with features_col[0]:
        ## company name
        Company_name = st.selectbox(
            label="Company",
            options=list(laptop_features.Company_Name()),
            key="company name"
        )

        ## type
        Type_name = st.selectbox(
            label="Type",
            options=list(laptop_features.get_device_type()),
            index=1,
            key="type name"
        )

        ## screen size
        Inch_size = st.selectbox(
            label="Inches",
            options=[13.3, 15.6, 15.4, 14.0 , 12.0 , 11.6, 
                     17.3, 10.1, 13.5, 12.5, 13.0 ,18.4, 13.9, 
                     12.3, 17.0 , 15.0 , 14.1, 11.3],
            key="inch name"
        )

        ## screen width
        Screen_width = st.selectbox(
            label="Screen Width",
            options=[2560, 1440, 1920, 2880, 1366,
                    2304, 3200, 2256, 3840, 2160, 1600, 2736, 2400],
            key="width screen"
        )

        ## screen width
        Screen_height = st.selectbox(
            label="Screen Height",
            options=[1600,  900, 1080, 1800,  768, 1440, 1200, 1504, 2160, 1824],
            key="height screen"
        )

        ##  Cpu_company
        Cpu_company = st.selectbox(
            label="Cpu company",
            options=['Intel', 'AMD', 'Samsung'],
            key="Cpu_company"
        )

        ##  Cpu_model
        Cpu_model = st.selectbox(
            label="Cpu Model",
            options=list(laptop_features.CPU_Model_Name()),
            key="Cou model"
        )

        ##  primarary storage
        primarary_storage = st.selectbox(
            label="Primarary Storage",
            options=[ 128,  256,  512,  500, 1024,
                    32,  64, 2048,   16,  180,  240,
                    8,  508],
            key="P storage"
        )

        ##  primarary storage type
        primarary_storage_type = st.selectbox(
            label="Primarary Storage Type",
            options=list(laptop_features.PrimararyStorageType_Name()),
            key="P storage name",index=1
        )

        
        ##  gpu model
        Gpu_model = st.selectbox(
            label="GPU Model",
            options=list(laptop_features.GPU_Model_Name()),
            key="gpu model",index=0
        )

        Battery_life = st.slider(
            label="Battery Life",
            key="battery life",
            min_value=1,
            max_value=29,value=9
        )


    with features_col[1]:
         ### ram size
        Ram_size = st.selectbox(
            label="Ram",
            options=[ 8, 16,  4,  2, 12,  6, 32, 24, 64],
            key="ram name"
        )
        
        ### weight 
        laptop_weight = st.slider(
            label="Weight",
            min_value=0.69,
            max_value=5.0,
            value=1.7,
            key="Weight"
        )

         ### os
        Os_name = st.selectbox(
            label="Operating System",
            options=list(laptop_features.get_os()),
            key="os name"
        )
         ### touch screen
        Touch_screen_display = st.selectbox(
            label="Touch Screen",
            options=["Yes","No"],
            key="touch screen"
        )
        
         ### ips panel
        Ips_panel= st.selectbox(
            label="IPS Display",
            options=["Yes","No"],
            key="ips"
        )
        
         ### ips panel
        Retina_Display= st.selectbox(
            label="Retina Display",
            options=["Yes","No"],
            key="RetinaDisplay"
        )
        
         ### cpu frequency
        Cpu_Frequency= st.selectbox(
            label="CPU Frequency",
            options=[2.3 , 1.8 , 2.5 , 2.7 , 3.1 , 3.0  , 2.2 , 1.6 , 2.0  , 2.8 , 1.2 ,
             2.9 , 2.4 , 1.44, 1.5 , 1.9 , 1.1 , 1.3 , 2.6 , 3.6 , 3.2 , 1.0  ,
             2.1 , 0.9 , 1.92],
            key="cpu freq"
        )

        
        ##  Secondary storage
        Secondary_storage = st.selectbox(
            label="Secondary Storage",
            options=[   0, 1024,  256, 2048,  500,  512],
            key="S storage"
        )

        ##  primarary storage type
        Secondary_storage_type = st.selectbox(
            label="Secondary Storage Type",
            options=list(laptop_features.SecondaryStorageType_Name()),
            key="S storage name",index=1
        )

        ##  gpu company
        Gpu_company = st.selectbox(
            label="GPU Company",
            options=list(laptop_features.GPUCompany_Name()),
            key="gpu company",index=0
        )

    # predict button
    Predict_btn = st.button(
        label="Predict Price",
        key="btn prediction"
    )

    
    laptop_features_input = [
        laptop_features.Company_Name_Index(Company_name),    # Company (e.g., Asus)
        laptop_features.get_device_type_index(Type_name),    # TypeName (e.g., Gaming)
        Inch_size, # Inches
        Ram_size,   # Ram (GB)
        laptop_weight,  # Weight (kg)
        Screen_width, # ScreenW (Resolution Width)
        Screen_height, # ScreenH (Resolution Height)
        laptop_features.get_os_index(os_name=Os_name),    # OS (e.g., Windows 10)
        laptop_features.Touch_Screen(Touch_screen_display),    # Touchscreen (1 = Yes, 0 = No)
        laptop_features.IPS_panel(Ips_panel),    # IPSpanel (1 = Yes, 0 = No)
        laptop_features.Retina_Display(Retina_Display),    # RetinaDisplay (1 = Yes, 0 = No)
        laptop_features.CPU_Company(Cpu_company),    # CPU_company (e.g., Intel)
        laptop_features.get_cpu_model_index(Cpu_model),    # CPU_model (e.g., Intel Core i7)
        Cpu_Frequency,  # CPU_freq (GHz)
        primarary_storage,  # PrimaryStorage (GB)
        laptop_features.PrimararyStorageType_Index(primarary_storage_type),    # PrimaryStorageType (e.g., SSD)
        Secondary_storage, # SecondaryStorage (GB)
        laptop_features.SecondaryStorageType_Index(Secondary_storage_type),    # SecondaryStorageType (e.g., HDD)
        laptop_features.GPUCompany_Index(Gpu_company),    # GPU_company (e.g., NVIDIA)
        laptop_features.GPU_Model_Index(Gpu_model),    # GPU_model (e.g., GTX 1650)
        Battery_life  # Battery Life (Assuming a numerical value, replace if different)
    ]

    Laptop_Model = {
        "Company":Company_name,
        "Type":Type_name,
        "Inches":Inch_size,
        "RAM":Ram_size,
        "Laptop Weight":laptop_weight,
        "Screen Width":Screen_width,
        "Screen Height":Screen_height,
        "Operating System":Os_name,
        "Touch Screen":Touch_screen_display,
        "Ips Panel":Ips_panel,
        "Ratina Display":Retina_Display,
        "CPU Company":Cpu_company,
        "CPU Model":Cpu_model,
        "CPU Frequency":Cpu_Frequency,
        "Primarary Storage":primarary_storage,
        "Primarary Storage Type":primarary_storage_type,
        "Secondary Storage":Secondary_storage,
        "Primarary Storage Type":Secondary_storage_type,
        "GPU Company":Gpu_company,
        "GPU Model":Gpu_model,
        "Battery Life":Battery_life
    }
   
    if Predict_btn:
        with st.spinner("Predicting..."):
            for Feature_name, feature in Laptop_Model.items():
                st.write(f"- {Feature_name} :: {feature}")
            predicted_value = ML_model(model=model_select,specification=laptop_features_input)
            st.subheader(f"Model - {model_select}")
            st.subheader(f"Predicted price - {predicted_value} €")

          