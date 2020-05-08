"""Console script for timesheet."""
import sys
import click
from timesheet import timesheet


@click.command()
@click.option('-s', '--server', type=(str))
def main(server):
    click.echo("See click documentation at https://click.palletsprojects.com/")
    tasks = timesheet.tasks(timesheet.get_config(server))
    for t in tasks:
        click.secho(t['name'], fg='green')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
