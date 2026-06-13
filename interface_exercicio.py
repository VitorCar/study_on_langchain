# utilizando a biblioteca rich (pip install rich), esta configuração cria um painel centralizado com sombra e título.

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def interface():
    console = Console()

    console.print(
        Panel(
            "[bold white]Sistema de Resumos de Arquivos utilizando [bold cyan]IA[/bold cyan]", 
            title="[bold blue]Prompt Inicial[/bold blue]",
            border_style="cyan",
            expand=False
        )
    )

    # 1. Cabeçalho do Menu
    menu_texto = (
        "[bold cyan][1][/bold cyan] 📝 [bold white]Resumo Curto[/bold white]       [dim](Direto ao ponto)[/dim]\n"
        "[bold cyan][2][/bold cyan] 📚 [bold white]Resumo Detalhado[/bold white]   [dim](Análise profunda)[/dim]"
    )

    console.print(
        Panel(
            menu_texto,
            title="[bold magenta]⚡ Opções de Resumo[/bold magenta]",
            border_style="magenta",
            expand=False
        )
    )

    # 2. Input Inteligente (Valida automaticamente se o usuário digitou 1 ou 2)
    escolha = Prompt.ask(
        "\n[bold yellow]Digite o número da sua escolha[/bold yellow]", 
        choices=["1", "2"], 
        default="1"
    )

    # 3. Converte a escolha numérica de volta para o texto que você precisa
    summary_type = "Resumo Curto" if escolha == "1" else "Resumo Detalhado"

    # Feedback visual para o usuário confirmando a escolha
    console.print(f"\n[bold green]✓[/bold green] Selecionado: [bold underline cyan]{summary_type}[/bold underline cyan]\n")

    return summary_type
