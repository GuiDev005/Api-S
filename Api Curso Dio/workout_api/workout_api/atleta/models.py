from workout_api.contrib.models import BaseModel
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime




class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped [int] = mapped_column (Integer, primary_key = True)
    nome: Mapped [str] = mapped_column(String(50), nullable = False)
    cpf: Mapped [str] = mapped_column(String(11), unique = True, nullable = False)
    idade: Mapped [int] = mapped_column(Integer, nullable = False)
    peso: Mapped [float] = mapped_column(Float, nullable = False)
    altura: Mapped [float] = mapped_column(Float, nullable = False)
    sexo: Mapped [str] = mapped_column(String(1), nullable = False)
    created_at: Mapped [datetime] = mapped_column(DateTime, nullable = False)
    categoria: Mapped ['CategoriaModel'] = relationship(back_populates = 'atleta')
    categoria_id: Mapped [int] = mapped_column(ForeignKey('categorias.pk_id'))
    CentroDeTreinamento: Mapped ['CentroDeTreinamentoModel'] = relationship(back_populates = 'atleta')
    CentroDeTreinamento_id: Mapped [int] = mapped_column(ForeignKey('centros_de_treinamento.pk_id'))