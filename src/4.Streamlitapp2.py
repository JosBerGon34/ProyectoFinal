import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la base de datos y la tabla (si no existen)
engine = create_engine('sqlite:///./src/tablausuario.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'ClusterUsuario'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    Salario_Bruto_Anual = Column(Integer)
    # Agrega más columnas según tus necesidades

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear el formulario de Streamlit
with st.form("ClusterUsuario"):
    name = st.text_input("Nombre")
    age = st.number_input("Edad")
    Salario_Bruto_Anual = st.number_input("SalarioBrutoAnual")
    # ... otros campos
    submitted = st.form_submit_button("Enviar")

# Si se envía el formulario, insertar los datos
if submitted:
    with SessionLocal() as db:
        new_user = User(name=name, age=age, Salario_Bruto_Anual=Salario_Bruto_Anual,)
        db.add(new_user)
        db.commit()
        st.success("Datos guardados correctamente")
        
#Modelo base sin terminar.