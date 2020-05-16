"""Console script for timesheet."""
import sys
import click
from timesheet import timesheet


@click.command()
@click.option('-s', '--server', type=str)
@click.option('--domain', type=str)
@click.option('--id', type=int)
def main(server, domain='[]', id=0):
    click.echo("See click documentation at https://click.palletsprojects.com/")
    config = timesheet.get_config(server),
    if id:
        click.secho(timesheet.task_by_id(config, id=id))
        return 0
    tasks = timesheet.tasks(config, domain=eval(domain))
    for t in tasks:
        click.secho(t['name'], fg='green')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
