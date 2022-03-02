from azureml.core import Workspace

subscription_id = 'b9a6768e-15b4-423e-810f-41a0bdac4365'
resource_group  = 'DefaultResourceGroup-WUK'
workspace_name  = 'flower-nerualnetwork'

try:
    ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
    ws.write_config()
    print('Library configuration succeeded')
except:
    print('Workspace not found')