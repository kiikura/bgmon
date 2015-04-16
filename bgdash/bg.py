

site1 = {
    id: 1,
    name: "mysite_1",
    url: "https://service.url/",
    address: "192.168.11.100",
    }

n1 = {
    id: 1,
    name: "node-b",
    address: "192.168.11.1",
    mac: "ff:ff:ff:bb:bb:bb",
    url: "https://node-b/",

    active: true,
    deployment: {
        build_id: "#123",
    },
    storestate: {

    }

    }

n2 = {}
nodes = [n1, n2]

def list_site():
    pass

def retrieve_site(site_id):
    pass

def list_nodes():
    pass

def retrieve_node(node_id):
    pass

def activate_node(node_id):
    '''
    引数で指定されたノードをアクティブ化する。
    実際には
    '''


def list_deployments():
    pass

def retrieve_deployment(deploy_id):
    pass


def list_artifact():
    '''
    次に非アクティブノードにデプロイされるであろうビルド成果物の取得
    jenkins等の各種成果物のキー情報を取得する
    '''
    pass

class Node():
    deployment =
class Deployment():
    app_ver = ""
    build_id = ""



