from prefect import flow, task
import modal

stub = modal.Stub("prefect-modal-example")
image = modal.Image.debian_slim().pip_install("request")

@stub.function(image=image)
def modal_task(param: str):
    import requests
    print("Running inside Modal")
    print("Param received:", param)
    print("Status from dimgi.com:", requests.get("".join(["https://", param])).status_code)

@task
def trigger_modal(param: str):
    with stub.run():
        modal_task.remote(param)

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