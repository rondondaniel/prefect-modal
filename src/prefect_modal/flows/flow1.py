from prefect import flow, task
from .modal_tasks import app, modal_task

@task
def trigger_modal(param: str):
    # Run the modal function remotely
    with app.run():
        result = modal_task.remote(param)
        print(f"Modal task result: {result}")

@task
def get_website_url(param: str) -> str:
    print("Creating website name")
    print(param)
    return ".".join([param, "com"])

@flow(log_prints=True)
def main(name: str = "dimgi", goodbye: bool = False):
    print(f"Scrapping {name} from Prefect! 🤗")
    url = get_website_url(name)
    trigger_modal(url)
    if goodbye:
        print(f"Goodbye {name}!")