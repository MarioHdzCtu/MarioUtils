

from .defautCredential import AzureBlobManagementDefaultCredential
from .connString import AzureBlobManagementConnectionString
from .baseclass import AzureBlobManager


def create_blob_manager(self, manager: str) -> AzureBlobManager:
    managers = {
        'defaultCredential': AzureBlobManagementDefaultCredential(),
        'connectionString': AzureBlobManagementConnectionString()
    }
    if manager not in managers:
        raise ValueError(f"No factory is implemented for provided value {manager}")
    return managers[manager]
