import openai
import config
import typer
from rich import print
from rich.table import Table

""""openai.api_key = config.api_key

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                             messages=[{"role":"user","content": "Whats is the OpenAI mission"}])

#print(response)
print(response.choices[0].message.content)
"""
def main():
    openai.api_key = config.api_key
    print(f"Chat GPT API  en Python")
    table =  Table("Comando","Descripcion")
    table.add_row("exit","Salir de la aplicacion")
    table.add_row("new","Iniciar un nuevo contexto")
    print(table)
    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asiente muy util"}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🕳  Nueva conversacion creada")
            messages = [context]
            content = __prompt()

        messages.append({"role":"user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre que quieres hablar?")

    if prompt == "exit":
        exit = typer.confirm("🤢 Estas seguro")
        if exit:
            print(" 🤷‍♂️  Hasta luego")
            raise typer.Abort()
        
        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)
