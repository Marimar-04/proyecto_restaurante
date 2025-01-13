import pandas as pd
from statistics import mean

class Analysis:
    # def __init__(self):
        # self.data: pd.DataFrame = data

    def calculate_weighted_rating(self, row):
        """Calcula una valoración ponderada."""
        total_reviews = row['valoration.cant_g'] + row['valoration.cant_w'] + row['valoration.cant_t']
        if total_reviews == 0:
            return 0
        weighted = (
            row['valoration.google'] * row['valoration.cant_g'] +
            row['valoration.web'] * row['valoration.cant_w'] +
            row['valoration.tripadvisor'] * row['valoration.cant_t']
        ) / total_reviews
        return weighted

    # Función para calcular el promedio de precios por categoría
    def calculate_average_prices(self, menu):
        averages = {}
        for category, items in menu.items():
            prices = []
            if category == 'drinks' and isinstance(items, dict):
                for category_drinks, items_drinks in items.items():
                    prices = []
                    for item, details in items_drinks.items():
                        if isinstance(details, dict) and "price" in details and details["price"] is not None:
                            prices.append(details["price"])
                    if prices:
                        averages[category_drinks] = mean(prices)
            elif isinstance(items, dict):
                for item, details in items.items():
                    if isinstance(details, dict) and "price" in details and details["price"] is not None:
                        prices.append(details["price"])
                if prices:
                    averages[category] = mean(prices)
        return averages
        
    def group_by_region(self, region_column):

        """Agrupa datos por región y calcula estadísticas básicas."""
        grouped = self.data.groupby(region_column)['valoration.google']

        return grouped.mean()

    def calcular_promedio_por_municipio(self, tipo_plato):
        # Crear una lista para los promedios por municipio
        promedios_por_municipio = []

        # Agrupar por municipio
        for municipio, grupo in self.data.groupby('location.municipality'):
            # Obtener la lista de los platos del tipo seleccionado para cada restaurante
            platos = grupo['menu.card'].apply(lambda x: x.get(tipo_plato, {}))
            
            # Calcular el promedio de la cantidad de platos, manejando casos vacíos
            num_platos = platos.apply(lambda x: len(x) if isinstance(x, dict) else 0)
            promedio_platos = num_platos.mean()
            
            promedios_por_municipio.append({'municipio': municipio, 'promedio': promedio_platos})
        
        return pd.DataFrame(promedios_por_municipio)