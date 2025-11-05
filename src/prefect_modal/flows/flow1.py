from prefect import flow, task

@task()
def do_print(param: str) -> None:
    print("Doing the task")
    print(param)

@flow(log_prints=True)
def run_my_flow(param: str) -> None:
    print("flow 2")
    do_print(param)

@flow(log_prints=True)
def main(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")
    run_my_flow(name)
    if goodbye:
        print(f"Goodbye {name}!")