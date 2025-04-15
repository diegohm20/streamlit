import streamlit as st

# Função para gerar o PDF


def gerar_pdf(nome, email, telefone, formacao, experiencia, habilidades):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Currículo", ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nome: {nome}", ln=True)
    pdf.cell(200, 10, txt=f"E-mail: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Telefone: {telefone}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Formação", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, formacao)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Experiência", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, experiencia)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Habilidades", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, habilidades)

    return pdf


# Interface do Streamlit
st.title("Gerador de Currículo em PDF")

nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
telefone = st.text_input("Telefone")
formacao = st.text_area("Formação acadêmica")
experiencia = st.text_area("Experiência profissional")
habilidades = st.text_area("Habilidades e idiomas")

if st.button("Gerar Currículo"):
    pdf = gerar_pdf(nome, email, telefone, formacao, experiencia, habilidades)
    pdf.output("curriculo.pdf")

    with open("curriculo.pdf", "rb") as f:
        st.download_button("📄 Baixar Currículo em PDF",
                           f, file_name="curriculo.pdf")
