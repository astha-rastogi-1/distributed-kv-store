from dataclasses import dataclass
from platform import node
from typing import Dict, Any
import os

@dataclass(frozen=True)
class NodeConfig:
    node_id: str
    host: str
    port: int

    @property
    def base_url(self) -> str:
        """
        returns the base url of the node
        """
        return f"http://{self.host}:{self.port}"

def load_cluster_from_env()->Dict[str, NodeConfig]:
    """
    reads the cluster configs from env vars
    """

    cluster_env = os.getenv("RAFT_CLUSTER")
    if not cluster_env:
        # when using single nodes for local dev instead of clusters
        node_id = os.getenv("RAFT_NODE_ID", "node1")
        host = os.getenv("RAFT_HOST", "127.0.0.1")
        port = int(os.getenv("RAFT_PORT", "8000"))
        cfg = NodeConfig(node_id = node_id, host=host, port=port)
        return {node_id: cfg}
    else:
        nodes: Dict[str, NodeConfig] = {}   # creating dict of nodes with their configs
        for item in cluster_env.split(","):
            item = item.strip()
            if not item:
                continue    # node desc is bad, skip
            # node1:host:port
            parts = item.split(":")
            if len(parts)!=3:
                raise ValueError(f"Invalid RAFT_CLUSTER entry: {item}")
            node_id, host, port = parts
            nodes[node_id] = NodeConfig(node_id=node_id, host=host, port=int(port))
        return nodes
