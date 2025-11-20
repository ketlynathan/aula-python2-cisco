from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import Sessionmaker, declarative_base, Session
from datetime import datetime

# Modelo ORM


class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    data_hora = Column(DateTime, nullable=False)
