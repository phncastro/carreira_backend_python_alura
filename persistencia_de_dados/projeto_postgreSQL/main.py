from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from persistencia_de_dados.projeto_postgreSQL import models
from persistencia_de_dados.projeto_postgreSQL import schemas
from persistencia_de_dados.projeto_postgreSQL.database import SessionLocal, engine

# Cria as tabelas no PostgreSQL(caso nao existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schemas.EstudanteResponse)
def create_studant(studant:schemas.EstudanteCreate, db:Session=Depends(get_db)):
    db_estudant = models.Estudante(**studant.model_dump())
    db.add(db_estudant)
    db.commit()
    db.refresh(db_estudant)
    return db_estudant

@app.get('/estudantes/', response_model=List[schemas.EstudanteResponse])
def read_students(db:Session=Depends(get_db)):
    students = db.query(models.Estudante).all()
    return students

@app.post('/matriculas/',response_model=schemas.MatriculaResponse)
def create_matricula(matricula:schemas.MatriculaCreate, db:Session=Depends(get_db)):
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get('/matriculas/',response_model=List[schemas.MatriculaResponse])
def read_matriculas(db:Session=Depends(get_db)):
    matriculas = db.query(models.Matricula).all()
    return matriculas

@app.get('/estudantes/{estudante_id}',response_model=schemas.LerEstudantesResponse)
def ler_estudante(estudante_id:int,db:Session=Depends(get_db)):
    estudante = db.query(models.Estudante).filter(models.Estudante.id==estudante_id).first()
    if estudante == None:
        raise HTTPException(status_code=404, detail= 'ID Não encontrada.')
    return estudante

