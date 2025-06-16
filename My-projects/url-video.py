
# importar videos desde youtube
import webbrowser

def buscar_video_youtube():
    query = input("Introduce el tema del video de YouTube que deseas buscar: ")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
