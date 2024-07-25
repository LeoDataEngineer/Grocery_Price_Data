import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def extract_text(id, url, by_type, identifier):
    # Configurar el servicio para ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    # Configurar opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Iniciar el navegador
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navegar a la página web
        print(f"Navegando a la URL: {url}")
        driver.get(url)
        
        # Hacer scroll hacia abajo para cargar el contenido si es necesario
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Esperar hasta que el contenedor de los productos esté presente
        wait = WebDriverWait(driver, 10)  # Incrementar el tiempo de espera
        print(f"Esperando el elemento con {by_type} y {identifier}")
        element = wait.until(EC.presence_of_element_located((by_type, identifier)))

        # Extraer datos utilizando el tipo de localización y el identificador proporcionado
        print(f"Elemento encontrado: {element}")

        # Obtener el texto del elemento
        text = element.text
        print(f"Texto encontrado para {id}: {text}")
        text_name = (id, text)
        
        return text_name
    except Exception as e:
        print(f"Error al extraer texto para {id} con URL {url}: {e}")
        with open(f"error_{id}.html", "w") as f:
            f.write(driver.page_source)
        return None
    finally:
        # Asegurarse de que el navegador se cierra
        driver.quit()

# Rest of the code remains the same

links_products = [
      ['1', 'Carrefour', 'azucar', 'https://www.carrefour.com.ar/azucar-comun-tipo-a-bella-vista-1-kg-421740/p', '/html/body/div[3]/div/div[1]/div/div/div/div[5]/div/div[2]/div[3]/section/div/div[2]/div/div[10]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/span/span/span[1]'],
      ['2', 'Dia', 'azucar', 'https://diaonline.supermercadosdia.com.ar/az%C3%BAcares?_q=az%C3%BAcares&map=ft', '/html/body/div[2]/div/div[1]/div/div[3]/div/div/section/div[2]/div/div[3]/section/div/div[3]/div/div[3]/div/div/div/div/div[5]/section/a/article/div/div/div[5]/div/div/div[1]/span/span/span'],
      ['3', 'Disco', 'azucar', 'https://www.disco.com.ar/azucar?_q=azucar&map=ft&page=1', '/html/body/div[2]/div/div[1]/div/div[10]/div/div[2]/section/div[2]/div/div[4]/section/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/section/a/article/div[5]/div/div/div/div[1]/div/span/div/div'],
      ['4', 'Carrefour', 'arroz', 'https://www.carrefour.com.ar/arroz-molinos-ala-parboil-bolsa-1-kg/p', '/html/body/div[3]/div/div[1]/div/div/div/div[5]/div/div[2]/div[3]/section/div/div[2]/div/div[10]/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/span/span/span'],
      ['5', 'Dia', 'arroz', 'https://diaonline.supermercadosdia.com.ar/arroz-parboil-molinos-ala-1-kg-33019/p', '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/span/span/span'],
      ['6', 'Disco', 'arroz', 'https://www.disco.com.ar/arroz?_q=arroz&map=ft', '/html/body/div[2]/div/div[1]/div/div[10]/div/div[2]/section/div[2]/div/div[4]/section/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[4]/section/a/article/div[5]/div/div/div/div[1]/div/span/div/div'],
      ['7', 'Carrefour', 'aceite', 'https://www.carrefour.com.ar/aceite-de-girasol-natura-900-cc/p','/html/body/div[3]/div/div[1]/div/div/div/div[5]/div/div[2]/div[3]/section/div/div[2]/div/div[10]/div/div/div/div/div/div[2]/div/div/div[1]'],
      ['8', 'Dia', 'aceite', 'https://diaonline.supermercadosdia.com.ar/aceite-girasol-natural-09-l-78855/p', '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[5]/div/div/div[1]/div/div'],
      ['9', 'Disco', 'aceite', 'https://www.disco.com.ar/aceite?_q=aceite&fuzzy=0&initialMap=ft&initialQuery=aceite&map=ft&operator=and&query=/aceite&searchState', '/html/body/div[2]/div/div[1]/div/div[10]/div/div[2]/section/div[2]/div/div[4]/section/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[3]/section/a/article/div[5]/div/div/div/div[1]/div/span/div/div'],
      ['10', 'Carrefour', 'leche','https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Leches?order=', '/html/body/div[3]/div/div[1]/div/div[5]/div/div/section/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/div/div[10]/div/div/div/div[1]/span/span/span[1]'],
      ['11', 'Dia', 'leche', 'https://diaonline.supermercadosdia.com.ar/leche?_q=leche&map=ft', '/html/body/div[2]/div/div[1]/div/div[3]/div/div/section/div[2]/div/div[3]/section/div/div[3]/div/div[3]/div/div/div/div/div[6]/section/a/article/div/div/div[5]/div/div/div[1]/span/span/span'],
      ['12', 'Disco', 'leche', 'https://www.disco.com.ar/leche?_q=leche&map=ft', '/html/body/div[2]/div/div[1]/div/div[10]/div/div[2]/section/div[2]/div/div[4]/section/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[6]/section/a/article/div[5]/div/div/div/div[1]/div/span/div/div']
]

columnas = ['id', 'empresa', 'producto', 'link', 'xpath']
df = pd.DataFrame(links_products, columns=columnas)

# Se extrae la data de la web
productos = []
# se recorre el dataframe df
for index, row in df.iterrows():
    # variables que se le pasan a la función
    id = row['id']
    url = row['link']
    xpath = row['xpath']
    
    result = extract_text(id, url, By.XPATH, xpath) 
    if result:  # Solo añadir si no es None
        productos.append(result)
    
    # Esperar 5 segundos antes de la siguiente iteración
    print("Esperando 1 segundos antes de la siguiente iteración...")
    # time.sleep(5)

# Imprimir el diccionario resultante
print(productos)
    
# Crear el DataFrame
df_precio = pd.DataFrame(productos, columns=['id', 'precio'])

# Hacer el merge de los DataFrames en función de la columna 'id'
df_final = pd.merge(df, df_precio, on='id')
# Nuevo orden de columnas
columnas_reordenadas = ['id', 'empresa', 'producto', 'precio', 'link', 'xpath']

# Crear un nuevo DataFrame con las columnas reordenadas
df_final = df_final[columnas_reordenadas]

# limpiaza y cambio de tipo de datos de las columnas 
def clean_price(price):
    # Eliminar el símbolo de dólar y los puntos de los miles
    clean_price = price.replace('$', '').replace('.', '').replace(',', '.')
    # Convertir a float
    return int(float(clean_price))

# Aplicar la función al DataFrame
df_final['precio'] = df_final['precio'].apply(clean_price)
df_final['id'] = df_final['id'].astype(int)
df_final

df_final.to_csv('precios.csv', index=False)
print(df_final)
