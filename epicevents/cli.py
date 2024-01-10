import typer

from .controllers import employees
from .auth import login_required

app = typer.Typer()


@app.command()
def login():
    """
    Connecte l'utilisateur à l'application.
    """
    employees.login()


@app.command("employees:create")
@login_required
def employees_create():
    """
    Crée un nouvel employé.
    """
    employees.create()


@app.command("employees:update")
@login_required
def employees_update(email: str):
    """
    Met à jour les données d'un employé existant.
    """
    print(email)
    employees.update(email)


@app.callback()
def main():
    """
    L'application EpicEvents fait ...
    """
