import pandas as pd
import json
import os
import numpy as np

class DataProcessor:
    def __init__(self, json_dir):
        """
        Inicializa el procesador con uno o más archivos JSON.
        :param json_paths: Lista de rutas de archivos JSON o un solo archivo.
        """
        self.json_dir = json_dir
        self.data = self.load_data()

    def load_data(self):
        """Carga datos de uno o varios archivos JSON y los combina en un diccionario."""
        combined_data = []  # Lista para almacenar los datos combinados
        for archivo in os.listdir(self.json_dir):
            # Obtener la ruta completa del archivo
            if archivo.endswith(".json"):  # Verifica que el archivo sea JSON
                path = os.path.join(self.json_dir, archivo)
                try:
                    with open(path, 'r', encoding='utf-8') as file:
                        data = json.load(file)  # Cargar datos JSON
                    if isinstance(data, list):
                        combined_data.extend(data)  # Si es una lista, agregar elementos
                    elif isinstance(data, dict):
                        combined_data.append(data)  # Si es un diccionario, agregarlo
                    else:
                        print(f"Formato no compatible en el archivo: {path}")
                except json.JSONDecodeError as e:
                    print(f"Error al cargar {path}: {e}")
                    continue
                except FileNotFoundError as e:
                    print(f"Archivo no encontrado: {path}")
                    continue

        if not combined_data:
            raise ValueError("No se pudieron cargar datos de los archivos proporcionados.")

        return {"data": combined_data}

    def clean_and_organize_data(self):
        """
        Limpia y organiza un DataFrame creado a partir de datos JSON de restaurantes.

        Args:
            data (list): Lista de diccionarios (datos JSON) de restaurantes.

        Returns:
            pd.DataFrame: DataFrame limpio y organizado para análisis.
        """
        
        # Normalizar las columnas anidadas
        if 'information.website' in self.data.columns:
            info_df = pd.json_normalize(self.data['information.website'])
            info_df.columns = [f'information.website_{col}' for col in info_df.columns]
            self.data = pd.concat([self.data.drop(columns=['information.website']), info_df], axis=1)

        if 'information.instagram' in self.data.columns:
            info_df = pd.json_normalize(self.data['information.instagram'])
            info_df.columns = [f'information.instagram_{col}' for col in info_df.columns]
            self.data = pd.concat([self.data.drop(columns=['information.instagram']), info_df], axis=1)

        if 'information.facebook' in self.data.columns:
            info_df = pd.json_normalize(self.data['information.facebook'])
            info_df.columns = [f'information.facebook_{col}' for col in info_df.columns]
            self.data = pd.concat([self.data.drop(columns=['information.facebook']), info_df], axis=1)

        if 'information.telephone_number' in self.data.columns:
            info_df = pd.json_normalize(self.data['information.telephone_number'])
            info_df.columns = [f'information.telephone_number_{col}' for col in info_df.columns]
            self.data = pd.concat([self.data.drop(columns=['information.telephone_number']), info_df], axis=1)
        
        # if 'location' in self.data.columns:
        #     location_df = pd.json_normalize(self.data['location'])
        #     location_df.columns = [f'location_{col}' for col in location_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['location']), location_df], axis=1)
        
        # if 'valoration' in self.data.columns:
        #     valoration_df = pd.json_normalize(self.data['valoration'])
        #     valoration_df.columns = [f'valoration_{col}' for col in valoration_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['valoration']), valoration_df], axis=1)
        
        # if 'description' in self.data.columns:
        #     description_df = pd.json_normalize(self.data['description'])
        #     description_df.columns = [f'description_{col}' for col in description_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['description']), description_df], axis=1)
        
        # if 'schedule' in self.data.columns:
        #     schedule_df = pd.json_normalize(self.data['schedule'])
        #     schedule_df.columns = [f'schedule_{col}' for col in schedule_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['schedule']), schedule_df], axis=1)
        
        # if 'logistics' in self.data.columns:
        #     logistics_df = pd.json_normalize(self.data['logistics'])
        #     logistics_df.columns = [f'logistics_{col}' for col in logistics_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['logistics']), logistics_df], axis=1)
        
        # if 'sustainability' in self.data.columns:
        #     sustainability_df = pd.json_normalize(self.data['sustainability'])
        #     sustainability_df.columns = [f'sustainability_{col}' for col in sustainability_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['sustainability']), sustainability_df], axis=1)
        
        # if 'experiences' in self.data.columns:
        #     experiences_df = pd.json_normalize(self.data['experiences'])
        #     experiences_df.columns = [f'experiences_{col}' for col in experiences_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['experiences']), experiences_df], axis=1)
        
        # if 'extras' in self.data.columns:
        #     extras_df = pd.json_normalize(self.data['extras'])
        #     extras_df.columns = [f'extras_{col}' for col in extras_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['extras']), extras_df], axis=1)
        
        # if 'pay' in self.data.columns:
        #     pay_df = pd.json_normalize(self.data['pay'])
        #     pay_df.columns = [f'pay_{col}' for col in pay_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['pay']), pay_df], axis=1)
        
        # if 'menu' in self.data.columns:
        #     menu_df = pd.json_normalize(self.data['menu'])
        #     menu_df.columns = [f'menu_{col}' for col in menu_df.columns]
        #     self.data = pd.concat([self.data.drop(columns=['menu']), menu_df], axis=1)
        
        # # Reemplazar valores faltantes
        # self.data.replace("", np.nan, inplace=True)
        # self.data.fillna({
        #     'valoration_google': 0,
        #     'valoration_web': 0,
        #     'valoration_tripadvisor': 0,
        #     'description_capacity': 0,
        #     'logistics_average_salary': 0
        # }, inplace=True)
        
        # # Convertir columnas relevantes a numéricas
        # numeric_columns = ['valoration_google', 'valoration_cant_g', 'valoration_web', 
        #                 'valoration_cant_w', 'valoration_tripadvisor', 'valoration_cant_t', 
        #                 'description_capacity', 'logistics_average_salary']
        # for col in numeric_columns:
        #     if col in self.data.columns:
        #         self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        
        # # Crear columnas calculadas (ejemplo: promedio de valoración general)
        # self.data['valoration_average'] = self.data[['valoration_google', 'valoration_web', 'valoration_tripadvisor']].mean(axis=1)
        
        # # Retornar el DataFrame limpio
        return self.data
