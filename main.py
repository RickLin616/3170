import os
import streamlit as st
from streamlit_option_menu import option_menu as om
from web.pagelib.log_page import *
from web.pagelib.consumer.shopping_cart_page import *
from web.pagelib.consumer.preview_page import *
from web.pagelib.consumer.custormer_order_page import *
from web.utils.session_control import *
from web.utils.bgsetting import *

#current path
path = os.path.dirname(__file__)

#initialize session state
if "function" not in st.session_state:
    st.session_state["function"] = "log" # RANGE in {log, staff, consumer}
if "log_check" not in st.session_state:
    st.session_state["log_check"] = False
if "role" not in st.session_state:
    st.session_state["role"] = "staff"
#three functions
if st.session_state["function"] == "log":
    selected = om("CHIPANDA COOPERATION", 
                    ["LOG IN", 
                    'SIGN UP'], 
                menu_icon =  "chip_fill",
                icons=['house', 'text-indent-right'], 
                orientation='horizontal',
                default_index=0)
    if selected == "LOG IN":
        log_in_page()
    elif selected =="SIGN UP":
        sign_up_page()

elif st.session_state["function"] == "consumer":
    with st.sidebar:
        st.image("web\images\pandas_chip_2.png")
        selected_c = om("CEND-INTERFACE", 
                        ["Introduction", 
                         "Shopping Cart",
                         "Current Order"], 
                    menu_icon =  "None",
                    icons=['house', 'ui-checks','columns','text-indent-right','ui-radios-grid','heptagon-half','eye-fill'], 
                    default_index=0)
        st.sidebar.info(
                """
            Welcome to chipandas! Contact us with +86 17767361813.  
            Copyright © 2022 CHIPANDAS Corporation
                """
        )
    if selected_c == "Introduction":
        preview_page()
    elif selected_c == "Shopping Cart":
        shopping_cart_page()
    elif selected_c == "Current Order":
        custormer_order_page(user_id=1)
    st.button("Log out", on_click=move_to_log_state)

elif st.session_state["function"] == "staff":
    with st.sidebar:
        st.image("web\images\pandas_chip_1.png")
        selected_b = om("BEND-INTERFACE", 
                        ["Introduction", 
                        "Page1",
                        "Page2"], 
                    menu_icon =  "None",
                    icons=['house', 'ui-checks','columns','text-indent-right','ui-radios-grid','heptagon-half','eye-fill'], 
                    default_index=0)
    st.sidebar.info(
            """
        Welcome to chipandas! Contact us with +86 17767361813.  
        Copyright © 2022 CHIPANDAS Corporation
            """
    )
    if selected_b == "Introduction":
        preview_page()
    st.button("Log out", on_click=move_to_log_state)