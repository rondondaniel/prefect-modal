import modal

app = modal.App("prefect-modal-example")
image = modal.Image.debian_slim().pip_install("requests")

@app.function(image=image)
def modal_task(param: str):
    import requests
    print("Running inside Modal")
    print("Param received:", param)
    return f"Successfully fetched {requests.get(''.join(['https://', param])).status_code}"
