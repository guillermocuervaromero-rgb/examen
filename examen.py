import streamlit as st
import pandas as pd

st.title("Examen de Clash Royale")
st.write("Buena suerte, que saques buena nota. (Cada fallo resta 0,25).")

# ------------------ PREGUNTAS ------------------
preguntas = [
    {
        "texto": "¿Cuál es el coste de elixir del Gigante?",
        "opciones": ["3", "5", "6", "4"],
        "correcta": "5"
    },
    {
        "texto": "¿Qué carta se desbloquea en la arena 3 (Barracks)?",
        "opciones": ["Mosquetera", "Príncipe", "Mini P.E.K.K.A", "Esqueleto"],
        "correcta": "Mosquetera"
    },
    {
        "texto": "¿Cuál de estas cartas es legendaria?",
        "opciones": ["Valquiria", "Leñador", "Horno", "Dragón Infernal"],
        "correcta": "Leñador"
    },
    {
        "texto": "¿Qué carta tiene la habilidad de saltar sobre tropas?",
        "opciones": ["Mini P.E.K.K.A", "Príncipe", "Caballero", "Gólem"],
        "correcta": "Príncipe"
    },
    {
        "texto": "¿Cuál es el objetivo principal en Clash Royale?",
        "opciones": [
            "Destruir la torre del Rey del enemigo",
            "Reunir elixir ilimitado",
            "Ganar cofres sin combatir",
            "Reclutar más tropas"
        ],
        "correcta": "Destruir la torre del Rey del enemigo"
    }
]

# ------------------ TABS ------------------
tab_examen, tab_informe = st.tabs(["📝 Examen", "📊 Informe"])

# ------------------ TAB EXAMEN ------------------
with tab_examen:
    with st.form("quiz_form"):
        respuestas_usuario = []

        for pregunta in preguntas:
            st.subheader(pregunta["texto"])
            eleccion = st.radio(
                "Elige una opción:",
                pregunta["opciones"],
                key=pregunta["texto"]
            )
            respuestas_usuario.append(eleccion)
            st.write("---")

        boton_enviar = st.form_submit_button("Entregar Examen")

# ------------------ CORRECCIÓN ------------------
if 'boton_enviar' in locals() and boton_enviar:

    fallos = 0
    aciertos = 0
    total = len(preguntas)

    informe_md = "# 📊 Informe del Examen\n\n"

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
            informe_md += f"✅ **{preguntas[i]['texto']}**\n"
            informe_md += f"- Tu respuesta: {respuestas_usuario[i]}\n\n"
        else:
            fallos += 1
            informe_md += f"❌ **{preguntas[i]['texto']}**\n"
            informe_md += f"- Tu respuesta: {respuestas_usuario[i]}\n"
            informe_md += f"- Respuesta correcta: {preguntas[i]['correcta']}\n\n"

    nota_base = (aciertos / total) * 10
    penalizacion = fallos * 0.25
    notafinal = round(nota_base - penalizacion, 2)
    if notafinal < 0:
        notafinal = 0

    # ------------------ MENSAJE SEGÚN NOTA ------------------
    if 1 <= notafinal <= 4:
        mensaje = "😬 Un poco flojo, ¡toca empollar!"
    elif 5 <= notafinal <= 8:
        mensaje = "🙂 Está bien, ¡se puede mejorar!"
    elif 9 <= notafinal <= 10:
        mensaje = "🎉 Perfecto, ¡excelente!"
    else:
        mensaje = ""

    informe_md += "---\n"
    informe_md += f"## 🎯 Nota final: {notafinal} / 10\n"
    informe_md += f"- Aciertos: {aciertos}\n"
    informe_md += f"- Fallos: {fallos}\n"
    informe_md += f"**{mensaje}**\n"

    # ------------------ TAB EXAMEN ------------------
    with tab_examen:
        st.divider()
        st.header(f"Resultado final: {notafinal} / 10")
        st.subheader(mensaje)

    # ------------------ TAB INFORME ------------------
    with tab_informe:
        st.markdown(informe_md)

        # ------------------ GRÁFICO DE RESULTADOS ------------------
        df = pd.DataFrame({
            'Resultado': ['Aciertos', 'Fallos'],
            'Cantidad': [aciertos, fallos]
        })
        st.subheader("📊 Gráfico de resultados")
        st.bar_chart(df.set_index('Resultado'))
