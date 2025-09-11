import random
import pandas as pd
import streamlit as st


def apply_styles():
    st.markdown("""
<style>
    h1#table {
        text-align: center; !important
    }
</style>
""", unsafe_allow_html=True)


def generate_random_table():
    numbers = []

    running = True
    while running:
        number = random.randint(1, 25)

        if number not in numbers:
            numbers.append(number)

        if len(numbers) >= 25:
            running = False

    data = numbers[:5], numbers[5:10], numbers[10:15], numbers[15:20], numbers[20: 25]
    df = pd.DataFrame(data)

    return df


def color_game():
    colors = ['<p style="color: red;">AMARELO</p>',
              '<p style="color: blue;">VERDE</p>',
              '<p style="color: green;">VERDE</p>',
              '<p style="color: green;">VERMELHO</p>',
              '<p style="color: cyan;">VERMELHO</p>',
              '<p style="color: white;">PRETO</p>',
              '<p style="color: cyan;">ROXO</p>',
              '<p style="color: yellow;">ROXO</p>',
              '<p style="color: purple;">VERDE</p>',
              '<p style="color: cyan;">ROXO</p>',
              '<p style="color: red;">BRANCO</p>',
              '<p style="color: green;">PRETO</p>',
              '<p style="color: purple;">VERMELHO</p>'
            ]

    for _ in range(10):
        st.write(random.choice(colors), unsafe_allow_html=True)



def main():
    apply_styles()
    st.title("Table")

    st.write(generate_random_table())

    if st.button("Nova Tabela", type="primary", use_container_width=True):
        st.rerun()

    color_game()


main()