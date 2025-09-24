import flet as ft


def main(page: ft.Page):
    page.title="galeria"
    page.bgcolor=ft.Colors.BLACK38

    jefes = [
        {
            "nombre": "rey slime",
            "vida": "2,000 en normal 2,800 en experto 3,570 en maestro",
            "manera de invocarlo": "se invoca con la corona de slime que se hacer con una corona y 50 padasos de slime o con al lluvia de slime se invoca despues de matar 50 slimes",
            "especial": "cada que recibe cierto daño invoca slimes primero invoca 26 y luego 50",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/rey%20slime.jpeg",
        },
        { 
            "nombre": "ojo de cthulhu",
            "vida": "2,800 en normal 3,640 en experto 4,641 en maestro",
            "manera de invocarlo": "puede aparecer si tienes mas 200 de vida en cada noche con un 33% de probabilidad o invocandolo solo de noche con el ojo de aspecto sospechoso",
            "especial":"vuando su ida esta a la mitad el ojo sse trasforma a su segumda fase donde empieza a hacer enbestidas hacai el jugador",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/ojo.jpeg",
        },
        {
            "nombre": "devoramundos",
            "vida": "7,485 en normal 10,479 en experto 13,361 en maestro",
            "manera de invocarlo": "se puede invocar con el cebo de gusano que se hace con 16 de carne podrida y 30 polvo vil en un altar demoniaco o rompiendo orbes en la corrupcion",
            "especial": "el gusano de divide en diferentes partes cada que recibe daño",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/devorador.jpeg",    
        },
        {
            "nombre": "cerebro de cthulhu",
            "vida": "1,250 en normal 2,125 en experto 2,279 en maestro",
            "manera de invocarlo": "rompiendo orbes en el carmesi",
            "especial": " cuando recibe daño crea ilusiones para confundir al jugador",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/cerebro.png",
        },
        {
            "nombre": "abeja reina",
            "vida": "3,400 en normal 4,720 en experto 6,069 en maestro",
            "manera de invocarlo": "rompiendo la larva que se encuentra en los panales de la jungla",
            "especial": "sus envestidas se vuelven mas rapidas mientras menos vida tengan",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/reina%20abeja.jpeg",
        },
        {
            "nombre": "esqueletron",
            "vida": "4,400 en normal 8,800 en experto 11,220 en maestro",
            "manera de invocarlo": "hablando de noche con el anciano de la mazmorra",
            "especial": "cuando pierde sus brazos su cabeza empieza a girar haciendo mucho daño",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/skeletron.jpeg",
        },
        {
            "nombre": "muro de carne",
            "vida": "sus ojos tanto en normal y experto tiene 8,000 y su boca 11,000 en meatro tiene el doble",
            "manera de invocarlo": "tirando a la lava un muñeco vudu del guia un npc",
            "especial": "cuando tenga menos vida tira ryos de sus ojos haciendo mucho daño",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/muro%20de%20carne.jpeg",
        },
        {
            "nombre": "los gemelos",
            "vida": "ambos ojos tiene la misma vida 20,000 en normal 30,000 en experto 38,250 en maestro",
            "manera de invocarlo": "tienen un 33% de pararecer cada noche",
            "especial": "cuando tiene la mitad e vida cambian de forma y hacen el triple de daño",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/los%20gemelos.jpeg",
        },    
        {
            "nombre": "eldestructor",
            "vida": "80,000 en normal 120,000 en experto 153,000 en maestro",
            "manera de invocarlo": "tiene un 33% de aparecer cada noche",
            "especial": "cuando recibe daño libera ojos mecanicos que disparan lasers",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/el%20destructor.jpeg",
        },
        {
            "nombre": "esqueletron prime",
            "vida": "29,000 en normal 42,000 en experto 53,550 en maestro",
            "manera de invocarlo": "tiene un 33% de aparecer cada noche",
            "especial": "cuando pierde los brasos su cabeza gira haciendo mucho daño",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/skeletron%20prieme.png",
        },
        {
            "nombre": "plantera",
            "vida": "30,000 en normal 42,000 en experto 53,550 en maestro",
            "manera de invocarlo": "rompiendo la flor de plantera que sale en las cavernas de la jungla",
            "especial": "cuando llega a la mitad de vida deja de lanzar esporas y comiensa a persegirte",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/plantera.png",
        },
        {
            "nombre": "golem",
            "vida": "60,000 en normal 90,000 en experto 114,749 en maestro",
            "manera de invocarlo": "se invoca con un nucleo el el templo lizhard",
            "especial": "separa su cabeza de su cuerpo y dispara lasers",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/gole.png",
        },
        {
            "nombre": "cultista lunatico",
            "vida": "32,000 en normal 40,000 en experto 51,000 en maestro",
            "manera de invocarlo": "matando alos cultistas que estan afuera de la  mazmorra",
            "especial": "no cuenta con especial",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/el%20lunatico.jpeg",      
        },   
        {
            "nombre": "moon lord",
            "vida": "145,000 en normal 217,500 en experto 277,310 en maestro",
            "manera de invocarlo": "con un sello celestial",
            "especial": "no tiene especial por que es el jefe final",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyectoprimerperiodo/refs/heads/main/moon%20lord.jpeg",
        },
    ]

    indice_actual=[0]

    contenedor=ft.Container(
        content=ft.Column([]),
        width=500,
        height=580,
        bgcolor=ft.Colors.BLUE_300,
        alignment=ft.alignment.center,
        padding=30
    )

    boton_siguiente = ft.ElevatedButton(text="Siguiente Pintura")

    def mostrar_jefe():
        jefe=jefes[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=jefe ["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(jefe["nombre"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Vida: {jefe ['vida']}",size=16),
            ft.Text(f"Manera de invocarlo: {jefe['manera de invocarlo']}",size=16),
            ft.Text(f"Especial: {jefe ["especial"]}",size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        if indice_actual[0]==len(jefes)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente jefe"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(jefes)
        mostrar_jefe()
    boton_siguiente.on_click=siguiente_click



    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              spacing=20
        ),

            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_jefe()


ft.app(main)
