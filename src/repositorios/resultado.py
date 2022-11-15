from models.resultado import Resultado
from models.mesa import Mesa
from models.candidatos import Candidato
from models.partidos import Partido
from repositorios.candidatos import CandidatoRepository
from repositorios.partidos import PartidoRepository
from repositorios.mesa import MesaRepository
from collections import Counter

class ResultadoRepository():
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
        resultado = []
        for res in Resultado.objects:
            resultado.append(res)
        return resultado
    
    def get_by_id(self, id_item):
        return Resultado.objects(id= id_item).first()
        
    def create(self, content):
        self.check_content_fields(content)
        resultado = Resultado(
            id_mesa= content.get('id_mesa'),
            id_candidato= content.get('id_candidato'),
            votos= content.get('votos')
        )
        resultado.save()
        return resultado
    
    def update(self, id_item, content):
        resultado = self.get_by_id(id_item)
        if resultado:
            resultado.update(
                id_mesa=content.get('id_mesa', resultado.id_mesa),
                id_candidato=content.get('id_candidato', resultado.id_candidato),
                votos=content.get('votos', resultado.votos)
            )
            return resultado
        return None
    
    def delete(self, id_item):
        resultado = self.get_by_id(id_item)
        if resultado:
            resultado.delete()
            return resultado
        return None
    
    def get_by_mesa(self, id_mesa):
        resultado = []
        for res in Resultado.objects(id_mesa= id_mesa):
            resultado.append(res)
        return resultado

    def get_by_candidato(self, id_candidato):
        resultado = []
        for res in Resultado.objects(id_candidato= id_candidato):
            resultado.append(res)
        return resultado
    
    def get_sum_mesa_candidato(self, id_mesa, id_candidato):
        resultado = {
            'id_mesa': id_mesa,
            'id_candidato': id_candidato,
            'votos': 0
        }
        self.check_content_fields(resultado)
        for res in Resultado.objects(id_mesa= id_mesa, id_candidato= id_candidato):
            resultado['votos'] += res.votos
        return resultado
    
    def check_content_fields(self, resultado):
        if not resultado.get('id_mesa'):
            raise Exception('id_mesa is required')
        if not resultado.get('id_candidato'):
            raise Exception('id_candidato is required')
        if not self.mesa_exists(resultado.get('id_mesa')):
            raise Exception('La mesa no existe')
        # import pdb; pdb.set_trace()
        if not self.candidato_exists(resultado.get('id_candidato')):
            raise Exception('El candidato no existe')
        return True

    def mesa_exists(self, id_mesa):
        return Mesa.objects(Nmesa= id_mesa).first() != None
    
    def candidato_exists(self, id_candidato):
    # here check using the mongodb _id of the candidato
        return Candidato.objects(id= id_candidato).first() != None

    def candidato_mesa_partido_votos(self):
        candidatos = CandidatoRepository.get_all(self)
        mesas = MesaRepository.get_all(self)
        votos_por_candidato = []
        for mesa in mesas:
            for candidato in candidatos:
                nombre_partido = Partido.objects(id= candidato.id_partido).first().nombre_partido
                votos = self.get_sum_mesa_candidato(mesa.Nmesa, candidato.id.__str__())['votos']

                votos_por_candidato.append({
                    'mesa': mesa.Nmesa,
                    'candidato': candidato.nameCandidato + ' ' + candidato.apellidoCandidato,
                    'partido': nombre_partido,
                    'votos': votos
                })

        return sorted(votos_por_candidato, key= lambda i: i['votos'], reverse= True)

    def partido_mesa_votos(self):
        prev_results = self.candidato_mesa_partido_votos()
        results_by_partido = []
        for result in prev_results:
            partido = result['partido']
            mesa = result['mesa']
            votos = result['votos']
            partido_exists = False
            for res in results_by_partido:
                if res['partido'] == partido and res['mesa'] == mesa:
                    res['votos'] += votos
                    partido_exists = True
            if not partido_exists:
                results_by_partido.append({
                    'partido': partido,
                    'mesa': mesa,
                    'votos': votos
                })
        return results_by_partido


    def mesa_votos(self):
        mesas = MesaRepository.get_all(self)
        votos_por_mesa = []
        for mesa in mesas:
            votos = self.get_sum_votos_by_mesa(mesa.Nmesa)
            votos_por_mesa.append({
                'mesa': mesa.Nmesa,
                'votos': votos
            })

        return sorted(votos_por_mesa, key= lambda i: i['votos'], reverse= False)

    def partido_votos(self):
        partidos = PartidoRepository.get_all(self)
        votos_por_partido = []
        for partido in partidos:
            votos = self.get_sum_votos_by_partido(partido.id.__str__())
            votos_por_partido.append({
                'partido': partido.nombre_partido,
                'votos': votos
            })

        return sorted(votos_por_partido, key= lambda i: i['votos'], reverse= True)

    def candidato_partido_votos_desc(self):
        candidatos = CandidatoRepository.get_all(self)
        votos_por_candidato = []
        for candidato in candidatos:
            nombre_partido = Partido.objects(id= candidato.id_partido).first().nombre_partido
            votos = self.get_sum_votos_by_candidato(candidato.id.__str__())

            votos_por_candidato.append({
                'candidato': candidato.nameCandidato + ' ' + candidato.apellidoCandidato,
                'partido': nombre_partido,
                'votos': votos
            })

        return sorted(votos_por_candidato, key= lambda i: i['votos'], reverse= True)

    def percentage_by_partido(self):
        results = self.partido_ocurrency_from_first_15_candidatos()
        percentage_of_partidos = []
        total = 0
        for result in results:
            total += result['candidatos']
        for result in results:
            percentage_of_partidos.append({
                'partido': result['partido'],
                'percentage': round((result['candidatos'] / total) * 100, 2)
            })
        return percentage_of_partidos
    
    def partido_ocurrency_from_first_15_candidatos(self):
        results = self.count_partido_candidatos(self.first_15_candidatos())
        return sorted(results, key= lambda i: i['candidatos'], reverse= True)
    
    def first_15_candidatos(self):
        candidatos = self.candidato_partido_votos_desc()
        return candidatos[:15]
    
    def count_partido_candidatos(self, collection):
        results = []
        partido_count = Counter([candidato['partido'] for candidato in collection])
        for partido, candidatos in partido_count.items():
            results.append({
                'partido': partido,
                'candidatos': candidatos
            })
        return results

    def get_sum_votos_by_candidato(self, id_candidato):     
        votos = 0
        for res in Resultado.objects(id_candidato= id_candidato):
            votos += res.votos
        return votos

    def get_sum_votos_by_mesa(self, id_mesa):
        votos = 0
        for res in Resultado.objects(id_mesa= id_mesa):
            votos += res.votos
        return votos

    def get_sum_votos_by_partido(self, id_partido):
        partido_cadidatos = Candidato.objects(id_partido= id_partido)
        votos = 0
        for candidato in partido_cadidatos:
            votos += self.get_sum_votos_by_candidato(candidato.id.__str__())
        return votos

#   def delete_database delete all resultados, candidatos, mesas and partidos
    def delete_database(self):
        Resultado.drop_collection()
        Candidato.drop_collection()
        Mesa.drop_collection()
        Partido.drop_collection()