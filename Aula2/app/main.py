from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, E,ailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import re

app = FastAPI(title="Sistema de Padronização de Nomes e Emails")
# Configuração do banco de dado SQLITE
SQLALCHEMY_DATABASE_URL = "sqlite:///./USUARIOS.db"
engine = create_engine(SQLALCHEMY_DATABASE_URl)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo SQLAlchemy para o banco de dados
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Função para padronizar nome
def padronizar_nome(nome: str) -> str:
    # Remove espaços extras e converte para lowercase
    nome = " ".join(nome.split()).lower()

    # Capitaliza cada palavra
    nome = nome.title()

    # Tratamento para nome com 'da', 'de', 'do', 'das', 'dos'
    preposicoes = ['Da', 'De', 'Do', 'Das', 'Dos']
    palavras = nome.split()
    nome_final = []
    
    for palavra in palavras:
        if palavra in preposicoes:
            nome_final.append(palavra.lower())
        else:
            nome_final.append(palavra)

    return " ".join(nome_final)

# Função para padronizar email
def padronizar_email(email: str) -> str:
    # remove acentos
    from unicodedata import normalize
    nome = normalize('NFKD', email).encode('ASCII', 'ignore').decode('ASCII')