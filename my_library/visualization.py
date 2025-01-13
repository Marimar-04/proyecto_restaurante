import matplotlib.pyplot as plt
import seaborn as sns
import folium

class Visualization:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        """Dibuja un histograma."""
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True, bins=30)
        plt.title(f'Distribución de {column}')
        plt.xlabel(column)
        plt.ylabel('Frecuencia')
        plt.show()

    def create_map(self):
        """Crea un mapa interactivo con las coordenadas."""
        m = folium.Map(location=[23.1136, -82.3666], zoom_start=12)  # Coordenadas centrales de La Habana
        for _, row in self.data.iterrows():
            folium.Marker(
                location=[float(row['latitude']), float(row['longitude'])],
                popup=row['name']
            ).add_to(m)
        return m

