from prefect import flow, task
import modal

@task
def trigger_modal(param: str):
    # Trigger modal function without waiting (fire-and-forget)
        modal_task = modal.Function.from_name("prefect-modal-example", "modal_task")
        function_call = modal_task.spawn(param)
        print(f"Modal task triggered with ID: {function_call.object_id}")
        print("Prefect will not wait for Modal to complete")

@task
def get_website_url(param: str) -> str:
    print("Creating website name")
    print(param)
    return ".".join([param, "com"])

@flow(log_prints=True)
def main(name: str = "google", goodbye: bool = False):
    if goodbye:
        print(f"Goodbye {name}!")
    print(f"Scrapping {name} from Prefect! 🤗")

    # First Job
    url = get_website_url(name)
    # Second Job
    trigger_modal(url)