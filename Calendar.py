import calendar
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def colorful_calendar(year, username="iitian_kundan"):
    console = Console()

    # Instagram gradient colors
    insta_colors = ["#F58529", "#FEDA77", "#DD2A7B", "#8134AF", "#515BD4"]

    def insta_username():
        text = ""
        name = f"📷 {username}"
        for i, ch in enumerate(name):
            color = insta_colors[i % len(insta_colors)]
            text += f"[{color}]{ch}[/{color}]"
        return text

    for month in range(1, 13):
        # 🔹 Instagram handle top-left me
        console.print(insta_username(), justify="left")
        console.print("")

        month_name = calendar.month_name[month]
        month_days = calendar.monthcalendar(year, month)

        table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

        # Week headers
        table.add_column("Mon", justify="center", style="green")
        table.add_column("Tue", justify="center", style="green")
        table.add_column("Wed", justify="center", style="green")
        table.add_column("Thu", justify="center", style="green")
        table.add_column("Fri", justify="center", style="yellow")
        table.add_column("Sat", justify="center", style="bright_red")
        table.add_column("Sun", justify="center", style="bright_magenta")

        # Add days
        for week in month_days:
            row = []
            for i, day in enumerate(week):
                if day == 0:
                    row.append("")
                elif i >= 5:  # Sat & Sun highlight
                    row.append(f"[bold red]{day}[/bold red]")
                else:
                    row.append(str(day))
            table.add_row(*row)

        console.print(table)
        console.print("\n" + "="*60 + "\n")

    # 🔹 Last me big chamakta panel banner
    banner_text = "✨ FOLLOW ON INSTAGRAM: " + username + " ✨"
    colorful_banner = Text()
    for i, ch in enumerate(banner_text):
        color = insta_colors[i % len(insta_colors)]
        colorful_banner.append(ch, style=f"bold {color}")

    panel = Panel(
        colorful_banner,
        border_style="bright_magenta",
        padding=(1, 2),
        expand=False
    )

    console.print("\n")
    console.print(panel, justify="center")


# Example Run
colorful_calendar(2025, "iitian_kundan")
