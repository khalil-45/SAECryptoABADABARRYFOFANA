from weasyprint import HTML
import markdown2

def convert_readme_to_pdf(input_file, output_file):
    try:
        # Convertir le fichier Markdown en HTML
        with open(input_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
            html_content = markdown2.markdown(markdown_content)

        # Générer le PDF à partir du HTML
        HTML(string=html_content).write_pdf(output_file)
        print(f"Le fichier PDF '{output_file}' a été créé avec succès!")
    
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# Utilisation de la fonction
convert_readme_to_pdf('README.md', 'README.pdf')


# Commandes à installer pour les import :
 # pip install weasyprint
 # pip install markdown2
