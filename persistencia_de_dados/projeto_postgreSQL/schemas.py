from pydantic import BaseModel,ConfigDict

class EstudanteBase(BaseModel):
    nome: str
    idade: int

class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class MatriculaBase(BaseModel):
    estudante_id: int
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class LerEstudantes(BaseModel):
    estudante_id: int

class LerEstudantesResponse(BaseModel):
    id: int
    nome: str
    idade: int

    model_config = ConfigDict(from_attributes=True)