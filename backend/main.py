from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post("/terraform/init")
async def terraform_init():
    try:
        result = subprocess.run(["terraform", "init"], cwd="/app/terraform", capture_output=True, text=True)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/terraform/plan")
async def terraform_plan():
    try:
        result = subprocess.run(["terraform", "plan"], cwd="/app/terraform", capture_output=True, text=True)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/terraform/apply")
async def terraform_apply():
    try:
        result = subprocess.run(["terraform", "apply", "-auto-approve"], cwd="/app/terraform", capture_output=True, text=True)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/terraform/destroy")
async def terraform_destroy():
    try:
        result = subprocess.run(["terraform", "destroy", "-auto-approve"], cwd="/app/terraform", capture_output=True, text=True)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))