from InquirerPy import prompt

questions = [
    {
        "type": "list",
        "message": "Choose your environment:",
        "choices": ["Development", "Production", "Staging"],
        "name": "env",
    },
    {
        "type": "input",
        "message": "Enter port number:",
        "name": "port",
    }
]

answers = prompt(questions)
print(answers)
