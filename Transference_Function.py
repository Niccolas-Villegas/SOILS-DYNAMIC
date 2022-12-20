from numpy import *
from math import *
import streamlit as st
import plotly.express as px

with st.sidebar:
    st.header("Universidad Nacional de Ingeniería")
    st.subheader("Facultad de Ingeniería Civil")
    st.subheader("Departamento Académico de Ingeniería Civil")
    st.write("EC514G - Dinámica de Suelos")

st.title("Funciones de Transferencia")

tab1, tab2, tab3 = st.tabs(["Marco Teórico","Suelo Elástico", "Suelo Rígido"])

with tab1:
    st.image('esfuerzo-deformacion.png')
    st.write(
        "La relación esfuerzo-deformación de Kelvin-Voight para un sólido en corte se expresa mediante el modelo mostrado en la figura. La resistencia total a la deformación por corte viene dada por la suma de un componente elástico (resorte) y un componente viscoso (amortiguador)."
    )
    st.latex(r'''
        \tau = G\gamma + \eta\frac{\partial \gamma}{\partial t}
    ''')
    st.write(
        "La ecuación de movimiento unidimensional para ondas SH que se propagan verticalmente se expresa como:"
    )
    st.latex(r'''
        \rho \frac{\partial^2 u}{\partial t^2} = G \frac{\partial^2 u}{\partial z^2} + \eta \frac{\partial^3 u}{\partial z^2 \partial t}
    ''')
    st.write(
        "Derivando la ecuación (1) y reemplazando la ecuación (2) considerando que $\sigma=\\tau$ ,$\\gamma=\\frac{\partial u}{\partial z}$, se obtiene lo siguiente:"
    )
    st.latex(r'''
        \tau = G\gamma + \eta\frac{\partial \gamma}{\partial t}
    ''')
    st.write(
        "Para funciones armónicas, los desplazamientos pueden ser escritos como:"
    )
    st.latex(r'''
        u(z,t) = U(z) e^{i \omega t}
    ''')
    st.write(
        "Sustituyendo en la ecuación anterior, obtenemos la siguiente ecuación diferencial ordinaria:"
    )
    st.latex(r'''
        -\rho \omega^2 U = (G + i \omega \eta) \frac{\partial^2 U}{\partial z^2}
    ''')
    st.write(
        "Donde $G^*=G + i\\omega\\eta$. La solución de la ecuación diferencial es la siguiente:"
    )
    st.latex(r'''
        u(z,t) = E e^{i(k^*z + \omega t)} + F e^{-i(k^*z - \omega t)}
    ''')
    st.write(
        "Donde:"
    )
    st.latex(r'''
        k^* = \omega \sqrt{\frac{\rho}{G^*}}
    ''')

with tab2:
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
    with r2: xi11 = st.number_input("xi11", value = 4.5, min_value=0.0, label_visibility="collapsed")
    with r3: f"$\\xi_2$ (%)"
    with r4: xi21 = st.number_input("xi21", value = 2.5, min_value=0.0, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: "$H (m)$"
    with r2: H1 = st.number_input("H1", value = 25.0, min_value=0.1, label_visibility="collapsed")
    with r3: "$limit$)"
    with r4: limit1 = st.number_input("limit1", value = 30.0, min_value=0.0, label_visibility="collapsed")

# Procedimiento para la gráfica de la funcion de transferencia:
    f1 = arange(0, limit1, 0.01, dtype=float)
    w1 = []
    F1 = []

    for i in range(len(f1)):
        w1.append(2*pi*f1[i])
    
    alpha = (rho11*Vs11*(1+(xi11/100)**2)**2)/(rho21*Vs21*(1+(xi21/100)**2)**2)
    for i in range(len(f1)):
        a = sin(w1[i]*H1/Vs11)**2 + sinh((xi11/100)*w1[i]*H1/Vs11)**2
        b = cos(w1[i]*H1/Vs11)**2 + sinh((xi11/100)*w1[i]*H1/Vs11)**2
        F1.append(1/sqrt(alpha*a + b))
    
    fig1 = px.line(x = f1, y = F1, labels = {'x':'Frequency (Hz)', 'y':'F1(ω)'}, range_x=[0,limit1])
    st.plotly_chart(fig1, use_container_width = True)

with tab3:
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
    with r2: xi12 = st.number_input("xi12", value = 4.5, min_value=0.0, label_visibility="collapsed")
    with r3: f"$\\xi_2$ (%)"
    with r4: xi22 = st.number_input("xi22", value = 2.5, min_value=0.0, label_visibility="collapsed")

    r1, r2, r3, r4 = st.columns([1,2,1,2], gap="medium")
    with r1: "$H (m)$"
    with r2: H2 = st.number_input("H2", value = 25.0, min_value=0.1, label_visibility="collapsed")
    with r3: "$limit$)"
    with r4: limit2 = st.number_input("limit2", value = 30.0, min_value=0.0, label_visibility="collapsed")

# Procedimiento para la gráfica de la funcion de transferencia:
    f2 = arange(0, limit2, 0.01, dtype=float)
    w2 = []
    F2 = []

    for i in range(len(f2)):
        w2.append(2*pi*f2[i])
    
    alpha = (rho12*Vs12*(1+(xi12/100)**2)**2)/(rho22*Vs22*(1+(xi22/100)**2)**2)
    for i in range(len(f2)):
        F2.append(1/sqrt(cos(w2[i]*H2/Vs12)**2 + sinh((xi12/100)*w2[i]*H2/Vs12)**2))
    
    fig2 = px.line(x = f2, y = F2, labels = {'x':'Frequency (Hz)', 'y':'F2(ω)'}, range_x=[0,limit2])
    st.plotly_chart(fig2, use_container_width = True)
