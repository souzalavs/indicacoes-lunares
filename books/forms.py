from django import forms

class BookForms(forms.Form):

    CATEGORY_OPTIONS = [
        ("CRIME", "Crime"),
        ("CIÊNCIA", "Ciência"),
        ("DRAMA", "Drama"),
        ("FANTASIA", "Fantasia"),
        ("FICÇÃO CIENTÍFICA", "Ficção Científica"),
        ("MISTÉRIO", "Mistério"),
        ("AUTORES NACIONAIS", "Autores Nacionais"),
        ("ROMANCE", "Romance"),
        ("ROMANCE DE ÉPOCA","Romance de Época"),
        ("SUSPENSE", "Suspense"),
        ("TERROR", "Terror"),
    ]
    
    title=forms.CharField(
        label='Título:',
        required=True,
        max_length=100,
    )
    
    author=forms.CharField(
        label='Autor:',
        required=True,
        max_length=100,
    )
    
    cover=forms.ImageField(
        label='Imagem da capa:'
    )
    
    synopsis=forms.CharField(
        label='Sinopse:',
        widget=forms.Textarea
    )
     
    category=forms.ChoiceField(
        label='Categoria:',
        choices=CATEGORY_OPTIONS,
        required=True 
    )