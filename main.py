from model.Deportivo import Deportivo
from model.Furgoneta import Furgoneta

objDeportivo = Deportivo('Ferrari', '488', '2021', '330')
print(objDeportivo.tipo())
print(objDeportivo.descripcion())

objFurgoneta = Furgoneta('volvo', '212', '2022', '300kg')
print(objFurgoneta.descripcion())
