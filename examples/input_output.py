from hera import InputParameter, OutputPathParameter, Task, Workflow, WorkflowService


def produce():
    with open("/test.txt", "w") as f:
        f.write("Hello, world!")


def consume(msg: str):
    print(f"Message was: {msg}")


with Workflow("io", service=WorkflowService(host="https://my-argo-server.com", token="my-auth-token")) as w:
    p = Task("p", produce, outputs=[OutputPathParameter("msg", "/test.txt")])
    c = Task("c", consume, inputs=[InputParameter("msg", p.name, "msg")])
    p >> c

w.create()
