from numpy import *
from math import *
import streamlit as st
import plotly.express as px   

with st.sidebar:
    st.header("National University of Civil Engineering")
    st.subheader("Academic Department of Geothecnical Engineering")
    st.write("EC514G - Soils Dynamic")

st.title("Transferences Functions")

tab1, tab2 = st.tabs(["Elastic Soil", "Rigid     Soil"])
with tab1:
    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: "$V_{s1} (m/s)$"
    with r2: Vs11 = st.number_input("Vs11", value = 145.0,min_value=0.1, label_visibility="collapsed")
    with r3: "$V_{s2} (m/s)$"
    with r4: Vs21 = st.number_input("Vs21", value = 700.0,min_value=0.1, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: f"$\\rho_1 (kg/m^3)$"
    with r2: rho11 = st.number_input("rho11", value = 1650.0, min_value=0.1, label_visibility="collapsed")
    with r3: f"$\\rho_2 (kg/m^3)$"
    with r4: rho21 = st.number_input("rho21", value = 1800.0, min_value=0.1, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: f"$\\xi_1$ (%)"
    with r2: xi11 = st.number_input("xi11", value = 4.5, min_value=0.1, label_visibility="collapsed")
    with r3: f"$\\xi_2$ (%)"
    with r4: xi21 = st.number_input("xi21", value = 2.5, min_value=0.1, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: "$H (m)$"
    with r2: H1 = st.number_input("H1", value = 25.0, min_value=0.1, label_visibility="collapsed")

# Procedimiento para la gráfica de la funcion de transferencia:
    f1 = arange(0, 30, 0.01, dtype=float)
    w1 = []
    F1 = []

    for i in range(len(f1)):
        w1.append(2*pi*f1[i])
    
    alpha = (rho11*Vs11*(1+(xi11/100)**2)**2)/(rho21*Vs21*(1+(xi21/100)**2)**2)
    for i in range(len(f1)):
        a = sin(w1[i]*H1/Vs11)**2 + sinh((xi11/100)*w1[i]*H1/Vs11)**2
        b = cos(w1[i]*H1/Vs11)**2 + sinh((xi11/100)*w1[i]*H1/Vs11)**2
        F1.append(1/sqrt(alpha*a + b))
    
    fig1 = px.line(x = f1, y = F1, labels = {'x':'Frequency (Hz)', 'y':'F1(ω)'}, range_x=[0,30])
    st.plotly_chart(fig1, use_container_width = True)

with tab2:
    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: "$V_{s1} (m/s)$"
    with r2: Vs12 = st.number_input("Vs12", value = 145.0, min_value=0.1, label_visibility="collapsed")
    with r3: "$V_{s2} (m/s)$"
    with r4: Vs22 = st.number_input("Vs22", value = 700.0, min_value=0.1, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: f"$\\rho_1 (kg/m^3)$"
    with r2: rho12 = st.number_input("rho12", value = 1650.0,min_value=0.1, label_visibility="collapsed")
    with r3: f"$\\rho_2 (kg/m^3)$"
    with r4: rho22 = st.number_input("rho22", value = 1800.0,min_value=0.1, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: f"$\\xi_1$ (%)"
    with r2: xi12 = st.number_input("xi12", value = 4.5, min_value=0.1, label_visibility="collapsed")
    with r3: f"$\\xi_2$ (%)"
    with r4: xi22 = st.number_input("xi22", value = 2.5, min_value=0.1, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: "$H (m)$"
    with r2: H2 = st.number_input("H2", value = 25.0, min_value=0.1, label_visibility="collapsed")

# Procedimiento para la gráfica de la funcion de transferencia:
    f2 = arange(0, 30, 0.01, dtype=float)
    w2 = []
    F2 = []

    for i in range(len(f2)):
        w2.append(2*pi*f2[i])
    
    alpha = (rho12*Vs12*(1+(xi12/100)**2)**2)/(rho22*Vs22*(1+(xi22/100)**2)**2)
    for i in range(len(f2)):
        F2.append(1/sqrt(cos(w2[i]*H2/Vs12)**2 + sinh((xi12/100)*w2[i]*H2/Vs12)**2))
    
    fig2 = px.line(x = f2, y = F2, labels = {'x':'Frequency (Hz)', 'y':'F2(ω)'}, range_x=[0,30])
    st.plotly_chart(fig2, use_container_width = True)
