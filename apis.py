from fastapi import FastAPI
from typing import Dict, Any

def create_app():
    """
    Creates the FastAPI application, exposing API endpoints for docker for each node
    """
    # get nodes
    # create kv store
    # build node configs

    app = FastAPI(title="Raft KV Node")

    @app.put("/kv/{key}")
    async def put_key(key: str, body: Dict[str, Any]):
        """
        Puts key into KV store for node
        """
        # check theres a value in the body
        # send command to node
        # get status and respond
        pass
    
    @app.delete("/kv/{key}")
    async def delete_key(key: str):
        # check key exists in body
        # send command to node
        # get status and response
        pass

    @app.get("/kv/{key}")
    async def get_key(key: str):
        # check if leader
        # if not leader, redirect to leader
        # else, return value
        # check status and respond   